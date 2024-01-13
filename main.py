from tkinter import *

windows = Tk()
windows.title("Mile to km Converter")
windows.minsize(width=20, height=50)
windows.config(padx=5, pady=5)

#label1
my_label1 = Label(text="Miles")
my_label1.grid(row=0, column=2)
#label2
my_label2 = Label(text="is equal to")
my_label2.grid(row=1, column=0)
#label3
my_label3 = Label(text="Km")
my_label3.grid(row=1, column=2)
#label4
my_label4 = Label(text="0")
my_label4.grid(row=1, column=1)


#Button:
def button_clicked():
    miles = float(input.get())
    km = miles * 1.60934
    my_label4.config(text=f"{km}")

button = Button(text="Calculate", command=button_clicked)
button.grid(row=2, column=1)

#Entry
input = Entry(width=10)
input.grid(row=0, column=1)
print(input.get())

windows.mainloop()