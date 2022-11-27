from tkinter import *
from PIL import Image
import qrcode


root = Tk()
root.title("QR code generator")
root.geometry("800x600+600+200")
root.config(bg="#FAFAEB")

icon = PhotoImage(file="icon.png")
root.iconphoto(False, icon)


def generate():
    global name
    name = titletext.get()
    if len(name) >= 1:
        link = url.get()
        qr = qrcode.make(link)
        qr.save("qrcode/" + name + "qr.png")

        img = Image.open("qrcode/" + name + "qr.png")
        new_width = 350
        new_height = 350
        img = img.resize((new_width, new_height), Image.ANTIALIAS)
        img.save("qrcode/" + name + ".png")

        global output
        output = PhotoImage(file="qrcode/" + name + ".png")
        output_view.config(image=output)
        output_title = Label(root, text=name + " QR code has been generated", font="Arial 14 italic", bg="#FAFAEB")
        output_title.place(x=50, y=60)
    else:
        error = Label(root, text="Please provide a title", font="Arial 14", bg="#FAFAEB")
        error.place(x=50, y=100)


output_view = Label(root, height=400, width=400, bg="#FAFAEB")
output_view.pack(side=RIGHT)

msg = Label(root, text="Generate your own QR code", font="Arial 14 bold", bg="#FAFAEB")
msg.place(x=250, y=10)

title = Label(root, text="Title", bg="#FAFAEB", font="Arial 14")
title.place(x=50, y=170)

titletext = Entry(root, width=20, font="Arial 14")
titletext.place(x=50, y=200)

urltext = Label(root, text="Qr text", bg="#FAFAEB", font="Arial 14")
urltext.place(x=50, y=260)

url = Entry(root, width=28, font="Arial 14")
url.place(x=50, y=290)

button = Button(root, text="Generate QR code", font="Arial 14", width=20, bg="light green", height=5, command=generate).place(x=50, y=350)

root.mainloop()
