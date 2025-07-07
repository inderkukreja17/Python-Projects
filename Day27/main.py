from tkinter import *

from click import command
def button_click():
    print("I got clicked")
    new_input=input.get()
    my_label.config(text=new_input)

window=Tk()
window.title("My first GUI program")
window.minsize(width=500,height=300)
window.config(padx=100,pady=300)


#Label
my_label=Label(text="I am a label",font=("Arial",24,"bold"))
my_label.config(text="New text")
my_label.grid(column=0,row=0)


#Buttons
button=Button(text="Click me",command=button_click)
button.grid(column=1,row=1)

button_2=Button(text="Click me")
button_2.grid(column=2,row=0)

#
#Entry
input=Entry(width=10)
input.grid(column=3,row=2)












window.mainloop()