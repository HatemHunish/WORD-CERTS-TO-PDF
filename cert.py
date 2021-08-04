

# importing all the required modules
import PyPDF2
from PyPDF2 import PdfFileReader, PdfFileWriter
# creating an object 
file = open('certicate.pdf', 'rb')
pdf_writer = PdfFileWriter()
# creating a pdf reader object
fileReader = PyPDF2.PdfFileReader(file)
information = fileReader.getDocumentInfo()
pdf_writer.appendPagesFromReader(fileReader)
metadata = fileReader.getDocumentInfo()
pdf_writer.addMetadata(metadata)
pdf_page = fileReader.getPage(0)
print(pdf_page.extractText().replace("NEW","HATEM"))
text=pdf_page.extractText()
text=text.replace("NEW","HATEM")
print(pdf_page.extractText())

# # Write your custom metadata here:
# pdf_writer.addMetadata({
#     '/Subject': 'Example'
# })

fout = open('result.pdf', 'wb')
pdf_writer.write(fout)
# fout.close()
# # fout = open('result.pdf', 'rb')
# # fileReader2 = PyPDF2.PdfFileReader(fout)
# print(fileReader.getFormTextFields)