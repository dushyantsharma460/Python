# Use the external library ->  https://pypi.org/project/PyPDF2/   (py pdf2)
# Read Docs ->https://pypdf2.readthedocs.io/en/3.x/  (pypdf2 docs)

from PyPDF2 import PdfWriter

merger = PdfWriter()

pdfs = []

n = int(input("How many pdf do you want to merge ?\n"))

for i in range(0,n):
    name = input(f"Enter the name of {i + 1} pdf: ")
    pdfs.append(name)

for pdf in pdfs:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()