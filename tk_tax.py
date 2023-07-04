#!/usr/bin/env python3

import locale
import os.path
import argparse
import configparser
from tkinter import messagebox
from tkinter import *


# The title of the program
PROG_TITLE="Tax Calculator 2017"

# The name of the config file
CONFIG_FILE=".tk_tax.ini"

CONFIG_NAME='Tax'

# Social Security Tax Cap in 2017
SS_TAX_CAP= 127200
SS_TAX_RATE = 0.062
MED_TAX_RATE = 0.0145

#Number of Pay Period
NUM_PAY_PERIOD_STR='Number of Pay Period'
NUM_PAY_PERIOD=24

# Federal Tax Rate for 2017
FILE_TYPE_STR='File Type'
FILE_TYPE=2

PERSONAL_DEDUCTION = 4050
FED_TAX_RATES=[0.10, 0.15, 0.25, 0.28, 0.33, 0.35, 0.396]

STD_DEDUCTION_M = 12700
FED_TAX_LIMITS_M = [ 18650, 75900, 153100, 233350, 416700, 470700, 10000000000 ]

STD_DEDUCTION_S = 6350
FED_TAX_LIMITS_S = [ 9325, 37950, 91900, 191650, 416700, 418400, 10000000000 ]


# Help String
PROG_HELP="Tax Calculator in Python\n\nCopyright 2017\nwww.liteon-pss.com"


#Fields
fields = ['Annual Income', 'Health Insurance', '401K Contribution', 'Number of Children', 'Number of Deductible', 'Federal Tax','Social Security Tax','Medicare Tax', 'Take Home Pay']
field_values = {}

annual_income = 0.0


def get_ss_tax(total_income, insurance):
   ss_taxable = total_income - insurance
   if ss_taxable < SS_TAX_CAP:
      return ss_taxable * SS_TAX_RATE
   else:
      return SS_TAX_CAP * SS_TAX_RATE 

def get_medicare_tax(total_income, insurance):
   med_taxable = total_income - insurance
   return med_taxable * MED_TAX_RATE

def get_fed_tax(total_income, insurance, k401, num_children, num_ded):
   if FILE_TYPE == 1:
     STD_DEDUCTION=STD_DEDUCTION_S
     FED_TAX_LIMITS=FED_TAX_LIMITS_S
   else:
     STD_DEDUCTION=STD_DEDUCTION_M
     FED_TAX_LIMITS=FED_TAX_LIMITS_M
     
   fed_taxable = total_income - insurance - k401 - STD_DEDUCTION - PERSONAL_DEDUCTION * num_ded
   #print "%d %d %d %d %d %d" %(total_income, insurance, k401, STD_DEDUCTION, PERSONAL_DEDUCTION * num_ded, fed_taxable)
   num_bracket = len(FED_TAX_RATES)
   fed_tax = 0.0
   lower_limit = 0.0
   for i in range(0, num_bracket):
     if fed_taxable < FED_TAX_LIMITS[i]:
       fed_tax = fed_tax + (fed_taxable - lower_limit) * FED_TAX_RATES[i]
       return fed_tax - 1000.0 *num_children
     else:
       fed_tax = fed_tax + (FED_TAX_LIMITS[i] - lower_limit) * FED_TAX_RATES[i]
       #print fed_tax
       lower_limit = FED_TAX_LIMITS[i]

def load_config():
   global field_values
   global annual_income
   global NUM_PAY_PERIOD

   # Initialize the defaults
   for field in fields:
      field_values[field] = "0"

   if os.path.isfile(CONFIG_FILE):
      config = configparser.RawConfigParser()
      config.read(CONFIG_FILE)
      NUM_PAY_PERIOD = int(config.get(CONFIG_NAME, NUM_PAY_PERIOD_STR))
      FILE_TYPE= int(config.get(CONFIG_NAME, FILE_TYPE_STR))
      for field in fields:
         field_values[field] = config.get(CONFIG_NAME, field)
         #print field,field_values[field]
         if field == 'Annual Income':
           annual_income = locale.atof(field_values[field].strip(MONEY_SYM))
           #print annual_income

def save_config():
   config = configparser.RawConfigParser()

   config.add_section(CONFIG_NAME)
   config.set(CONFIG_NAME, NUM_PAY_PERIOD_STR, NUM_PAY_PERIOD)
   config.set(CONFIG_NAME, FILE_TYPE_STR, FILE_TYPE)
   for field in fields:
      value = field_values[field]
      config.set(CONFIG_NAME, field, value)
   with open(CONFIG_FILE, 'w') as configFile:
      config.write(configFile)

class ConfigWindow(Frame):
  PAY_TYPES = [ ('Monthly' , '12'), ('Bi-Monthly', '24'), ('Bi-Weekly', '26')]
  FILE_TYPES = [ ('Individual' , '1'), ('Married Filed Jointly', '2')]

  def __init__(self, parent, *args, **kwargs):
    Frame.__init__(self, *args, **kwargs)

    self.parent = parent
    self.pay_type = IntVar()
    self.file_type = IntVar()

    self.pay_type.set(NUM_PAY_PERIOD)

    self.file_type.set(FILE_TYPE)

    self.toplevel = Toplevel(self)
    self.toplevel.wm_title('Config Window')

    row = Frame(self.toplevel)
    row.pack(side=TOP, fill=X, padx=5, pady=5)
    lab = Label(row, width=22, text='Pay Type:', anchor='w')
    lab.pack(side=LEFT, anchor='w')
    for txt, val in self.PAY_TYPES:
      r = Radiobutton(row, text=txt, variable = self.pay_type, value=val)
      r.pack(side=RIGHT, anchor='w', padx=50, pady=10)

    row = Frame(self.toplevel)
    row.pack(side=TOP, fill=X, padx=5, pady=5)
    lab = Label(row, width=22, text='File Type:', anchor='w')
    lab.pack(side=LEFT, anchor='w')
    for txt, val in self.FILE_TYPES:
      r = Radiobutton(row, text=txt, variable = self.file_type, value=val)
      r.pack(side=LEFT, anchor='w', padx=50, pady=10)

    b1 = Button(self.toplevel, text='Quit', command=self.toplevel.destroy)
    b1.pack(side=RIGHT, padx=5, pady=5)

    b2 = Button(self.toplevel, text='Apply Setting', command=self.apply_setting)
    b2.pack(side=RIGHT, padx=5, pady=5)

  def apply_setting(self):
    global NUM_PAY_PERIOD
    global FILE_TYPE

    NUM_PAY_PERIOD= int(self.pay_type.get())
    FILE_TYPE = int(self.file_type.get())

    #print NUM_PAY_PERIOD
    self.toplevel.destroy()
    self.parent.calc_tax()
    

class MainWindow(Frame):
  #Headings
  headings = ['Field', 'Yearly', 'Each Pay Period', 'Percent']

  UI_Entries={}
  UI_Entries2={}
  UI_Entries3={}

  def __init__(self, *args, **kwargs):
    global fields
    Frame.__init__(self, *args, **kwargs)

    self.makeform(self.headings, fields)

    self.add_callback()

    #root.bind('', (lambda event, e=ents: fetch(e)))   
    b3 = Button(self, text='Quit', command=self.quit_form)
    b3.pack(side=RIGHT, padx=5, pady=5)

    b2 = Button(self, text='Calc Income', command=self.calc_tax)
    b2.pack(side=RIGHT, padx=5, pady=5)

    b2a = Button(self, text='Config', command=self.config_tax)
    b2a.pack(side=RIGHT, padx=5, pady=5)

    b1 = Button(self, text='About', command=self.about)
    b1.pack(side=RIGHT, padx=5, pady=5)


  def read_value(self, field):
    global field_values
    value = self.UI_Entries[field].get()
    field_values[field] = value

    self.UI_Entries2[field].config(state='normal')
    self.UI_Entries2[field].delete(0, END)
    self.UI_Entries2[field].insert(0, value)
    self.UI_Entries2[field].config(state='readonly')

    self.UI_Entries3[field].config(state='normal')
    self.UI_Entries3[field].delete(0, END)
    self.UI_Entries3[field].insert(0, value)
    self.UI_Entries3[field].config(state='readonly')

    return value

  def read_curr_value(self, field):
    global field_values
    global annual_income
    value = locale.atof(self.UI_Entries[field].get().strip(MONEY_SYM))
    value_str = locale.currency(value, grouping=True)
    self.UI_Entries[field].delete(0, END)
    self.UI_Entries[field].insert(0, value_str)
    field_values[field] = value_str

    if field == 'Annual Income':
      annual_income = value
    
    # Calculate per pay period
    value2 = value/NUM_PAY_PERIOD
    value2_str = locale.currency(value2, grouping=True)
    self.UI_Entries2[field].config(state='normal')
    self.UI_Entries2[field].delete(0, END)
    self.UI_Entries2[field].insert(0, value2_str)
    self.UI_Entries2[field].config(state='readonly')

    # Calculate percentage
    if annual_income != 0:
      value3 = value/annual_income * 100.0
      value3_str = '{0:2.1f}%'.format(value3)
      self.UI_Entries3[field].config(state='normal')
      self.UI_Entries3[field].delete(0, END)
      self.UI_Entries3[field].insert(0, value3_str)
      self.UI_Entries3[field].config(state='readonly')

    return value

  def write_curr_value(self, field, value):
    global annual_income
    global field_values
    value_str = locale.currency(value, grouping=True)
    self.UI_Entries[field].delete(0, END)
    self.UI_Entries[field].insert(0, value_str)
    field_values[field] = value_str

    # Calculate per pay period
    value2 = value/NUM_PAY_PERIOD
    value2_str = locale.currency(value2, grouping=True)
    self.UI_Entries2[field].config(state='normal')
    self.UI_Entries2[field].delete(0, END)
    self.UI_Entries2[field].insert(0, value2_str)
    self.UI_Entries2[field].config(state='readonly')

    # Calculate percentage
    if annual_income != 0:
      value3 = value/annual_income * 100.0
      value3_str = '{0:2.1f}%'.format(value3)
      self.UI_Entries3[field].config(state='normal')
      self.UI_Entries3[field].delete(0, END)
      self.UI_Entries3[field].insert(0, value3_str)
      self.UI_Entries3[field].config(state='readonly')

  def calc_tax(self, *args):
    # Annual Income:
    income = self.read_curr_value('Annual Income')
    insurance = self.read_curr_value('Health Insurance')
    k401 = self.read_curr_value('401K Contribution')
    num_ded = int(self.read_value('Number of Deductible'))
    num_children = int(self.read_value('Number of Children'))

    total_income = income 

    ss_tax = get_ss_tax(total_income, insurance)
    self.write_curr_value('Social Security Tax', ss_tax)
    #print ss_tax

    med_tax = get_medicare_tax(total_income, insurance)
    self.write_curr_value('Medicare Tax', med_tax)
    #print med_tax

    fed_tax = get_fed_tax(total_income, insurance, k401, num_children, num_ded)
    self.write_curr_value('Federal Tax', fed_tax)

    take_home_pay = total_income - insurance - ss_tax - med_tax - k401 - fed_tax
    self.write_curr_value('Take Home Pay', take_home_pay)


  def config_tax(self, *args):
    config = ConfigWindow(self)
    config.pack(side='top', fill='both', expand=True)


  def about(self, *args):
    messagebox.showinfo("About", PROG_HELP)


  def quit_form(self, *args):
    save_config()
    root.quit()
   
  def makeheading(root, headings):
    row = Frame(root)
    row.pack(side=TOP, fill=X, padx=5, pady=5)
    num = len(headings)
    for i in range(0, num):
      lab = Label(row, width=22, text=headings[i], anchor='w')
      if i < (num -1):
        lab.pack(side=LEFT)
      else:
        lab.pack(side=RIGHT, expand=YES, fill=X)


  def makeform(self, headings, fields):
    global field_values

    self.makeheading(headings)
    for field in fields:
      row = Frame(self)
      lab = Label(row, width=22, text=field+": ", anchor='w')

      ent = Entry(row)
      ent.insert(0,field_values[field])

      ent2 = Entry(row)
      if (field_values[field]).startswith(MONEY_SYM):
        value = locale.atof(field_values[field].strip(MONEY_SYM))
        value2 = value/ NUM_PAY_PERIOD
        value2_str = locale.currency(value2, grouping=True)
        ent2.insert(0,value2_str)
      else:
        ent2.insert(0,field_values[field])

      ent2.config(state='readonly')

      ent3 = Entry(row)
      if (field_values[field]).startswith(MONEY_SYM):
        value = locale.atof(field_values[field].strip(MONEY_SYM))

        if annual_income != 0.0:
          value3 = value/ annual_income * 100.0
          value3_str = '{0:2.1f}%'.format(value3)
          #print value3_str, annual_income, value
          ent3.insert(0,value3_str)
      else:
        ent3.insert(0,field_values[field])

      ent3.config(state='readonly')

      row.pack(side=TOP, fill=X, padx=5, pady=5)
      lab.pack(side=LEFT)
      ent.pack(side=LEFT, padx = 5)
      ent2.pack(side=LEFT, padx =5)
      ent3.pack(side=RIGHT, padx=5, expand=YES, fill=X)
      self.UI_Entries[field] = ent
      self.UI_Entries2[field] = ent2
      self.UI_Entries3[field] = ent3

  def add_callback(self):
    for field in fields:
      ent = self.UI_Entries[field]
      ent.bind("<FocusOut>", self.calc_tax)


if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('--config','-c',default=CONFIG_FILE,help='Configuration File')

  args = parser.parse_args()

  CONFIG_FILE=args.config

  # Find the local currency symbol
  locale.setlocale(locale.LC_ALL,'')
  locale_mon = locale.localeconv()
  MONEY_SYM = locale_mon['currency_symbol']

  load_config()

  root = Tk()
  root.wm_title(PROG_TITLE)
  main = MainWindow(root)
  main.pack(side='top', fill='both', expand=True)

  root.mainloop()

