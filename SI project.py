from tkinter import *
 
from functools import partial
 
top=Tk()
 
top.title("SIMPLE INTEREST CALCULATER")
 
top.geometry("800x800")
top.config(bg="#00ffff")
 
def cal_si(P,R,T,ANS):
 
    P = int(num1.get())
 
    R = float(num2.get())
 
    T = int(num3.get())
 
    SI = P*R*T/100
 
    ANS.config(text=" Simple Interest = RS. %d"%SI)
 
ANS=Label(top, fg="red",bg='#00ffff',font="Arial 20")
 
ANS.place(x=50 , y=300)
 
num1 = StringVar()
 
num2 = StringVar()
 
num3 = StringVar()
 
l4=Label(top,text="SIMPLE INTEREST CALCULATER",font="lucida 9 bold",pady=12,fg="black",bg="white").pack()

L1= Label(top, text="PRINCIPAL = ",fg = "green" , bg = "yellow").place(x=50, y=70)
 
E1=Entry(top, textvariable=num1 ,fg= 'black',bg= 'orange').place(x=250, y=70)
 

L2= Label(top, text="RATE % = ", fg = "green" , bg = "yellow").place(x=50, y=120)
 
E2=Entry(top, textvariable=num2).place(x=250, y=120)
 
 
L3= Label(top, text="TIME = ", fg = "green" , bg = "yellow").place(x=50, y=170)
 
E3=Entry(top, textvariable=num3,bg='green',fg= 'white').place(x=250, y=170)
 
cal_si= partial(cal_si , 'P','R','T',ANS)
 
B1= Button(top, text="CALCULATE" ,bg="#ff4d94",fg="white",activeforeground="#ff4d94",activebackground="white",font = 'Arial 9 bold ' ,command=cal_si).place(x=50, y=230 )
 
top.mainloop()
