import os
import PyPDF2
from PyPDF2 import PdfMerger
from os import system

system("title " + "Antonio Xara" + "v1.3")

folder_path = os.getcwd()
folder_path_saida = os.getcwd() + r'\resultado'

pdfs_to_merge = []
count = 0

for filename in os.listdir(folder_path):
    if filename.endswith(".pdf"):
        count += 1
        filepath = os.path.join(folder_path, filename)
        with open(filepath, "rb") as f:
            pdf_reader = PyPDF2.PdfReader(f)
            first_page = pdf_reader.pages[0]
            output_filename = "pag1_" + os.path.splitext(filename)[0] + ".pdf"
            output_filepath = os.path.join(folder_path, output_filename)
            print(f'Processando o arquivo: {filename}')
            with open(output_filepath, "wb") as out_f:
                pdf_writer = PyPDF2.PdfWriter()
                pdf_writer.add_page(first_page)
                pdf_writer.write(out_f)
        pdfs_to_merge.append(output_filepath)

merger = PdfMerger()
for pdf in pdfs_to_merge:
    merger.append(pdf)

merger.write("1-RESULTADO.pdf")
merger.close()

for file_path in pdfs_to_merge:
    os.remove(file_path)

print(f'Arquivos processados com sucesso: {count}')

# Tela para fechar o programa
confirmation = input('Pressione qualquer tecla para encerrar...')
quit()

# pyinstaller --onefile --clean --name PDF-Print-1-Page main.py
