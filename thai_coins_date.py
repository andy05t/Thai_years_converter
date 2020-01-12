from tkinter import *

root = Tk()

year = []

top_frame = Frame(root)
top_frame.pack()
bottom_frame = Frame(root)
bottom_frame.pack(side = BOTTOM)

def converter0():
    year.append("0")
    full_convert(year)
def converter1():
    year.append("1")
    full_convert(year)
def converter2():
    year.append("2")
    full_convert(year)
def converter3():
    year.append("3")
    full_convert(year)
def converter4():
    year.append("4")
    full_convert(year)
def converter5():
    year.append("5")
    full_convert(year)
def converter6():
    year.append("6")
    full_convert(year)
def converter7():
    year.append("7")
    full_convert(year)
def converter8():
    year.append("8")
    full_convert(year)
def converter9():
    year.append("9")
    full_convert(year)


def full_convert(year):
    print(year)
    if year:
        yr = int(''.join(year))- 543
    v.set("The actual year is {}".format(yr))
       

def clearfunc():
    year.clear()     
    v.set("The actual year is not defined yet")   


photo0 = PhotoImage(file = "0.png")
photo1 = PhotoImage(file = "1.png")
photo2 = PhotoImage(file = "2.png")
photo3 = PhotoImage(file = "3.png")
photo4 = PhotoImage(file = "4.png")
photo5 = PhotoImage(file = "5.png")
photo6 = PhotoImage(file = "6.png")
photo7 = PhotoImage(file = "7.png")
photo8 = PhotoImage(file = "8.png")
photo9 = PhotoImage(file = "9.png")


button1 = Button(top_frame,image = photo0, command = converter0)
button2 = Button(top_frame,image = photo1, command = converter1)
button3 = Button(top_frame,image = photo2, command = converter2)
button4 = Button(top_frame,image = photo3, command = converter3)
button5 = Button(top_frame,image = photo4, command = converter4)
button6 = Button(top_frame,image = photo5, command = converter5)
button7 = Button(top_frame,image = photo6, command = converter6)
button8 = Button(top_frame,image = photo7, command = converter7)
button9 = Button(top_frame,image = photo8, command = converter8)
button10 = Button(top_frame,image = photo9, command = converter9)

clear = Button(bottom_frame, text = "Clear", command = clearfunc).pack()

v = StringVar()
lab = Label(bottom_frame, textvariable = v).pack()
button1.pack(side = LEFT, padx = 2, pady = 2)
button2.pack(side = LEFT, padx = 2, pady = 2)
button3.pack(side = LEFT, padx = 2, pady = 2)
button4.pack(side = LEFT, padx = 2, pady = 2)
button5.pack(side = LEFT, padx = 2, pady = 2)
button6.pack(side = LEFT, padx = 2, pady = 2)
button7.pack(side = LEFT, padx = 2, pady = 2)
button8.pack(side = LEFT, padx = 2, pady = 2)
button9.pack(side = LEFT, padx = 2, pady = 2)
button10.pack(side = LEFT, padx = 2, pady = 2)


a_Label = Label(top_frame, text = "Converting the year on Thai coins: \n Please type in the characters on the coin", fg = "red")  
a_Label.pack(side = TOP)



root.mainloop()  