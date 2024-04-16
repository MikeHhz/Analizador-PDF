
import PyPDF2
import re

def leer_palabras_a_buscar(archivo):
    with open(archivo, 'r') as file:
        return [line.strip() for line in file]

def buscar_palabras_en_pdf(pdf_file, palabras_a_buscar):
    pdf_text = ""
    with open(pdf_file, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        for page_num in range(reader.numPages):
            page = reader.getPage(page_num)
            pdf_text += page.extract_text()

    coincidencias = set()
    for palabra in palabras_a_buscar:
        matches = re.findall(r'\b{}\b'.format(re.escape(palabra)), pdf_text, re.IGNORECASE)
        coincidencias.update(matches)

    return coincidencias

def guardar_coincidencias(coincidencias, archivo_salida):
    with open(archivo_salida, 'w') as file:
        for match in coincidencias:
            file.write(match + '\n')

if __name__ == "__main__":
    archivo_pdf = 'archivo_pdf.pdf'
    archivo_palabras = 'palabras_a_buscar.txt'
    archivo_salida = 'coincidencias.txt'

    palabras_a_buscar = leer_palabras_a_buscar(archivo_palabras)
    coincidencias = buscar_palabras_en_pdf(archivo_pdf, palabras_a_buscar)
    guardar_coincidencias(coincidencias, archivo_salida)

    print("Se han encontrado y guardado las siguientes coincidencias:")
    for match in coincidencias:
        print(match)
