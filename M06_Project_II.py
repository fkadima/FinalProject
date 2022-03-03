# Begining of program

from tkinter import *
import sys

#def main():
root = Tk()

# Configuring the window
root.title("Order System")
root.geometry("500x550")
root.configure(background = "white")

'''
# Test login popup page
login = Tk()
login.geometry("100x150")

def login_window():
    top = Toplevel(login)
    top.geometry("100x150")
    top.title(Login)
    L0 = Label(text = "ORDER RECEIPT SYSTEM", padx = 20, pady = 5, font = "bold",
               foreground = "blue")
    L0.grid(row = 3, column = 1)
'''
gender = ["M", "F"]
apparel = ["pant","shirt"]

# Defining method to clear data from input boxes
def clear():
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry5.delete(0, END)
    entry6.delete(0, END)

# Defining method to 
def display():
    name = (entry1.get())
    street = str(entry2.get())
    city = str(entry3.get())
    state = str(entry4.get())
    zipCode = int(entry5.get())
    card_num = int(entry6.get())

    # data validation
    if type (name) != str and name != "":
        print("Continue")
    else:
        print ("invalid info")

'''
    # data validation
    if type (name) == str and type (street) == str and type (city) == str and type (state) == str and type(zipCode) == int and type (card_num) == int:
        print("Valid info")
    else:
        print ("invalid info")
'''        




# Setting up the label & input boxes
L0 = Label(text = "WELCOME TO OUR ORDER SYSTEM", padx = 20, pady = 5, font=('Georgia 18 bold underline'), foreground = "blue")
L0.grid(row = 2, column = 1)

L1 = Label(text = "Customer information", foreground = "black", font=('Helvetica 15 underline'))
L1.grid(row = 5, column = 0)

L2 = Label(text = "Name", padx = 20, pady = 5, font = "bold", foreground = "blue", justify= LEFT)
L2.grid(row = 7, column = 0)

entry1 = Entry(root, width = 35, borderwidth = 10)
entry1.grid(row = 7, column = 1)

L2 = Label(text = "Street Address", padx = 20, pady = 5, font = "bold", foreground = "blue")
L2.grid(row = 8, column = 0)

entry2 = Entry(root, width = 35, borderwidth = 10)
entry2.grid(row = 8, column = 1)

L3 = Label(text = "City", padx = 20, pady = 5, font = "bold", foreground = "blue")
L3.grid(row = 9, column = 0)

entry3 = Entry(root, width = 35, borderwidth = 10)
entry3.grid(row = 9, column = 1)

L4 = Label(text = "State", padx = 20, pady = 5, font = "bold", foreground = "blue")
L4.grid(row = 11, column = 0)

entry4 = Entry(root, width = 35, borderwidth = 10)
entry4.grid(row = 11, column = 1)

L5 = Label(text = "Zip Code", padx = 20, pady = 5, font = "bold", foreground = "blue")
L5.grid(row = 13, column = 0)

entry5 = Entry(root, width = 35, borderwidth = 10)
entry5.grid(row = 13, column = 1)

L6 = Label(text = "Card Number", padx = 20, pady = 5, font = "bold", foreground = "blue")
L6.grid(row = 15, column = 0)

entry6 = Entry(root, width = 35, borderwidth = 10)
entry6.grid(row = 15, column = 1)

# Setting up the buttons
btnF = Button(root, text = "Submit", padx = 20, pady = 10, background = "green", command = display)
btnF.grid(row = 17, column = 1)

#clearbtn = Button(root, text = "CLEAR", padx = 40, pady = 10, background = "yellow", command = clear)
#clearbtn.grid(row = 17, column = 1)

# Calling main() to run
root.mainloop()
