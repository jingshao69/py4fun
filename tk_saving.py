#!/usr/bin/python3

import locale
import os.path
import configparser
import tkinter.messagebox
from tkinter import *


# The title of the program
PROG_TITLE="Saving Calculator"

# The name of the config file
CONFIG_FILE=".tk_saving.ini"

# Help String
PROG_HELP="Saving Calculator in Python"

#Fields
fields = ('Initial Balance', 'Monthly Saving', 'Annual Rate', 'Number of Month', 'Total Saving')

field_values = {}
UI_Entries={}


def total_saving(*args):
   # period rate:
   r = (float(UI_Entries['Annual Rate'].get()) / 100) / 12
   #print("r", r)
   # principal loan:
   initial_balance= locale.atof(UI_Entries['Initial Balance'].get().strip(MONEY_SYM))
   initial_balance_str =  locale.currency(initial_balance, grouping=True)

   UI_Entries['Initial Balance'].delete(0, END)
   UI_Entries['Initial Balance'].insert(0, initial_balance_str)

   saving = locale.atof(UI_Entries['Monthly Saving'].get().strip(MONEY_SYM))

   saving_str = locale.currency(saving, grouping=True)

   UI_Entries['Monthly Saving'].delete(0, END)
   UI_Entries['Monthly Saving'].insert(0, saving_str)

   n =  float(UI_Entries['Number of Month'].get())

   if r != 0:
      q = (1 +r) ** n;
      total_saving = saving *(q - 1)/r + initial_balance * q;
   else:
      total_saving = initial_balance + saving * n

   total_saving_str = locale.currency(total_saving, grouping=True)

   UI_Entries['Total Saving'].delete(0,END)
   UI_Entries['Total Saving'].insert(0, total_saving_str )


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
      ent.bind("<FocusOut>", total_saving)


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

   b2 = Button(root, text='Total Saving', command=total_saving)
   b2.pack(side=RIGHT, padx=5, pady=5)

   b1 = Button(root, text='About', command=about)
   b1.pack(side=RIGHT, padx=5, pady=5)

   root.mainloop()

