#!/usr/bin/env python3

import locale
import os.path
import configparser
import tkinter.messagebox
from tkinter import *


# The title of the program
PROG_TITLE="Loan Calculator"

# The name of the config file
CONFIG_FILE=".tk_loan.ini"

# Help String
PROG_HELP="Mortgage Calculator in Python"

#Fields
fields = ('Loan Principle', 'Annual Rate', 'Number of Payments', 'Monthly Payment')

field_values = {}
UI_Entries={}


def monthly_payment(*args):
   # period rate:
   r = (float(UI_Entries['Annual Rate'].get()) / 100) / 12
   #print("r", r)
   # principal loan:
   loan = locale.atof(UI_Entries['Loan Principle'].get().strip(MONEY_SYM))

   loan_str = locale.currency(loan, grouping=True)

   UI_Entries['Loan Principle'].delete(0, END)
   UI_Entries['Loan Principle'].insert(0, loan_str)

   n =  float(UI_Entries['Number of Payments'].get())

   if r != 0 and loan !=0 and n != 0:
     q = (1 + r)** n
     monthly = r * ( (q * loan ) / ( q - 1 ))
     monthly_str = locale.currency(monthly, grouping=True)

     UI_Entries['Monthly Payment'].delete(0,END)
     UI_Entries['Monthly Payment'].insert(0, monthly_str )

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
         field_values[field] = config.get('Loan', field)

def save_config():
   config = configparser.RawConfigParser()

   config.add_section('Loan')
   for field in fields:
      value = UI_Entries[field].get()
      config.set('Loan', field, value)
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
      ent.bind("<FocusOut>", monthly_payment)


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

   b2 = Button(root, text='Monthly Payment', command=monthly_payment)
   b2.pack(side=RIGHT, padx=5, pady=5)

   b1 = Button(root, text='About', command=about)
   b1.pack(side=RIGHT, padx=5, pady=5)

   root.mainloop()

