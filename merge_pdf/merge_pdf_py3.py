from tkinter import *
from PyPDF2 import PdfFileMerger
from tkinter import filedialog, messagebox

list_of_files = []
count = 0


def getPdfPath():
    global count
    filez = filedialog.askopenfilename(parent=root, title='Choose a file', )
    print(filez)
    if filez:
        list_of_files.append(filez)
    var1 = StringVar()
    label1 = Label(root, textvariable=var1)
    var1.set(filez)
    label1.place(x=2, y=65 + (count * 20))
    count += 1


def mergePdfs():
    merger = PdfFileMerger()
    path = "/".join(list_of_files[0].split("/")[:-1])
    for pdf in list_of_files:
        merger.append(pdf)
    merger.write(path + "/" + T.get('1.0', "end-1c") + ".pdf")
    merger.close()
    messagebox.showinfo(title='Status', message='File created with file name %s' % T.get('1.0', "end-1c") + ".pdf")


def addselectfile():
    B = Button(root, text='Select File', command=getPdfPath)
    B.place(x=1, y=40)


root = Tk()
root.resizable()
root.geometry("400x300")
root.title("Merge PDF files")

var = StringVar()
label = Label(root, textvariable=var)
var.set("Final PDF file Name : ")
label.place(anchor=NW)

T = Text(root, height=2, width=30)
T.place(relx=1, x=-2, y=2, anchor=NE)
T.insert(END, "Enter_final_file_name_here")

var = StringVar()
label = Label(root, textvariable=var)
var.set("* with same name old file will get replaced\n*final file will be saved in same folder as per selected file")
label.place(relx=1, x=1, y=30, anchor=NE)

addselectfile()

B2 = Button(root, text='Merge Files', command=mergePdfs)
B2.place(x=300, y=250)

mainloop()
