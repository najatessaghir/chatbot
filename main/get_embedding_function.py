from langchain_community.embeddings import OllamaEmbeddings
from django.conf import settings

Model = settings.MODEL 
def get_embeddings():
    embeddings = OllamaEmbeddings(
        model = Model
    )
    return embeddings
