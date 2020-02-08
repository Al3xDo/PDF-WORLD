import PyPDF2,os
pdffile=[]
for file in os.listdir('.'):
    if file.endswith('.pdf'):
        pdffile.append(file)
pdffile.sort(key=str.lower)
pdfwriter=PyPDF2.PdfFileWriter()
for file in pdffile:
    pdfreader=PyPDF2.PdfFileReader(file,'rb')
    for Pnum in range (1,pdfreader.numPages):
        pdfreaderP=pdfreader.getPage(Pnum)
        pdfwriter.addPage(pdfreaderP)
pdfresult=open('allminutes.pdf','wb')
pdfwriter.write(pdfresult)
pdfresult.close()
print('completed')