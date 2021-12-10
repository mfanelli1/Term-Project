from tkinter import *
import tkinter as tk
from tkinter import ttk
import requests
import ctypes


class CurrencyConverter():
    def __init__(self, url):
            self.data = requests.get(url).json()
            self.currencies = self.data["rates"]

    #cross multiplication between the amount and the conversion rates
    def convert(self, amount, currency1, currency2): 
        amount = amount / self.currencies[currency1] 
        result = amount * self.currencies[currency2]
        return result

class App(tk.Tk):
    def __init__(self, converter):
        tk.Tk.__init__(self)
        self.converter = converter
        self.winfo_toplevel().title("Currency Converter Project")

        self.geometry("1000x700")

        self.title = Label(self, text = 'Currency Convertor Machine', bg = "pink", pady = 10, padx = 10)
        self.title.config(font = ('Times New Roman',16,'bold'))
        self.subTitle = Label(self, text = f"Rates from {self.converter.data['date']}")
        
        #dropdown menus
        self.options1 = StringVar(self) #Currency we are converting FROM
        self.options2 = StringVar(self) #Currency we are converting TO
        self.dropdown1 = ttk.Combobox(self, textvariable = self.options1, 
        							  values = list(self.converter.currencies.keys()), 
        							  state = 'readonly', width = 15, justify = tk.CENTER)
        self.dropdown2 = ttk.Combobox(self, textvariable = self.options2, 
        							  values = list(self.converter.currencies.keys()), 
        							  state = 'readonly', width = 15, justify = tk.CENTER)

        #input and result boxes
        self.inputBox = Entry(self, justify = tk.CENTER, relief = FLAT, width = 16)
        self.resultBox = Label(self, justify = tk.CENTER, bg = 'white', width = 16) #not sure why input box and result box is not the same

        #convert button
        self.button = Button(self, text = "convert", fg = "pink", bg = "black", 
        					 activebackground = "yellow", relief = FLAT, 
        					 command = self.convert) 
        self.button.config(font=('Times New Roman', 12, 'italic'))

        #centering title and subTitle 
        self.title.place(relx = 0.5, rely = .2, y = -50, anchor = N)
        self.subTitle.place(relx = 0.5, rely= .2, anchor = N)

        #placement of these widgets are relative to the subTitle
        self.dropdown1.place(in_= self.subTitle, relx=0, x=-150, rely = 3.5)
        self.inputBox.place(in_= self.subTitle, relx=0, x=-150, rely = 5.5)
        self.dropdown2.place(in_= self.subTitle, relx=1, x=25, rely = 3.5)
        self.resultBox.place(in_= self.subTitle, relx=1, x=25, rely = 5.5)
        self.button.place(in_= self.subTitle, x= 23, y = 70)

    def convert(self):
        """Function sends an error when user does not enter number"""
        try:
            startCurr = self.options1.get()
            endCurr = self.options2.get()
            amount = float(self.inputBox.get())
        except ValueError:
            ctypes.windll.user32.MessageBoxW(0, "Enter a number", "An Error!", 0)
        else:
            try:
                result = round(self.converter.convert(amount, startCurr, endCurr), 2)
                self.resultBox.config(text = str(result))
            except KeyError:
                ctypes.windll.user32.MessageBoxW(0, "Choose a currency", "An Error!", 0)
    

if __name__ == '__main__':
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    App(CurrencyConverter(url))
    mainloop()

