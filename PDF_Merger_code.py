import PyPDF2
import sys

input_files = sys.argv[1:]

def PDF_Merger(input):
  merger = PyPDF2.PdfFileMerger()
  for file in input:
    merger.append(file)
  merger.write('mereged_pdf.pdf')
 
PDF_Merger(input_files)
