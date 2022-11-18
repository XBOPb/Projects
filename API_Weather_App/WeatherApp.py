import tkinter
from tkinter import *
from tkinter import ttk
from weatherAPI import getweather


def update():
    city = search_city.get()
    weatherlabel.configure(text=getweather(city))


root = Tk()
result = ttk.Treeview
root.title("Weather")
root.geometry("500x500")
root.config(bg="#87CEFA")
icon = tkinter.PhotoImage(file="icon.png")
root.iconphoto(False, icon)
searchbutton = PhotoImage(file="smol.png")
searchbutton = searchbutton.subsample(1, 1)


label = Label(root,
              text="Get weather for your city\n",
              fg="white",
              font='Comfortaa 18 bold',
              bg="#87CEFA")
label.pack(pady=40)
search_city = Entry(root, width=30, font='Helvetica 10')
search_city.pack()
button = Button(root,
                image=searchbutton,
                text="Find a city",
                font=10,
                command=update)
button.pack(pady=40)
weatherlabel = Label(root,
                     text="",
                     width=400,
                     height=20,
                     bg="#87CEFA",
                     font='Comfortaa 15 bold',
                     fg="white")
weatherlabel.pack()


root.mainloop()
