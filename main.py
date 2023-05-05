import os
import PyPDF2
import win32api
from os import system

system("title " + "Antonio Xara")

directory = os.getcwd()
folder_path = rf"{directory}"

for filename in os.listdir(folder_path):
    if filename.endswith(".pdf"):

        # Abre o arquivo PDF
        filepath = os.path.join(folder_path, filename)
        with open(filepath, "rb") as f:

            pdf_reader = PyPDF2.PdfReader(f)

            first_page = pdf_reader.pages[0]

            output_filename = "pag1_" + os.path.splitext(filename)[0] + ".pdf"
            output_filepath = os.path.join(folder_path, output_filename)

            with open(output_filepath, "wb") as out_f:
                pdf_writer = PyPDF2.PdfWriter()
                pdf_writer.add_page(first_page)
                pdf_writer.write(out_f)
                print(f'Arquivo enviado para impressão: {output_filename}')
                win32api.ShellExecute(0, "print", output_filepath, None, ".", 0)


print('Pronto!')

confirmation = input('Pressione qualquer tecla para encerrar...')
quit()

# pyinstaller --onefile --clean --name PDF-Print-1-Page main.py
