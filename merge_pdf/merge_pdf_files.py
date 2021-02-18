import Tkinter as tk
import tkFileDialog
import tkMessageBox

from PyPDF2 import PdfFileMerger

list_of_files = []


def getPdfPath():
    filez = tkFileDialog.askopenfilename(parent=root, title='Choose a file', )
    print(filez)
    list_of_files.append(filez)


def mergePdfs():
    merger = PdfFileMerger()
    path = "/".join(list_of_files[0].split("/")[:-1])
    for pdf in list_of_files:
        merger.append(pdf)
    merger.write(path + "/" + T.get('1.0', "end-1c") + ".pdf")
    merger.close()
    tkMessageBox.showinfo(title='Status', message='File created with file name %s' % T.get('1.0', "end-1c"))


def addselectfile():
    B = tk.Button(frame, text='Select File', command=getPdfPath)
    B.pack(side=tk.LEFT)


root = tk.Tk()
# root.resizable()
root.geometry("300x100")
# root.minsize(300, 100)
root.title("Merge PDF files")
frame = tk.Frame(root)
frame.pack()

var1 = tk.StringVar()
label1 = tk.Label(frame, textvariable=var1)
var1.set("Enter output file name below")
label1.pack()

T = tk.Text(frame, height=1, width=30)
T.pack()
T.insert(tk.END, "Enter_final_file_name_here")

var = tk.StringVar()
label = tk.Label(frame, textvariable=var)
var.set("* with same name old file will get replaced\n*final file will be saved in same folder as per selected file")
label.pack()

addselectfile()

# B1 = tk.Button(frame, text='Add more', command=addselectfile)
# B1.pack(side=tk.LEFT)

B2 = tk.Button(frame, text='merge files', command=mergePdfs)
B2.pack(side=tk.LEFT)

tk.mainloop()
