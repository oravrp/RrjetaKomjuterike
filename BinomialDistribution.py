from sympy import *
import matplotlib
import tkinter
from tkinter import *
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')
from numpy import random
from scipy.stats import binom 
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.animation as animation



root=Tk()
frame=Frame(root)
frame.pack()

#-----------------------------Labels and Entries-----------------------------------

label1=Label(frame,text="n =")
label1.grid(row=1,column=1)

text1=Entry(frame,width=10)
text1.grid(row=1,column=2)

label2=Label(frame,text="x =")
label2.grid(row=2,column=1)

text2=Entry(frame,width=10)
text2.grid(row=2,column=2)

label3=Label(frame,text="p =")
label3.grid(row=1,column=4)

text3=Entry(frame,width=10)
text3.grid(row=1,column=5)

#-----------------------Dropdown Menu----------------------------------------------

options=StringVar(root)
choices={'P(X>=x)= ','P(X<=x)= ','P(X=x)= '}
options.set('P(X=x)= ')

menu=OptionMenu(frame,options,*choices)
menu.grid(row=2,column=4)

show=StringVar()
text4=Entry(frame,width=10,textvariable=show)
text4.grid(row=2,column=5)

#--------------------------Canavas--------------------------------------------------

button1=Button(frame,text="Go",command=lambda:tempCanvas())
button1.grid(row=3,column=3)

#--------------------------Functions-----------------------------------------------

def tempCanvas():
    canvas_width=300
    canvas_height=80
    temp=Canvas(frame,width=canvas_width,height=canvas_height)
    temp.config(background="white")
    temp.grid(row=3,column=1,columnspan=5)
    
#--------------------------Assure that n is a positive integer---------------------

    if text1.get().isdigit():
        global n
        n=int(text1.get())
    else:
        temp.create_text(150,20,text="The number of experiments is not valid!")
        temp.create_text(150,30,text="Please enter a positive integer!")
#----------------------------------------------------------------------------------
    if text2.get().isdigit():
        global x
        x=int(text2.get())
    else:
        temp.create_text(150,40,text="X is not valid!")
        temp.create_text(150,50,text="Please enter a positive integer!")
#------------------------------------------------------------------------------------
    try:
        global p
        p=float(text3.get())
        if p<0 or p>1:
            temp.create_text(150,50,text="Please enter a number between 0 and 1")
            exit()
        else:
            p=float(text3.get())
    except ValueError:
        temp.create_text(150,60,text="The probability is not valid!")
        temp.create_text(150,70,text="Please enter a number between 0 and 1")
    

#----------------------------------Value of Probability-------------------------------  

def Result(*args):
    h=tempCanvas()
    l=Paint()
    
    probability=options.get()
    if probability=='P(X>=x)= ':
        value=0
        for i in range(x,n+1):
            value=value+binomial(n,i)*(p**i)*((1-p)**(n-i))
    elif probability=='P(X<=x)= ':
        value=0
        for i in range(0,x+1):
            value=value+binomial(n,i)*(p**i)*((1-p)**(n-i))
    else:
        value=binomial(n,x)*(p**x)*((1-p)**(n-x))
        
    show.set(round(value,5))
            
            
def Paint():
    t=[]
    w=Figure(figsize=(5,5),dpi=100)
    a=w.add_subplot(111)
    a.set_ylabel('P(X)')
    a.set_xlabel('Number of trials')
    y=np.arange(n+1)
    for i in y:
        t.append(binomial(n,i)*(p**i)*((1-p)**(n-i)))
        
    barlist=a.bar(y[:],t[:])
    if options.get()=='P(X>=x)= ':
        for i in range(x,n+1):
            barlist[i].set_color('r')
    elif options.get()=='P(X<=x)= ':
        for i in range(0,x+1): 
            barlist[i].set_color('r')
    else:
        barlist[i].set_color('r')
        
    canvas=FigureCanvasTkAgg(w,frame)
    canvas.draw() 
    canvas.get_tk_widget().grid(row=3,column=1,columnspan=5)
    
    
options.trace('w',Result)
root.mainloop()