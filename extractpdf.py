import argparse
from PyPDF2 import PdfReader, PdfWriter

def extract_pages(input_file, output_file, pages):
    try:
        reader = PdfReader(input_file)
        writer = PdfWriter()

        # Ajustar índices para PyPDF2 (base 0)
        page_indices = [int(page) - 1 for page in pages]

        for index in page_indices:
            if index < 0 or index >= len(reader.pages):
                print(f"Advertencia: La página {index + 1} no existe en el archivo.")
                continue
            writer.add_page(reader.pages[index])

        with open(output_file, "wb") as output_pdf:
            writer.write(output_pdf)

        print(f"Archivo generado correctamente: {output_file}")
    except Exception as e:
        print(f"Error procesando el archivo: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extraer páginas específicas de un archivo PDF.")
    parser.add_argument("--file", required=True, help="Ruta del archivo PDF a procesar.")
    parser.add_argument("--pages", required=True, help="Páginas a extraer, separadas por comas (ejemplo: 1,2,3).")
    parser.add_argument("--output", required=True, help="Nombre del archivo de salida.")
    
    args = parser.parse_args()
    input_file = args.file
    output_file = args.output
    pages = args.pages.split(",")

    # Validar las páginas como números
    try:
        pages = [int(page.strip()) for page in pages]
    except ValueError:
        print("Error: Asegúrate de que las páginas estén en formato numérico, separadas por comas.")
        exit(1)

    extract_pages(input_file, output_file, pages)
