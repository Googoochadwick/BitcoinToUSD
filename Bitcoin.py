from tkinter import *
import requests
import json
import sys
from forex_python.converter import CurrencyRates
window = Tk()

try:
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    response = r.json()
    rate = response['bpi']['USD']['rate_float']

    

    
except requests.RequestException:
    sys.exit('error')

def from_bit():
    dollar = float(e2_value.get())*float(rate)
    t1.delete("1.0",END)
    t1.insert(END, dollar)

e1 = Label(window, text="Input the amount of bitcoins",bg='black', fg='white')
e2_value = StringVar()
e2 = Entry(window, textvariable=e2_value)
e3 = Label(window, text="Dollar",bg='black', fg='white')
window.configure(background='black')
t1 = Text(window, height=1, width=30,bg='black', fg='white')

b1 = Button(window, text="Convert", command=from_bit,height=2, width=30,bg='green' )

e1.grid(row=0, column=0)
e2.grid(row=0, column=1)
e3.grid(row=1, column=0)

t1.grid(row=2, column=0)

b1.grid(row=2, column=1)

window.mainloop()









