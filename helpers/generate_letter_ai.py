from langchain.llms import VertexAI
from templates import prompt
from class_config import download_bucket_file
from google.cloud import storage
from config_pdf import add_text_to_pdf
from create_url import upload_and_get_temporary_url
import PyPDF2

llm_model = VertexAI(model_name = "gemini-pro", max_output_tokens = 2000,temperature = 0.05)


def generate_letter_pdf(prompt):

    #output_letter_ai = llm_model.invoke(prompt)
    output_letter_ai = 'Señorita Laura,..... recibido'
    print(output_letter_ai)

    #Insertar template 
    template = download_bucket_file('Template.pdf')
    print(template)

    # Ruta del PDF de entrada
    input_pdf_path = 'pdfs/Template.pdf'
    text_to_add = output_letter_ai
    output_pdf_path = 'output_pdf_carta.pdf'
    bucket_name = 'pdf_cartas'
    blob_name = 'pdfs/output_carta.pdf'

    # Lee el contenido del archivo PDF
    with open('output_pdf_carta.pdf', 'rb') as pdf_file:
        pdf_content = pdf_file.read()

    temporary_url = upload_and_get_temporary_url(bucket_name, blob_name, pdf_content)

    temporary_url_general = 'https://storage.cloud.google.com/pdf_cartas/pdfs/output_carta.pdf'

    return temporary_url_general




