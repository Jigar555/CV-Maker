#CV Maker Project

import tkinter as tk
from tkinter import messagebox

def show_entry_fields():
    print("First Name: %s\n Last Name %s" %(e1.get(), e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),e7.get(),e8.get(),e9.get(),e10.get()))
def save_and_print():
   messagebox.showinfo("File Save", "Your CV has been Saved")
   print("First Name: %s\n Last Name: %s\n Email: %s\n Age: %d " %(e1.get(), e2.get(),e3.get(),int(e4.get())))
     

window=tk.Tk()
window.title("CV Maker")


label1 = tk.Label(window,text="First Name/Last Name").place(x=10,y=1)
label2 = tk.Label(window,text="Email").place(x=10,y=21)
label3 = tk.Label(window,text="Age").place(x=10,y=40)
label4 = tk.Label(window,text="Objective",bg="black",fg="red",width=84,height=2,font=8).place(x=10,y=60)
label5 = tk.Label(window,text="Acedimca",bg="black",fg="red",width=84,height=2,font=8).place(x=10,y=147)
#table
label6 = tk.Label(window,text="Qualifaction",bg="yellow",fg="red",width=20,height=2).place(x=10,y=191)
label7 = tk.Label(window,text="Board/University",bg="yellow",fg="red",width=20,height=2).place(x=162,y=191)
label8 = tk.Label(window,text="Subjects",bg="yellow",fg="red",width=20,height=2).place(x=314,y=191)
label9 = tk.Label(window,text="Passing Year",bg="yellow",fg="red",width=20,height=2).place(x=467,y=191)
label10 = tk.Label(window,text="Marks",bg="yellow",fg="red",width=20,height=2).place(x=620,y=191)
label11 = tk.Label(window,text="Graduation",bg="yellow",fg="red",width=20).place(x=10,y=230)
label11 = tk.Label(window,text="XII",bg="yellow",fg="red",width=20).place(x=10,y=255)
label12 = tk.Label(window,text="X",bg="yellow",fg="red",width=20).place(x=10,y=280)

label13 = tk.Label(window,text="Project Undertaken",bg="black",fg="red",width=84,height=2,font=8).place(x=10,y=303)

label14 = tk.Label(window,text="Skills",bg="black",fg="red",width=84,height=2,font=8).place(x=10,y=373)

label15 = tk.Label(window,text="Honour & Achievements",bg="black",fg="red",width=84,height=2,font=8).place(x=10,y=444)

e1=tk.Entry(window)             #firstname
e2=tk.Entry(window)             #lastname
e3=tk.Entry(window,width=42)    #email
e4=tk.Entry(window,width=42)    #age
e5=tk.Entry(window,width=126)   #objective1
e6=tk.Entry(window,width=126)   #objective2

#table
e7=tk.Entry(window,width=24)
e8=tk.Entry(window,width=24)
e9=tk.Entry(window,width=24)
e10=tk.Entry(window,width=24)

e11=tk.Entry(window,width=24)
e12=tk.Entry(window,width=24)
e13=tk.Entry(window,width=24)
e14=tk.Entry(window,width=24)

e15=tk.Entry(window,width=24)
e16=tk.Entry(window,width=24)
e17=tk.Entry(window,width=24)
e18=tk.Entry(window,width=24)

#project
e19=tk.Entry(window,width=126)
#skills
e20=tk.Entry(window,width=126)
#Honour
e21=tk.Entry(window,width=126)
e22=tk.Entry(window,width=126)


e1.place(x=150,y=1)     #firstname
e2.place(x=280,y=1)     #lastname
e3.place(x=150,y=21)    #email
e4.place(x=150,y=40)    #age
e5.place(x=10,y=104)    #objective1 
e6.place(x=10,y=125)    #objective2

#table
e7.place(x=162,y=230)
e8.place(x=314,y=230)
e9.place(x=467,y=230)
e10.place(x=620,y=230)

e11.place(x=162,y=255)
e12.place(x=314,y=255)
e13.place(x=467,y=255)
e14.place(x=620,y=255)

e15.place(x=162,y=280)
e16.place(x=314,y=280)
e17.place(x=467,y=280)
e18.place(x=620,y=280)

#project
e19.place(x=10,y=350)
#skills
e20.place(x=10,y=420)
#honour
e21.place(x=10,y=490)
e22.place(x=10,y=512)



button1 = tk.Button(window,text='Save',command=save_and_print,fg='white', bg='green',width=15)
button1.place(x=340,y=535)



window.mainloop()



