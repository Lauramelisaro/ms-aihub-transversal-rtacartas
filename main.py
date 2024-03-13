import os
from helpers.generate_letter_ai import generate_letter_pdf
from fastapi import Request, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field


class TextInputCoberturas(BaseModel):
   # categoria: str = Field(..., example="Asistencia", description="Area de negocio")
   # motivo: str = Field(..., example="Demora En Servicio Requerido", description="Clasificación de la causal de la queja")
    queja: str = Field(..., example="""Yo, USER identificado con cédula de ciudadanía número ID
    expedida en la ciudad de Ocaña (N. de S.) y domiciliado en la dirección ADDRESS
    El Lago de la ciudad de Ocaña, en ejercicio del derecho de petición que consagra el artículo 23 de la
    Constitución Política de Colombia y las disposiciones pertinentes del Código de Procedimiento
    Administrativo y de lo Contencioso administrativo, respetuosamente solícito lo siguiente: El
    reembolso del dinero que pagué por el servicio de grúa para mi camioneta entre Tibú y Cúcuta.

    La petición anterior está fundamentada en las siguientes razones:
    Tengo la camioneta de placas plate asegurada con Seguros Bolívar desde hace 3 años, es la
    primera vez que hago uso del seguro. La camioneta en estos momentos se moviliza en Tibú, pero
    para cualquier mantenimiento o reparación la ciudad a dónde se lleva es Cúcuta, yo le informé a mi
    asesora que la camioneta se encontraba operando en esa zona y ella me dijo que la directora
    comercial consultó con la parte técnica de Seguros Bolívar y le dieron el visto bueno para la
    circulación en ese sitio, con la salvedad que los servicios de asistencia tendrían que ser por
    reembolso porque no tienen proveedores por esa zona. La camioneta se varó en un lugar donde no
    había señal, por lo cual el reporte no se pudo hacer si no al día siguiente, cuando ya habían
    trasladado la camioneta a Cúcuta, es evidente que el vehículo no se podía dejar en la vía por
    seguridad, mientras la aseguradora autorizaba el servicio. Por tal motivo, solicito nuevamente el
    reembolso del dinero que debí pagar por la grúa que trasladó el vehículo.
    Atentamente,""", description="Relato del usuario dónde se detalla la inconformidad ")

    #info_gestion: str = Field(..., example="""de su servicio de  el pasado 30 de diciembre de 1899.  Se ofrece como solución Deacuerdo al analisis del caso, Una vez recibida su solicitud, nos complace ofrecerle aclaraciones sobre las políticas 
    #establecidas para la prestación del servicio de grúa. De acuerdo con nuestro convenio, 
    #disponible para su consulta en nuestra página web https://www.segurosbolivar.com , le 
    #confirmamos las siguientes especificaciones.    5. SERVICIOS O CIRCUNSTANCIAS NO CUBIERTAS   LA COMPAÑÍA queda liberada de toda responsabilidad y por lo tanto no 
    #restará los servicios de asistencia, cuando se presente una o más de las 
    #siguientes situaciones: 1. Servicios que el beneficiario haya contratado por su cuenta sin 
    #autorización de LA COMPAÑÍA, salvo en caso de fuerza mayor 
    #que le impida comunicarse con LACOMPAÑÍA.""", description="Datos relevantes, que guien la respuesta de la carta ")
    
    

# Parametros básicos y clases
app = FastAPI()
puerto = os.environ.get("PORT", 8080)
project_id = os.environ.get("PROJECT", "sb-prototipos-xops")

# Configuración de CORS
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Endpoint para Path de motor de coberturas
descripcion_path_evento = 'Este endpoint toma la queja reportada por un usuario y genera una carta como respuesta'
@app.post("/rtcartas-pdf", ssummary="Procesamiento de carta", description=descripcion_path_evento)
async def generalo_chat(input: TextInputCoberturas):
    pdf_url = generate_letter_pdf(input.queja)
    return pdf_url


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=int(puerto))


# uvicorn main:app --host 0.0.0.0 --port 8080
