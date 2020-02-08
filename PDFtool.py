import PyPDF2,os,pprint,re

# giao diện
print('Chào mừng bạn đến với PDF Tool:')
print('CHƯƠNG TRÌNH SẼ NHẬN FILE VÀ TẠO FILE TRONG ĐƯỜNG DẪN')
print(os.getcwd())
print('Để thay đổi đường dẫn hãy nhập vào địa chỉ của thư mục chứ file cần xử lý (bỏ trống sẽ mặc định đường dẫn trên):')
dirname=input()
if dirname!='':
    os.path.abspath(dirname)
    os.chdir(dirname)
    print('Đường dẫn đã thay đổi thành '+ dirname)
print('Mời bạn đặt tên cho file PDF do chương trình tạo ra: (enter sẽ mặc định là Py-name) ')
name=input()
if name=='':
    name='Py-'
# giao diện 2
# LƯU Ý SỬ DỤNG ENDSWITH= HAY HƠN REGEX
print('Các tool có trong phần mềm: ')
print('1. Tạo file PDF mới với Watermark')
print('2. Cắt ghép file PDF (trong cùng 1 file)')
print('3. Tạo file (.txt) mới với bản text thô từ file PDF: ')
print('4. Cài đặt mật mã cho các file PDF (nhiều file): ')
print('5. Đọc file mật khẩu và giải mã các file PDF: ')
print('6. Tra cứu thông tin của file PDF (nhiều file) ')
x=input()

# xử lý
if x=='1':
    # chức năng 1
    print('TẠO FILE PDF VỚI WATERMARK'.center(50,'*'))
    # mở 2 file pdf + xử lý thông tin người nhập
    print('Nhập tên file 1: ')
    fname=input()
    if fname.endswith('.pdf',len(fname)-4)==False:
        fname=fname+'.pdf'
    pdfobj=PyPDF2.PdfFileReader(fname,'rb')
    print('Nhập tên file watermark: ')
    fname=input()
    if fname.endswith('.pdf',len(fname)-4)==False:
        fname=fname+'.pdf'
    pdfWM=PyPDF2.PdfFileReader(fname,'rb')
    # ghép watermark
    print('chọn số trang bạn muốn ghép: (tính từ trang đầu tiên là 0)')
    n=int(input())
    pdfwriter=PyPDF2.PdfFileWriter()
    print('....')
    for i in range (0,n+1):
        pdfobjP=pdfobj.getPage(i)
        pdfobjP.mergePage(pdfWM.getPage(0))
        pdfwriter.addPage(pdfobjP)
    for k in range(n+1,pdfobj.numPages):
        pdfobj1=pdfobj.getPage(k)
        pdfwriter.addPage(pdfobj1)
    num=1
    while True:
        pdfname=name+str(num)+'-CN1'+fname
        if not os.path.exists(pdfname):
            break
        num=num+1
    pdfresult=open(pdfname,'wb')
    pdfwriter.write(pdfresult)
    pdfresult.close()
    print('Đã hoàn tất')
elif x=='2':
    # chức năng 2
    print('CẮT GHÉP CÁC TRANG TRONG CÙNG 1 FILE PDF'.center(50,'-'))
    print('1. Cắt trang rồi ghép thành file mới: ')
    print('2. Cắt ghép file PDF (2 file khác nhau) (đang bảo trì)')
    x2=input()
    if x2=='1':
        print('1. Cắt trang rồi ghép thành file mới: ')
        # xử lý dữ liệu đầu vào
        print('Nhập tên file PDF: ')
        fname=input()
        if fname.endswith('.pdf',len(fname)-4)==False:
            fname=fname+'.pdf'
        pdfobj2=PyPDF2.PdfFileReader(fname,'rb')
        print('Nhập các trang cần ghép (với các trang liên tiếp thì cách nhau bằng dấu gạch -): ')
        x=list(map(str,input().strip().split()))
        print('Đang xử lý....')
        pdfwriter2=PyPDF2.PdfFileWriter()
        for i in x:
            if len(i)>1:
                for k in range(int(i[0]),int(i[2])+1):
                    pdfobj2P=pdfobj2.getPage(k)
                    pdfwriter2.addPage(pdfobj2P)
            else:
                pdfobj2P=pdfobj2.getPage(int(i))
                pdfwriter2.addPage(pdfobj2P)
        num=1
        while True:
            pdfname2=name+str(num)+'-'+fname
            if not os.path.exists(pdfname2):
                break
            else:
                num=num+1
        pdfresult2=open(pdfname2,'wb')
        pdfwriter2.write(pdfresult2)
        pdfresult2.close()
        print('Đã hoàn tất')
    elif x2=='2':
        '''# xử lý dữ liệu đầu vào
        print('2. Cắt ghép file PDF (2 file khác nhau) ')
        pdfobj1=PyPDF2.PdfFileReader(open('meetingminutes.pdf','rb'))
        pdfobj2=PyPDF2.PdfFileReader(open('meetingminutes2.pdf','rb'))
        print('CHÚ Ý CÁC TRANG SẼ SẮP XẾP THEO THỨ TỰ NHẬP'.center(50,'*'))
        print('FILE CÓ DẤU * SẼ ƯU TIÊN GHÉP VÀO TRƯỚC THEO THỨ TỰ NHẬP')
        print('FILE 1 SẼ CẮT RA VÀ GHÉP VÀO TRƯỚC, SAU ĐÓ BẠN SẼ CHỌN TRANG TỪ FILE 2 ĐỂ CHÈN VÀO')
        print('Nhập trang cần ghép của file thứ nhất: ')
        x21=list(map(str,input().strip().split()))
        print('Đang xử lý file 1... ')
        for i in x:
            if len(i)>1:
                for k in range(int(i[0]),int(i[2])+1):
                    pdfobj1P=pdfobj1.getPage(k)
                    pdfwriter.addPage(pdfobj1P)
            else:
                pdfobj1P=pdfobj1.getPage(int(i))
                pdfwriter.addPage(pdfobj1P)
        print('Nhập trang cần ghép của file thứ hai: ')
        x22=list(map(str,input().strip().split()))
'''
elif x=='3':
    # xử lý chức năng 3
    #xử lý dữ liệu đầu vào
    print('3. Tạo file (.txt) mới với bản text thô từ file PDF: ')
    print('Nhập tên file PDF: ')
    fname=input()
    if fname.endswith('.pdf',len(fname)-4)==False:
        fname=fname+'.pdf'
    pdfobj=PyPDF2.PdfFileReader(fname,'rb')
    print('Nhập các trang bạn cần trích xuất text (với các trang liên tiếp thì cách nhau bằng dấu -): ')
    x3=list(map(str,input().strip().split()))
    print('Đang xử lý....')
    num=1
    while True:
        pdfname=name+str(num)+fname+'.txt'
        if not os.path.exists(pdfname):
            break
        else:
            num=num+1
    pdftext=open(pdfname,'w')
    for i in x3:
        if len(i)>1:
                for k in range(int(i[0]),int(i[2])+1):
                    pdfobjP=pdfobj.getPage(k)
                    pdftext.write(pdfobjP.extractText())
                    pdftext.write('\n')
        else:
            pdfobjP=pdfobj.getPage(int(i))
            pdftext.write(pdfobjP.extractText())
            pdftext.write('\n')
    print('Đã hoàn tất')
    pdftext.close()
elif x=='4':
    print('4. Cài đặt mật mã cho các file PDF ( nhiều file): ')
    print('LƯU Ý FILE CHƯƠNG TRÌNH SẼ CHỈ TẠO RA CÁC FILE COPY ĐÃ MÃ HÓA:')
    print('các file đã mã hóa sẽ được tạo trong 1 file ')
    dirname=os.path.join('.','file PDF đã mã hóa')
    os.makedirs(dirname,exist_ok=True)
    fpdf=re.compile(r'^(.*?)(.pdf)$')
    print('Nhập vào mật khẩu: ')
    passw=input()
    dem=1
    print('Đang xử lý....')
    for file in os.listdir('.'):
        n=fpdf.search(file)
        if n==None:
            continue
        else:
            pdff=PyPDF2.PdfFileReader(open(n.group(0),'rb'))
            pdfwriter=PyPDF2.PdfFileWriter()
            for pagenum in range(pdff.numPages):
                pdffP=pdff.getPage(pagenum)
                pdfwriter.addPage(pdffP)
            pdfwriter.encrypt(passw)
            tname=os.path.join(dirname,'đã mã hóa '+n.group(0))
            pdfresult=open(tname,'wb')
            pdfwriter.write(pdfresult)
            pdfresult.close()
            print('Đã hoàn tất file thứ '+str(dem))
            dem=dem+1
elif x=='6':
    print('6. Tra cứu thông tin của file PDF: ')
    # xử lý dữ liệu đầu vào
    pdfinfo={}
    while True:
        print('Nhập tên file PDF (enter để thoát): ')
        fname=input()
        if fname=='':
            break
        if fname.endswith('.pdf',len(fname)-4)==False:
            fname=fname+'.pdf'
        pdfobj=PyPDF2.PdfFileReader(fname,'rb')
        pdfinfo[fname]={}
        pdfinfo[fname]['Pages Num: ']=pdfobj.numPages
        if pdfobj.isEncrypted==True:
            pdfinfo[fname]['Password: ']='YES'
        else:
            pdfinfo[fname]['Password: ']='NO'
        # hiển thị file
        print('1. In trong terminal')
        print('2. In trong file text (.txt)')
        x6=input()
        if x6=='1':
            print(pprint.pformat(pdfinfo,indent=4))
        if x6=='2':
            print('Đang ghi dữ liệu...')
            tname=fname+'.txt'
            tfile=open('thông tin của file pdf','w')
            tfile.write(pprint.pformat(pdfinfo,indent=4))
            tfile.close()
            print('Đã hoàn tất')



