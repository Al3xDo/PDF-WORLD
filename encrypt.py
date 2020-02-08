import os,PyPDF2,random
def encrypt():
    for fname in fileinfo:
        n=random.randint(0,len(content))
        print('Đã chọn '+content[n].strip()+' là 1 mật khẩu')
        pdfobj=PyPDF2.PdfFileReader(open(fname,'rb'))
        pdfwriter=PyPDF2.PdfFileWriter()
        # giữa
        for Pnum in range(0,pdfobj.numPages):
            pdfobjP=pdfobj.getPage(Pnum)
            pdfwriter.addPage(pdfobjP)
        # kết
        pdfwriter.encrypt(content[n].strip())
        resultname=os.path.join(dirname,'encrypted'+fname)
        pdfresult=open(resultname,'wb')
        pdfwriter.write(pdfresult)
        pdfresult.close()
def decrypt():
    for fname in fileinfo2:
        pdfobj=PyPDF2.PdfFileReader(open(fname,'rb'))
        pdfwriter=PyPDF2.PdfFileWriter()
        # giữa
        for n in range(0,len(content)):
            if pdfobj.decrypt(content[n].strip())==0:
                continue
            elif pdfobj.decrypt(content[n].strip())==1:
                pdfobj.decrypt(content[n].strip())
                print(content[0].strip() + ' là mật khẩu của '+ fname)
        for Pnum in range(0,pdfobj.numPages):
            pdfobjP=pdfobj.getPage(Pnum)
            pdfwriter.addPage(pdfobjP)
        # kết
        fname=fname[8:]
        resultname=os.path.join(dirname,'decrypted'+fname)
        pdfresult=open(resultname,'wb')
        pdfwriter.write(pdfresult)
        pdfresult.close()
print('Mời bạn nhập vào file keys: ')
Kname=input()
if not Kname.endswith('.txt'):
    Kname=Kname+'.txt'
fileinfo=[]
print('Đang tìm các file pdf')
for fname in os.listdir('.'):
    if fname.endswith('.pdf'):
        fileinfo.append(fname)
textf=open(Kname,'r')
content=textf.readlines()
absname=os.getcwd()
print('1. Mã hóa')
print('2. Giải mã')
x=input()
if x=='1':
    print('Đang setup....')
    dirname=os.path.join(absname,'file đã mã hóa')
    os.makedirs(dirname,exist_ok=True)
    encrypt()
    os.chdir(absname)
elif x=='2':
    fileinfo2=[]
    print('Đang setup....')
    dirname=os.path.join(absname,'file đã giải mã')
    os.makedirs(dirname,exist_ok=True)
    for fname in os.listdir('.'):
        if fname.startswith('encrypted') and fname.endswith('.pdf'):
            fileinfo2.append(fname)
    decrypt()