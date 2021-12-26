from tkinter import *
from tkinter import ttk
converter = Tk()
converter.geometry("600x400")
converter.title("Currency Converter")
converter.wm_iconbitmap("math.ico")

OPTIONS = {
    "Australian Dollar": 0.0193,
    "Brazilian Real": 0.0193,
    "British Pound": 0.0107,
    "Chinese Yuan:": 0.0945,
    "Euro": 0.0119,
    "Honk Kong Dollar": 0.1037,
    "Indonesian Rupiah": 193.8986,
    "Japanese Yen": 1.44,
    "Pakistani Rupee": 2.2422,
    "SriLankan Rupee": 2.4896,
    "Swiss Franc": 0.0127,
    "US Dollar": 0.0134
           }
def ok():
    price = rupees.get()
    answer = variable.get()
    DICT = OPTIONS.get(answer,None)
    converted = float(DICT)*float(price)
    result.delete(1.0,END)
    result.insert(INSERT,"Price In ",INSERT,answer,INSERT," = ",
                  INSERT,converted)

appName = Label(converter, text="Currency",
                font=("arial", 25, "bold", "underline"), fg="dark blue")
appName.grid(row=0, column=0, padx=10)
photo = PhotoImage(file="cc5.png")
logo = Label(converter,image=photo)
logo.grid(row=0,column=1)
appName = Label(converter, text="Converter",
                font=("arial", 25, "bold", "underline"), fg="dark blue")
appName.grid(row=0, column=2, ipadx=10)

result= Text(converter,height=5,width=50,font=("arial",10,"bold"),bd=5)
result.grid(row=1,columnspan=10,padx=3)

india = Label(converter,text="Indian Rupees:",
              font=("arial",15,"bold"),fg="red")
india.grid(row=2,column=0)
rupees = Entry(converter,font=("calibri",20))
rupees.grid(row=2,column=1)
choice = Label(converter,text="choose country:",
               font=("arial",10,"bold"),fg="red")
choice.grid(row=3, column=0)
variable = StringVar(converter)
variable.set(None)
option = OptionMenu(converter, variable, *OPTIONS)
option.grid(row=3, column=1, sticky="ew")
button = Button(converter, text="Convert", fg="green",
                font=("calibri", 20), bg="powder blue",command=ok)
button.grid(row=3, column=2)
mainloop()
