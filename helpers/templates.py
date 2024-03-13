
Usuario = 'Name_user'
id = 'id_user'
address = 'address_user'
plate = 'plate_user'
poliza = 'poliza_number'


prompt = f"""
Redactar una respuesta a una queja a nombre de Seguros Bolívar con fecha de respuesta 11 de marzo de 2024 al cliente de nombre  con correo electrónico kbtoherreranuma@hotmail.com en donde se le ofrecen disculpas porque Negación de indemnización póliza de automóviles {poliza}
Yo, {Usuario} identificado con cédula de ciudadanía número {id}
expedida en la ciudad de Ocaña (N. de S.) y domiciliado en la dirección {address}
El Lago de la ciudad de Ocaña, en ejercicio del derecho de petición que consagra el artículo 23 de la
Constitución Política de Colombia y las disposiciones pertinentes del Código de Procedimiento
Administrativo y de lo Contencioso administrativo, respetuosamente solícito lo siguiente: El
reembolso del dinero que pagué por el servicio de grúa para mi camioneta entre Tibú y Cúcuta.

La petición anterior está fundamentada en las siguientes razones:
Tengo la camioneta de placas {plate} asegurada con Seguros Bolívar desde hace 3 años, es la
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
Atentamente,
 de su servicio de  el pasado 30 de diciembre de 1899.  Se ofrece como solución Deacuerdo al analisis del caso, Una vez recibida su solicitud, nos complace ofrecerle aclaraciones sobre las políticas 
establecidas para la prestación del servicio de grúa. De acuerdo con nuestro convenio, 
disponible para su consulta en nuestra página web https://www.segurosbolivar.com , le 
confirmamos las siguientes especificaciones.    5. SERVICIOS O CIRCUNSTANCIAS NO CUBIERTAS   LA COMPAÑÍA queda liberada de toda responsabilidad y por lo tanto no 
prestará los servicios de asistencia, cuando se presente una o más de las 
siguientes situaciones: 1. Servicios que el beneficiario haya contratado por su cuenta sin 
autorización de LA COMPAÑÍA, salvo en caso de fuerza mayor 
que le impida comunicarse con LACOMPAÑÍA.. como cierre de la respuesta mencionar canales de comunicación En los anteriores términos esperamos haber dado respuesta a todas sus inquietudes, recordando que cualquier asunto adicional con gusto será atendido, no dude en comunicarse por nuestra Página Web www.segurosbolivar.com, nuestro canal WhatsApp Corporativo: +57 322-332-2322, correo electrónico servicioalcliente@segurosbolivar.com o nuestra línea de servicio RED322, marcando desde su celular #322 o a través del número, en Bogotá 601 3122 122 o a nivel nacional 01 8000 123 322.Este párrafo de cierre debe ir tal cual en la generación de la respuesta.
NOTA: El saludo inicial debe ser el texto: cordial saludo, tal cual el ejemplo a continuación. Si bien es importante disculparse no ser tan reiterativo
Tener en cuenta el siguiente ejemplo de respuesta de queja desde su estructura y tono para la generación de la nueva respuesta:

Bogotá D.C., 11 de Agosto del 2023

Señora
YENCY 

yency@hotmail.com

Asunto: Respuesta a su Requerimiento de la Superintendencia Financiera

Cordial saludo,

Atendiendo su solicitud la cual nos fue dada a conocer por la Superintendencia Financiera, donde solicita el reintegro del dinero debitado de su cuenta de ahorros del banco Davivienda por concepto de “Asistencia Médica y Venta IGS”, los cuales en ningún momento autorizó. Al respecto nos permitimos pronunciarnos en los siguientes términos:

De acuerdo a lo expuesto en su comunicado, le indicamos que Seguros Bolívar S.A., no tiene ninguna relación con la comercialización de los servicios que le fueron debitados de su cuenta de ahorros. Aclaramos que la compañía encargada de los servicios adquiridos es Servicios Bolívar S.A., identificada con NIT. 900.311.092-7. En consecuencia, esta es la Compañía encargada de dar respuesta de fondo a la queja presentada y no Seguros Bolívar S.A.

Por lo anterior, procedimos a dar traslado de la queja a Servicios Bolívar S.A., que será la Compañía encargada de dar respuesta de fondo a la señora Yency, sobre el caso de la referencia.

En los anteriores términos esperamos haber dado respuesta a todas sus inquietudes, recordando que cualquier asunto adicional con gusto será atendido, no dude en comunicarse por nuestra Página Web www.segurosbolivar.com, nuestro canal WhatsApp Corporativo: +57 322-332-2322, correo electrónico servicioalcliente@segurosbolivar.com o nuestra línea de servicio RED322, marcando desde su celular #322 o a través del número, en Bogotá 601 3122 122 o a nivel nacional 01 8000 123 322.

Atentamente, 
"""

print(prompt)