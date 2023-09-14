import os
import PyPDF2
from PyPDF2 import PdfMerger
from os import system

system("title " + "Antonio Xara" + " v1.3")

folder_path = os.getcwd()
folder_path_saida = os.path.join(os.getcwd(), 'resultado')

pdfs_to_merge = [os.path.join(folder_path, filename) for filename in os.listdir(folder_path) if filename.endswith(".pdf")]
count = len(pdfs_to_merge)

for pdf_path in pdfs_to_merge:
    with open(pdf_path, "rb") as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        first_page = pdf_reader.pages[0]  # Pega a primeira página
        second_page = pdf_reader.pages[1]  # Pega a segunda página
        output_filename = "pag0_AGUARDE_{}.pdf".format(os.path.splitext(os.path.basename(pdf_path))[0])
        output_filepath = os.path.join(folder_path, output_filename)
        print(f'Processando o arquivo: {os.path.basename(pdf_path)}')
        with open(output_filepath, "wb") as output_file:
            pdf_writer = PyPDF2.PdfWriter()
            pdf_writer.add_page(first_page)
            pdf_writer.add_page(second_page)  # Adiciona a segunda página ao arquivo de saída
            pdf_writer.write(output_file)

pdfs_to_merge = [os.path.join(folder_path, output_filename) for output_filename in os.listdir(folder_path) if output_filename.startswith("pag0_AGUARDE_")]

print('Compilando arquivo final, aguarde...')

merger = PdfMerger()
for pdf in pdfs_to_merge:
    merger.append(pdf)

merger.write(os.path.join(folder_path, "1-RESULTADO.pdf"))
merger.close()

for file_path in pdfs_to_merge:
    os.remove(file_path)

print(f'Arquivos processados com sucesso: {count}')

# pyinstaller --onefile --clean --icon=icon.ico --name PDF-Print-1e2 main2.py