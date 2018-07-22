from tkinter import *
import tkinter as tk
import tkinter.messagebox
import tkinter.ttk






top = tkinter.Tk()
top.title("Freefall Test Bot")
top.configure(background="white")
top.geometry("310x300")

menubar=Menu(top)

#FileMenu
filemenu=Menu(menubar,tearoff=0)
filemenu.add_command(label="Save Settings")
filemenu.add_separator()
filemenu.add_command(label="Exit")
menubar.add_cascade(label="File", menu=filemenu)

#BrowserOpen
browsermenu = Menu(menubar, tearoff=0)
##radio = StringVar()
##menu_file.add_radiobutton(label='One', variable=radio, value=1)
radio1 = StringVar()
browsermenu.add_radiobutton(label='DISABLE', variable=radio1, value=1)
browsermenu.add_radiobutton(label='DuckDuckGo', variable=radio1, value=2)
browsermenu.add_radiobutton(label='Bing', variable=radio1, value=3)
browsermenu.add_separator()
browsermenu.add_radiobutton(label='Google', variable=radio1, value=4)
menubar.add_cascade(label="BrowserOpen", menu=browsermenu)


#LangMenu
langmenu = Menu(menubar, tearoff=0)
##radio = StringVar()
##menu_file.add_radiobutton(label='One', variable=radio, value=1)
radio = StringVar()
langmenu.add_radiobutton(label='French', variable=radio, value=1)
langmenu.add_radiobutton(label='German', variable=radio, value=2)
langmenu.add_separator()
langmenu.add_radiobutton(label='English', variable=radio, value=3)
menubar.add_cascade(label="OCR Language", menu=langmenu)

#HElpMenu
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About")
filemenu.add_separator()
helpmenu.add_command(label="Version=8.8.8.8")
menubar.add_cascade(label="Help", menu=helpmenu)

# display the menu
top.config(menu=menubar)




L_Question = Label(top, text="Question",relief="solid",padx=80).grid(row=0,columnspan=4)
L_Guess=Label(top,text="Guess",padx=10).grid(row=0,column=4)

L_Control = Label(top, text="Control",).grid(row=0,column=5)

##Question = Entry(top, bd =3,width=30)
##Question.grid(rowspan=2,column=0)

Question = tkinter.Text(top, height=4, width=30,wrap=WORD,relief="solid",font=("Arial",10))
Question.insert(INSERT, 'Waiting for Scan\n\nHope you win today')
Question.grid(row=1,rowspan=2,column=0,pady=(10, 0),columnspan=4)


##Guess = Entry(top, bd =3,width=8)
##Guess.grid(rowspan=2,column=4)
Guess = tkinter.Text(top, height=2, width=3,font=("Arial",20),relief="solid",fg="Red")
Guess.insert(INSERT, '  0')
Guess.grid(row=1,rowspan=2,column=4,pady=(10, 0))

B_Scan=Button(top, text ="Scan",padx=5).grid(row=1,column=5,pady=(10, 0))
B_Reset=Button(top, text ="Reset",padx=4).grid(row=2,column=5)


Option1=tkinter.Text(top, height=4,width=12,relief="solid")
Option1.insert(INSERT, '------')
Option1.grid(row=3,column=0,columnspan=2,rowspan=2,pady=(20,0))

##o11
o11=tkinter.Text(top, height=2,width=12,relief="solid")
o11.insert(INSERT, '------')
o11.grid(row=5,column=0,columnspan=2)

##o12
o12=tkinter.Text(top, height=2,width=12,relief="solid")
o12.insert(INSERT, '------')
o12.grid(row=6,column=0,columnspan=2)

##o13
o13=tkinter.Text(top, height=2,width=12,relief="solid")
o13.insert(INSERT, '------')
o13.grid(row=7,column=0,columnspan=2)


#Option2
Option2=tkinter.Text(top, height=4,width=12,relief="solid")
Option2.insert(INSERT, '------')
Option2.grid(row=3,column=2,columnspan=2,pady=(20,0))

##o21
o21=tkinter.Text(top, height=2,width=12,relief="solid")
o21.insert(INSERT, '------')
o21.grid(row=5,column=2,columnspan=2)

##o22
o22=tkinter.Text(top, height=2,width=12,relief="solid")
o22.insert(INSERT, '------')
o22.grid(row=6,column=2,columnspan=2)

##o23
o23=tkinter.Text(top, height=2,width=12,relief="solid")
o23.insert(INSERT, '------')
o23.grid(row=7,column=2,columnspan=2)

#Option3
Option3=tkinter.Text(top, height=4,width=12,relief="solid")
Option3.insert(INSERT, '------')
Option3.grid(row=3,column=4,columnspan=2,pady=(20,0))

##o31
o31=tkinter.Text(top, height=2,width=12,relief="solid")
o31.insert(INSERT, '------')
o31.grid(row=5,column=4,columnspan=2)

##o32
o32=tkinter.Text(top, height=2,width=12,relief="solid")
o32.insert(INSERT, '------')
o32.grid(row=6,column=4,columnspan=2)

##o33
o33=tkinter.Text(top, height=2,width=12,relief="solid")
o33.insert(INSERT, '------')
o33.grid(row=7,column=4,columnspan=2)



top.mainloop()













