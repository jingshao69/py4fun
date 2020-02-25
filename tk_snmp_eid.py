#!/usr/bin/python3

import locale
import os.path
import configparser
import tkinter.messagebox
from tkinter import *


# The title of the program
PROG_TITLE="SNMP Engine ID"

# Help String
PROG_HELP="SNMP Engine ID Calculator in Python"

#Fields
fields = ('MAC Address', 'SNMP Engine ID')

field_values = {}
UI_Entries={}

PEN=34675

def snmp_engine_id(*args):
    global PEN
    mac_str = UI_Entries['MAC Address'].get()
    mac_str = mac_str.replace(':','').lower()
    PEN = PEN | 0x80000000
    pen_str = hex(PEN)[2:]
    engine_id_str = pen_str + "03" + mac_str + "00"
    UI_Entries['SNMP Engine ID'].delete(0, END)

    UI_Entries['SNMP Engine ID'].insert(0, engine_id_str)

def about(*args):
    tkinter.messagebox.showinfo("About", PROG_HELP)


def quit_form(*args):
    root.quit()
   

def makeform(root, fields):
    global UI_Entries
    for field in fields:
        row = Frame(root)
        lab = Label(row, width=16, text=field+": ", anchor='w')
        ent = Entry(row, width=28)
        row.pack(side=TOP, fill=X, padx=5, pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT, expand=YES, fill=X)
        UI_Entries[field] = ent

def add_callback():
    for field in fields:
        #print field
        ent = UI_Entries[field]
        ent.bind("<FocusOut>", snmp_engine_id)


if __name__ == '__main__':

    root = Tk()
    root.wm_title(PROG_TITLE)
    makeform(root, fields)

    add_callback()

    #root.bind('', (lambda event, e=ents: fetch(e)))   
    b3 = Button(root, text='Quit', command=quit_form)
    b3.pack(side=RIGHT, padx=5, pady=5)

    b2 = Button(root, text='Engine ID', command=snmp_engine_id)
    b2.pack(side=RIGHT, padx=5, pady=5)

    b1 = Button(root, text='About', command=about)
    b1.pack(side=RIGHT, padx=5, pady=5)

    root.mainloop()

