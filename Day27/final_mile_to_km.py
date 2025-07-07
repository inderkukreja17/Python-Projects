from tkinter import *


def button_click():
    print("I got clicked")
    cal=input.get()
    in_km=float(cal)*1.609
    calculate_label.config(text=in_km)


window=Tk()
window.title("Mile to Km converter")
window.minsize(width=500,height=300)

empty_label=Label(text="                    ",font=("Arial",24))
empty_label.grid(column=0,row=0)


miles_label=Label(text="Miles",font=("Arial",24))
miles_label.grid(column=2,row=0)

is_label=Label(text="is equal to",font=("Arial",24))
is_label.grid(column=0,row=1)

#
km_label=Label(text="Km",font=("Arial",24))
km_label.grid(column=2,row=1)


calculate_label=Label(text="0",font=("Arial",24))
calculate_label.grid(column=1,row=1)


button=Button(text="Calculate",command=button_click)
button.grid(column=1,row=2)




input=Entry(width=10)
input.grid(column=1,row=0)


















window.mainloop()
