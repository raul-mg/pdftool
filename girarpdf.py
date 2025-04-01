import PyPDF2

def girar_pdf(input_pdf, output_pdf, angulo=270):
    """
    Gira todas las páginas de un PDF en un ángulo especificado.
    
    :param input_pdf: Ruta del archivo PDF de entrada.
    :param output_pdf: Ruta del archivo PDF de salida.
    :param angulo: Ángulo de rotación, por defecto 90 grados en el sentido horario.
    """
    try:
        # Abre el archivo PDF en modo lectura binaria
        with open(input_pdf, 'rb') as archivo_entrada:
            lector_pdf = PyPDF2.PdfReader(archivo_entrada)
            escritor_pdf = PyPDF2.PdfWriter()

            # Itera sobre cada página y la gira
            for pagina in lector_pdf.pages:
                pagina_rotada = pagina.rotate(angulo)
                escritor_pdf.add_page(pagina_rotada)

            # Escribe el nuevo archivo PDF
            with open(output_pdf, 'wb') as archivo_salida:
                escritor_pdf.write(archivo_salida)

        print(f"El archivo PDF ha sido girado y guardado como: {output_pdf}")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

# Ejemplo de uso
entrada = "INE.pdf"
salida = "DIAPOSITIVA_FIXED.pdf"
girar_pdf(entrada, salida)
