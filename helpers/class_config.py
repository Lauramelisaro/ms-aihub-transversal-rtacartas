import vertexai
from vertexai.language_models import TextEmbeddingModel
from langchain.llms import VertexAI
from langchain.chat_models import ChatVertexAI
#from langchain_google_vertexai import VertexAI
import gcsfs
import pandas as pd
from google.cloud import storage

class Config():
    """
    Contains the configuration of the LLM.
    """
    vertexai.init(project="sb-xops-prod", location="us-central1")
    embedding_model = TextEmbeddingModel.from_pretrained("textembedding-gecko@003")
    llm_model = VertexAI(model_name = "gemini-pro", max_output_tokens = 2000,temperature = 0.05)
    chat_model = ChatVertexAI(model_name="chat-bison", max_output_tokens=2000, temperature=0.1)
    

config = Config()

from google.cloud import storage

from google.cloud import storage

def download_bucket_file( file_name):
    # Configura el cliente de Storage
    bucket_name = 'prototipado_coberturas'
    destination_path = 'Template.pdf'
    client = storage.Client()

    # Selecciona el bucket
    bucket = client.bucket(bucket_name)

    # Selecciona el objeto Blob
    blob = bucket.blob(file_name)

    # Descarga el archivo PDF al destino especificado
    blob.download_to_filename(destination_path)

