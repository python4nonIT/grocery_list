import tkinter
from tkinter import *
from PIL import Image, ImageTk

top = tkinter.Tk() #initialize window manager
top.geometry("600x500")
top.title("Welcome to my shoppinglist")
top.configure(bg="#2E86C1")

my_image= ImageTk.PhotoImage(Image.open("cart.jpg"))
my_label= Label(image=my_image)
my_label.place (x=100, y=200)

shoplist = [] #current shopping list

def add():
    item= entry1.get()
    shoplist.append(item)
    print(item)

def view():
    txt.delete (0.0, 'end')
    print(shoplist)
    txt.insert(0.0, shoplist)

def remove():
    item= entry2.get()
    shoplist.remove(item)
    print(item)

def export():
    for listitem in shoplist:
        print(listitem)
    with open ("shopping.txt", "w") as output:
        output.write(str(shoplist))

def exit1():
    exit()

#button
B_add= tkinter.Button(top, text= "Add item", bg="brown", font=("arial",19,"bold"), command = add)
B_add.place (x=10, y=20)
B_remove= tkinter.Button(top, text= "Remove item", bg="brown", font=("arial",19,"bold"), command = remove)
B_remove.place (x=10, y=60)
B_view= tkinter.Button(top, text= "View list", bg="brown", font=("arial",19,"bold"), command = view)
B_view.place (x=10, y=100)
B_export= tkinter.Button(top, text= "Export to notepad", bg="brown",font=("arial",19,"bold"), command = export)
B_export.place (x=10, y=140)
B_exit= tkinter.Button(top, text= "Exit", bg="brown", font=("arial",19,"bold"), command = exit1)
B_exit.place (x=10, y=180)

#show output list


#L1 = Label(top, text= "Type item")
#L1.place(x=10, y=20)
#L2 = Label (top, text= "Remove item")
#L2.place(x=10, y=60)
entry1 = Entry(top, bd=5) #bd=border
entry1.place(x=160, y=20)
entry2 = Entry(top, bd=5)
entry2.place(x=160, y=60)

txt=Text(top, width=30, height=8, wrap=WORD)
txt.place(x=300, y=200)

top.mainloop()
