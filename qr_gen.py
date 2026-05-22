from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import qrcode
import os

root=Tk()
root.geometry("340x550")
root.resizable(False,False)
root.iconbitmap(r"D:\جابر\zezo\PythonProjects\QR Code Generator - EN\qr-code.ico")
root.title("QR Code Generator")
root.configure(background="aliceblue")

def save_qr():
    file=filedialog.asksaveasfile(mode='w',filetypes=[('PNG Files','*.png'),('JPEG Files','*.jpg')],title="Select Save Location",defaultextension='.png')
    if file:
        save_path =os.path.abspath(file.name)
        qr=qrcode.make(qr_hide.get())
        qr.save(save_path)
        messagebox.showinfo('success!',f'Successfully saved image at: {save_path}')

label=Label(root,text="Professional QR Code Generator",font=("calibri",13),bg="#000",fg="#fff")
label.pack(fill=X)

label3=Label(root,text="Enter QR-Code hidden text or URL:",font=("Tajawal",13))
label3.place(x=50,y=130)
qr_hide = Entry(root, justify="center",relief="solid",width=31)
qr_hide.place(x=80,y=170)

save_btn=Button(root,text="save QR-Code",font=('consolas',16),width=20,relief="solid",bd=0,bg="#4cd038",fg="#fff",activebackground="#004700",activeforeground="#fff",cursor="hand2",command=save_qr)
save_btn.place(x=50,y=400)

root.mainloop()
