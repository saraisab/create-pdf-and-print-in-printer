from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import win32api

def crear_pdf_con_copias(imagen_png, nombre_pdf, num_copias):
    """ 
    creates a pdf file 
    params: 
      imagen_png: image in png format
      nombre_pdf: pdf file name
      num_copias: number of copies of the image in the pdf file that we are generating
    """
    try:
        # Obtener las dimensiones de la imagen
        with Image.open(imagen_png) as img:
            img_width, img_height = img.size

        # Crear un lienzo para el PDF
        c = canvas.Canvas(nombre_pdf, pagesize=A4)

        # Dimensiones de la página
        page_width, page_height = A4

        # Escalar la imagen para que quepa en la página
        scale = min(page_width / img_width, page_height / img_height)
        scaled_width = img_width * scale
        scaled_height = img_height * scale

        # Añadir varias copias de la imagen al PDF
        for copia in range(num_copias):
            c.drawImage(imagen_png,
                        x=(page_width - scaled_width) / 2,  # Centrar horizontalmente
                        y=(page_height - scaled_height) / 2,  # Centrar verticalmente
                        width=scaled_width,
                        height=scaled_height,
                        preserveAspectRatio=True,
                        mask='auto')
            c.showPage()  # Añadir una nueva página para la siguiente copia

        # Guardar el PDF
        c.save()
        print(f"PDF '{nombre_pdf}' creado con éxito con {num_copias} copias de la imagen.")

    except Exception as e:
        print(f"Error al crear el PDF: {e}")


def imprimir_etiqueta(archivo):
    """
    prints the pdf file
    """
    try:
        impresora = etiqueta["impresora_final"]  # printer name
        win32api.ShellExecute(
            0,
            "printto",
            archivo,
            f'"{impresora}"',  # None,
            ".",
            0
        )

        print(f"PDF enviado a la impresora '{impresora}'.")

    except Exception as e:
        print(f"Error al imprimir el PDF: {e}")
