from tkinter import *


def cel_na_fahr(event):
    print(ent1.get())
    e = ".0"
    a = float(ent1.get())
    a = round((32 + 9 / 5 * a), 2)
    a = str(a)

    if a.endswith(e):
        a = a.replace(".0", "")
        ent2.delete(0, END)
        ent2.insert(0, a)
    else:
        ent2.delete(0, END)
        ent2.insert(0, a)


def fahr_na_cel(event):
    print(ent2.get())
    e = ".0"
    a = float(ent2.get())
    a = round(5 / 9 * (a - 32), 2)
    a = str(a)

    if a.endswith(e):
        a = a.replace(".0", "")
        ent1.delete(0, END)
        ent1.insert(0, a)
    else:
        ent1.delete(0, END)
        ent1.insert(0, a)


root = Tk()

root.geometry("300x180+400+400")

fr1 = Frame(root, padx=5, pady=40)
fr1.pack(side=TOP)

fr2 = Frame(root)
fr2.pack(side=TOP)

lbl1 = Label(fr1, text="cel to fahr   ")
lbl1.pack(side=LEFT)

ent1 = Entry(fr1)
ent1.pack(side=RIGHT)

lbl2 = Label(fr2, text="fahr to cel   ")
lbl2.pack(side=LEFT)

ent2 = Entry(fr2)
ent2.pack(side=RIGHT)

ent1.bind('<KeyRelease>', cel_na_fahr)
ent2.bind('<KeyRelease>', fahr_na_cel)

root.mainloop()
