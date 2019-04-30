#!/usr/bin/python

import math
import os.path
import tkMessageBox
from Tkinter import *


# The title of the program
PROG_TITLE="Binomial Distribution Calculator"

# Help String
PROG_HELP="Binomial Distribution Calculator in Python"

#Fields
fields = ('Number of Attempts', 'Number of Success', 'Probabilty of Success', 'Probability')

field_values = {}
UI_Entries={}

def factorial(n):
    result=1
    for i in range(1, n+1):
        result *= i
    return result

def binomial(n, k):
    return math.factorial(n) / (math.factorial(n-k) * math.factorial(k))

def calc_probability(*args):
   # period rate:
   n = int(UI_Entries['Number of Attempts'].get())
   k = int(UI_Entries['Number of Success'].get())
   p = float(UI_Entries['Probabilty of Success'].get())

   prob = binomial(n, k) * math.pow(p, k)*math.pow(1-p, n-k)
   prob_str = '%.3f' %(prob)
   UI_Entries['Probability'].delete(0,END)
   UI_Entries['Probability'].insert(0, prob_str )

def about(*args):
   tkMessageBox.showinfo("About", PROG_HELP)

def quit_form(*args):
   root.quit()
   
def makeform(root, fields):
   global UI_Entries
   for field in fields:
      row = Frame(root)
      lab = Label(row, width=22, text=field+": ", anchor='w')
      ent = Entry(row)
      field_values[field]="0"
      ent.insert(0,field_values[field])
      row.pack(side=TOP, fill=X, padx=5, pady=5)
      lab.pack(side=LEFT)
      ent.pack(side=RIGHT, expand=YES, fill=X)
      UI_Entries[field] = ent

def add_callback():
   for field in fields:
      #print field
      ent = UI_Entries[field]
      ent.bind("<FocusOut>", calc_probability)

if __name__ == '__main__':

   root = Tk()
   root.wm_title(PROG_TITLE)
   makeform(root, fields)

   add_callback()

   #root.bind('', (lambda event, e=ents: fetch(e)))   
   b3 = Button(root, text='Quit', command=quit_form)
   b3.pack(side=RIGHT, padx=5, pady=5)

   b2 = Button(root, text='Probability', command=calc_probability)
   b2.pack(side=RIGHT, padx=5, pady=5)

   b1 = Button(root, text='About', command=about)
   b1.pack(side=RIGHT, padx=5, pady=5)

   root.mainloop()

