from PyPDF2 import PdfFileMerger
import os

directory = os.path.dirname(os.path.realpath(__file__))
pdfs = []    

for file in os.listdir(directory):
	filename = os.fsdecode(file)
	if filename.endswith(".pdf"):
		pdfs.append(filename)


merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("result.pdf")
merger.close()
