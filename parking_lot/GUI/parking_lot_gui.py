from tkinter import * 
from tkinter.ttk import *

# creates a Tk() object 
root = Tk() 

# sets the geometry of main  
# root window 
root.geometry("500x500") 
  

def openEntry():
    
    openEntry = Toplevel(root)
    openEntry.title("Robotic Parking Systems, Inc.")
    openEntry.geometry("500 * 500")
    openEntry.config(background = "lightgreen")
    label2= Label(openEntry, text = "enter").grid(row=0)
    e1 = Entry(openEntry)
    e1.grid(row = 0, column = 1)
    #label2.pack(pady = 10)
#command class package commands ui entities folders for file

def openNewWindow(): 
      
    newWindow = Toplevel(root)
    newWindow.title("Robotic Parking Systems, Inc.")
    newWindow.geometry("500x500")
    newWindow.config(background = "lightblue")
    label1 = Label(newWindow, text = "ON ROUTE TO YOUR PARKING LOT")
    label1.config(background = "lightblue")
    label1.pack(pady = 10)
    btn2 = Button(newWindow, text = "Provide",command = openEntry)
    
    btn2.pack(pady=10)
    Label(newWindow, text = "Provide No. of Slots Required").pack()

root.title("Robotic Parking Systems, Inc.")

root.config(background = 'lightblue')
label = Label(root, text = "Click here to CREATE A PARKING LOT")
label.config(background = 'lightblue')

label.pack(pady = 10)

btn = Button(root, text = "Create Slots", command = openNewWindow)
btn.pack(pady = 10)

mainloop()