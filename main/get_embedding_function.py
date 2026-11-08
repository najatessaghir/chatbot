from langchain_ollama import OllamaEmbeddings
from django.conf import settings

def get_embeddings():
    embeddings = OllamaEmbeddings(
        model = settings.EMBEDDING_MODEL
    )
    return embeddings
