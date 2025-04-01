import pytesseract
from PyPDF2 import PdfReader
from pdf2image import convert_from_path
from pathlib import Path

# Configura Tesseract OCR si es necesario (para sistemas Windows)
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extraer_texto_ocr(pdf_path, output_txt):
    """
    Realiza OCR en cada página de un PDF y guarda el contenido como un documento de texto.
    
    :param pdf_path: Ruta del archivo PDF de entrada.
    :param output_txt: Ruta del archivo de texto de salida.
    """
    try:
        # Verifica que el PDF existe
        pdf_path = Path(pdf_path)
        if not pdf_path.is_file():
            print(f"El archivo {pdf_path} no existe.")
            return
        
        # Convierte las páginas del PDF a imágenes
        print(f"Convirtiendo páginas del PDF a imágenes...")
        paginas = convert_from_path(pdf_path, dpi=300)
        
        contenido = []
        for i, pagina in enumerate(paginas, start=1):
            print(f"Procesando página {i}...")
            
            # Realiza OCR en la imagen
            texto = pytesseract.image_to_string(pagina, lang="spa")  # Cambia "spa" a otro idioma si es necesario
            contenido.append(f"Página {i}:\n\n{texto.strip()}\n\n{'='*40}\n")
        
        # Escribe el texto extraído en el archivo de salida
        with open(output_txt, "w", encoding="utf-8") as archivo_salida:
            archivo_salida.writelines(contenido)
        
        print(f"El texto extraído ha sido guardado en: {output_txt}")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

# Ejemplo de uso
entrada = "DIAPOSITIVA_FIXED.pdf"
salida = "texto_extraido.txt"
extraer_texto_ocr(entrada, salida)
