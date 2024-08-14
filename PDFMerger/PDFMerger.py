#Name: PDFMerger
#Developer: Zach Demetriou
#Description: Takes user input of two or more files and merges them into one document in the order given
#Usage: CMD = Python PDFMerger.py *.pdf *.pdf

#needed libraries
import sys
import PyPDF2

#Create PDFMerger Obj & file list dictionary
mergedPDF = PyPDF2.PdfMerger()
filesToMerge = {}

#Get all files from terminal arguments and store in dictionary
for i, args in enumerate(sys.argv):
    if str(sys.argv[i]).endswith(".pdf"):
        filesToMerge[f'file_{i}'] = sys.argv[i]

#Append all valid files to mergedPDF Obj
for file in filesToMerge:
    if file is not None:
        mergedPDF.append(filesToMerge[file])

#Merge all valid files into a .pdf
mergedPDF.write("Combined.pdf")