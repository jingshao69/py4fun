#!/usr/bin/env python3

import locale
import os.path
import tkinter.messagebox
import tkinter.filedialog 
from tkinter import *

from glob import glob
import myhash

# The title of the program
PROG_TITLE="tk_hash"

# Help String
PROG_HELP="Hash Calculator in Python"

class MyForm(Frame):
  fields = ('MD5 Hash', 'SHA1 Hash', 'SHA256 Hash')
  FileEntry= None
  HashValues={}

  def about(*args):
    tkMessageBox.showinfo("About", PROG_HELP)

  def quit_form(*args):
    root.quit()

  def load_file(self):
    fname = tkinter.filedialog.askopenfilename(filetypes=[ ("All files", "*.*") ])
    if fname:
      self.title_file = fname 
      self.fileEntry.insert(0, fname)
      md5_val = myhash.md5sum(fname)
      self.HashValues['MD5 Hash'].set(md5_val)
      sha1_val = myhash.sha1sum(fname)
      self.HashValues['SHA1 Hash'].set(sha1_val)
      sha256_val = myhash.sha256sum(fname)
      self.HashValues['SHA256 Hash'].set(sha256_val)

  def __init__(self, root):
    Frame.__init__(self, root)

    row = Frame(root)
    lab = Label(row, width=16, text='File: ', anchor='w')
    self.fileEntry = Entry(row,width=64)
    self.fileEntry.insert(0,"")
    fileButton = Button(row, text='Browse', command=self.load_file)
    row.pack(side=TOP, fill=X, padx=5, pady=5)
    lab.pack(side=LEFT)
    self.fileEntry.pack(side=LEFT)
    fileButton.pack(side=RIGHT, padx=5, pady=5)

    for f in self.fields:
        row = Frame(root)
        lab_txt = f + ' :'
        lab = Label(row, width=16, text=lab_txt, anchor='w')
        self.HashValues[f] = StringVar()
        entry = Entry(row, state='readonly', textvariable=self.HashValues[f], width=64)
        row.pack(side=TOP, fill=X, padx=5, pady=5)
        lab.pack(side=LEFT)
        entry.pack(side=LEFT)

    b3 = Button(root, text='Quit', command=self.quit_form)
    b3.pack(side=RIGHT, padx=5, pady=5)

    b1 = Button(root, text='About', command=self.about)
    b1.pack(side=RIGHT, padx=5, pady=5)

if __name__ == '__main__':

   root = Tk()
   root.wm_title(PROG_TITLE)
   form = MyForm(root)

   root.mainloop()


