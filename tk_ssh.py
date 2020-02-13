#!/usr/bin/python3

import os.path
from tkinter import *


# The title of the program
PROG_TITLE="SSH Launcher"

# The name of the config file
CONFIG_FILE=".ssh_list"

# Help String
PROG_HELP="SSH Launcher"

targets=[]

def loadTargets():
    fpath = os.path.join(os.environ['HOME'], CONFIG_FILE)
    with open(fpath, 'r') as f:
        for line in f:
            target = line.strip()
            #print(target)
            if len(target) > 0:
                targets.append(target)

def quit_form(*args):
   root.quit()

def launch_ssh(target):
    cmd = 'gnome-terminal -x sh -c "ssh -X ' + target + '"'
    #print(cmd)
    os.system(cmd) 

if __name__ == '__main__':

    #Create & Configure root 
    root = Tk()
    root.title(PROG_TITLE)

    root.geometry('200x200')
    loadTargets()
    numTargets=len(targets)
    #print(numTargets)

    #Create a 5x10 (rows x columns) grid of buttons inside the frame
    for i in range(numTargets):
        btnText = targets[i]
        btn = Button(root, text=btnText, command=lambda txt=btnText:launch_ssh(txt))
        btn.pack()

    quitBtn = Button(root, text='Quit', command=quit_form)
    quitBtn.pack(side=RIGHT, padx=5, pady=5)

    root.mainloop()

