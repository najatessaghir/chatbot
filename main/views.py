from django.shortcuts import render
from django.http import  JsonResponse
from django.contrib.auth.decorators import login_required
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.schema.document import Document
from .get_embedding_function import get_embeddings
from langchain.prompts import ChatPromptTemplate
from langchain_community.llms.ollama import Ollama
from .models import Chat , Exchange
import os
import shutil
from django.conf import settings
model = 'mistral'
Model = settings.MODEL 
# Create your views here.

db_not_loaded = True

CHROMA_PATH = "chroma"

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_PATH = os.path.join(BASE_DIR, 'main', 'data')

PROMPT_TEMPLATE = """
Answer the query based only on the following context:

{context}

---

Answer the query based on the above context: {question}
"""

import argparse

def initialise():
    # Create (or update) the data store.
    documents = load_documents()
    chunks = split_documents(documents)
    add_to_chroma(chunks)

def load_documents():
    document_loader = PyPDFDirectoryLoader(DATA_PATH)
    return document_loader.load()

def split_documents(documents: list[Document]):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=80,
        length_function=len,
        is_separator_regex=False,
    )
    return text_splitter.split_documents(documents)

def add_to_chroma(chunks: list[Document]):
    # Load the existing database.
    db = Chroma(
        persist_directory=CHROMA_PATH, embedding_function=get_embeddings()
    )

    # Calculate Page IDs.
    chunks_with_ids = calculate_chunk_ids(chunks)

    # Add or Update the documents.
    existing_items = db.get(include=[])  # IDs are always included by default
    existing_ids = set(existing_items["ids"])
    print(f"Number of existing documents in DB: {len(existing_ids)}")

    # Only add documents that don't exist in the DB.
    new_chunks = []
    for chunk in chunks_with_ids:
        if chunk.metadata["id"] not in existing_ids:
            new_chunks.append(chunk)

    if len(new_chunks):
        print(f"👉 Adding new documents: {len(new_chunks)}")
        new_chunk_ids = [chunk.metadata["id"] for chunk in new_chunks]
        db.add_documents(new_chunks, ids=new_chunk_ids)
        db.persist()
    else:
        print("✅ No new documents to add")

def calculate_chunk_ids(chunks):

    # This will create IDs like "data/monopoly.pdf:6:2"
    # Page Source : Page Number : Chunk Index

    last_page_id = None
    current_chunk_index = 0

    for chunk in chunks:
        source = chunk.metadata.get("source")
        page = chunk.metadata.get("page")
        current_page_id = f"{source}:{page}"

        # If the page ID is the same as the last one, increment the index.
        if current_page_id == last_page_id:
            current_chunk_index += 1
        else:
            current_chunk_index = 0

        # Calculate the chunk ID.
        chunk_id = f"{current_page_id}:{current_chunk_index}"
        last_page_id = current_page_id

        # Add it to the page meta-data.
        chunk.metadata["id"] = chunk_id

    return chunks

def clear_database():
    if os.path.exists(CHROMA_PATH):
        shutil.rmtree(CHROMA_PATH)

def query_rag(query_text: str):
    global db_not_loaded
    if db_not_loaded:
        #initialize the database
        initialise()
        db_not_loaded = False
    # Prepare the DB.
    embedding_function = get_embeddings()
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)

    # Search the DB.
    results = db.similarity_search_with_score(query_text, k=5)

    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query_text)
    # print(prompt)

    model = Ollama(model=Model)
    response_text = model.invoke(prompt)

    sources = [doc.metadata.get("id", None) for doc, _score in results]
    formatted_response = f"Response: {response_text}\nSources: {sources}"
    print(formatted_response)
    return response_text


def home(request):
    return render(request, 'main/home.html')
@login_required
def chat_page(request):
    # Get all the chats the user was in
    chat = Chat.objects.filter(user=request.user).first()
    
        
    if chat:
            exchanges = chat.exchanges.all()  # Use the related name 'exchanges'
            return render(request, 'main/main.html', { 'chat': chat, 'exchanges': exchanges})
    else:
            # If the chat does not exist, create it
            chat = Chat.objects.create(user=request.user, name=f"Chat with {request.user.username}")
            chat.save()
            exchanges = chat.exchanges.all()  # Use the related name 'exchanges'
            return render(request, 'main/main.html', {'chat': chat, 'exchanges': exchanges})

def response(request , question ) :
     response_text = query_rag(question)
     response = {
         "response" : response_text
     }
     chat = Chat.objects.get(user = request.user)
     exchange = Exchange(question=question, 
                         response=response_text,    
                         chat=chat 
                         )
     exchange.save()

     return JsonResponse(response)
