from PyPDF2 import PdfFileWriter, PdfFileReader
from getpass import getpass

pdfwriter = PdfFileWriter()
pdf = PdfFileReader('Большая шпаргалка по Python.pdf')


for page in range (pdf.numPages):
    pdfwriter.add_page(pdf.pages[page])

password = getpass(prompt='Введите пароль: ')
pdfwriter.encrypt(password)

with open ('protect.pdf', 'wb') as file:
    pdfwriter.write(file)