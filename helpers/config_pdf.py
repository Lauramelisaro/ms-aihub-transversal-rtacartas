from reportlab.pdfgen import canvas

def add_text_to_pdf(input_pdf, output_pdf, text_to_add):
    # Crear un lienzo PDF
    c = canvas.Canvas(output_pdf)

    # Añadir texto al lienzo
    c.drawString(10, 800, text_to_add)  # Ajusta las coordenadas según tus necesidades

    # Guardar el lienzo como PDF
    c.save()

# Ruta del PDF de entrada
input_pdf_path = 'Template.pdf'

# Texto para añadir
text_to_add = "Señorita Laura,..... recibido"

# Ruta del PDF de salida
output_pdf_path = 'output_pdf_carta.pdf'

# Añadir texto al PDF
add_text_to_pdf(input_pdf_path, output_pdf_path, text_to_add)
