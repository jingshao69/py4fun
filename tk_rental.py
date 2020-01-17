#!/usr/bin/python3

import locale
import os.path
import configparser
import tkinter.messagebox
from tkinter import *


# The title of the program
PROG_TITLE="Rental Return Calculator"

# The name of the config file
CONFIG_FILE=".tk_rental.ini"

# Help String
PROG_HELP="Rental Calculator in Python"

NUM_YEAR_DEPRECIATION=27.5

#Fields
fields = ('House Value', 'Mortgage Rate', 'Number of Payments', 'Tax Rate', 'Down Payment', 'Property Tax','Home Owner Ins',  'Maintenance', 'Monthly Rent', 'Return Rate')

field_values = {}
UI_Entries={}


def return_rate(*args):
    # period rate:
    r = (float(UI_Entries['Mortgage Rate'].get()) / 100) / 12
    #print("r", r)
    # principal loan:
    houseVal= locale.atof(UI_Entries['House Value'].get().strip(MONEY_SYM))
    downPayment = locale.atof(UI_Entries['Down Payment'].get().strip(MONEY_SYM))
    taxRate= locale.atof(UI_Entries['Tax Rate'].get())
    loanValue = houseVal - downPayment
    #print("loanValue", loanValue)

    propTax = locale.atof(UI_Entries['Property Tax'].get().strip(MONEY_SYM))
    homeIns = locale.atof(UI_Entries['Home Owner Ins'].get().strip(MONEY_SYM))
    maintenance= locale.atof(UI_Entries['Maintenance'].get().strip(MONEY_SYM))
    monthlyRent = locale.atof(UI_Entries['Monthly Rent'].get().strip(MONEY_SYM))
    #loan_str = locale.currency(loan, grouping=True)

    #UI_Entries['Loan Principle'].delete(0, END)
    #UI_Entries['Loan Principle'].insert(0, loan_str)

    n =  float(UI_Entries['Number of Payments'].get())

    if r != 0 and loanValue !=0 and n != 0:
        q = (1 + r)** n
        monthly = r * ( (q * loanValue ) / ( q - 1 ))
        principal = monthly - loanValue *r
        #print("Monthly", monthly)
        #print("Principal", principal)
        piti = monthly + (propTax + homeIns)/12
        monthlyCost = piti - principal
        #print("piti", piti)
        if (monthlyRent > piti) and  (downPayment > 0):
            grossProfit = (monthlyRent - monthlyCost) *12 - maintenance; 
            depreciation = houseVal / NUM_YEAR_DEPRECIATION
            taxLoss = depreciation - grossProfit
            taxSaving = taxLoss * taxRate/100.0
            #print("taxLoss", taxLoss)
            #print("taxSaving", taxSaving)
            grossReturn = (grossProfit  + taxSaving)/ downPayment * 100.0
            #print("Gross Return", grossReturn);
            UI_Entries['Return Rate'].delete(0,END)
            UI_Entries['Return Rate'].insert(0, "{0:.1f}%".format(grossReturn))


def about(*args):
   tkinter.messagebox.showinfo("About", PROG_HELP)


def load_config():
   global field_values

   for field in fields:
      field_values[field] = "0"

   if os.path.isfile(CONFIG_FILE):
      config = configparser.RawConfigParser()
      config.read(CONFIG_FILE)
      for field in fields:
         field_values[field] = config.get('Rental', field)

def save_config():
   config = configparser.RawConfigParser()

   config.add_section('Rental')
   for field in fields:
      value = UI_Entries[field].get()
      config.set('Rental', field, value)
   with open(CONFIG_FILE, 'w') as configFile:
      config.write(configFile)

def quit_form(*args):
   save_config()
   root.quit()
   

def makeform(root, fields):
   global UI_Entries
   for field in fields:
      row = Frame(root)
      lab = Label(row, width=22, text=field+": ", anchor='w')
      ent = Entry(row)
      ent.insert(0,field_values[field])
      row.pack(side=TOP, fill=X, padx=5, pady=5)
      lab.pack(side=LEFT)
      ent.pack(side=RIGHT, expand=YES, fill=X)
      UI_Entries[field] = ent

def add_callback():
   for field in fields:
      #print field
      ent = UI_Entries[field]
      ent.bind("<FocusOut>", return_rate)


if __name__ == '__main__':

   locale.setlocale(locale.LC_ALL,'')
   locale_mon = locale.localeconv()
   MONEY_SYM = locale_mon['currency_symbol']

   load_config();

   root = Tk()
   root.wm_title(PROG_TITLE)
   makeform(root, fields)

   add_callback()

   #root.bind('', (lambda event, e=ents: fetch(e)))   
   b3 = Button(root, text='Quit', command=quit_form)
   b3.pack(side=RIGHT, padx=5, pady=5)

   b2 = Button(root, text='Rental Return', command=return_rate)
   b2.pack(side=RIGHT, padx=5, pady=5)

   b1 = Button(root, text='About', command=about)
   b1.pack(side=RIGHT, padx=5, pady=5)

   root.mainloop()

