from faulthandler import disable
from tkinter import *
from tkinter import messagebox

# Definition main class
class Order:
    qtyShirt = 0
    qtyPant = 0

    root = Tk()
    size = ["Small","Medium + $2.50","Large + $3.50"]
    color = ["Green","White + $1.00","Black + $2.00"]

    size_select1 = StringVar()
    size_select2 = StringVar()
    size_select1.set("Small")
    size_select2.set("Small")

    color_select1 = StringVar()
    color_select1.set("Green")
    color_select2 = StringVar()
    color_select2.set("Green")

    def __init__(self):
        # Begining of program
        # self.root = Tk()
        self.root.geometry("950x650") ## Setting window size

        self.root.resizable(False, False) ## Disabling maximize feature
        self.root.title("ORDERING SYSTEM")
        self.root.configure(background = "beige")

        # Creating frame at root
        self.topFrame = Frame(self.root, border = 10)
        self.topFrame.pack(side = TOP)

        self.bottomFrame = Frame(self.root, border = 0, background = "beige")
        self.bottomFrame.pack(anchor = NW)

        # Creating top frame label
        self.L0 = Label(self.topFrame, text = "ORDER RECEIPT SYSTEM", background = "gray",
                        padx = 10, pady = 10, font = ('Georgia', 28, 'bold'), foreground = "Blue2")
        self.L0.grid(row = 0, column = 0)

        Order.information(self)

        self.root.mainloop() ## main loop

        # Defining methods
    
    def information(self):
        
        #Creating labels
        self.label1 = Label(self.bottomFrame, text = 'Information', background = "beige",
               padx = 5, pady = 5, font = ('Georgia', 18, 'bold', 'underline'), foreground = "Blue2")
        self.label1.grid(row = 0, column = 0)
        
        self.label2 = Label(self.bottomFrame, text = 'Full Name*', background = "beige",
               padx = 5, pady = 5, font = ('helvetica', 12, 'bold'), foreground = "Blue2")
        self.label2.grid(row = 1, column = 0, sticky = E)

        self.label3 = Label(self.bottomFrame, text = 'Card Number*', background = "beige",
                       padx = 5, pady = 5, font = ('helvetica', 12, 'bold'), foreground = "Blue2")
        self.label3.grid(row = 2, column = 0, sticky = E)

        self.label4 = Label(self.bottomFrame, text = 'Zip Code*', background = "beige",
                       padx = 5, pady = 5, font = ('helvetica', 12, 'bold'), foreground = "Blue2")
        self.label4.grid(row = 3, column = 0, sticky = E)

        self.output = Label(self.bottomFrame, text = "", background = "beige",
                       padx = 5, pady = 5, font = ('helvetica', 12, 'bold'), foreground = "Blue2")
        self.output.grid(row = 7, column = 0, sticky = E)

        # Creating text entry boxes
        self.entry1 = Entry(self.bottomFrame, width = 18, borderwidth = 2, font = ('helvetica', 12, 'bold'))
        self.entry1.grid(row = 1, column = 1, sticky = W)

        self.entry2 = Entry(self.bottomFrame, width = 18, borderwidth = 2, font = ('helvetica', 12, 'bold'))
        self.entry2.grid(row = 2, column = 1, sticky = W)

        self.entry3 = Entry(self.bottomFrame, width = 18, borderwidth = 2, font = ('helvetica', 12, 'bold'))
        self.entry3.grid(row = 3, column = 1, sticky = W)

        self.clearBtn = Button(self.bottomFrame, text = "CLEAR", font = ('helvetica', 10, 'bold'), foreground = "blue4", width = 10,
                           padx = 5, pady = 5, background = "red", command = self.clear)
        self.clearBtn.grid(row = 6, column = 0, sticky = E)

        self.submitbtn = Button(self.bottomFrame, text = "SUBMIT", font = ('helvetica', 10, 'bold'), foreground = "blue4", width = 10,
                           padx = 5, pady = 5, background = "green2", command = self.submit)
        self.submitbtn.grid(row = 6, column = 1, sticky = W)

#app.information()

    def submit(self):
        try:
            int(self.entry2.get())
            int(self.entry3.get())

            if self.entry1.get() == "" or self.entry2.get() == "" or self.entry3.get() == "":
                #self.output = Label(self.bottomFrame, text = "Fields cannot be empty")
                messagebox.showinfo("showinfo", "Full name must be filled!!!")
                #print("Fields cannot be empty")
                self.clear()
            else:
                print("===================================================================")
                
                self.clearBtn.grid_forget()
                self.submitbtn.grid_forget()
                
                self.shopping()
                self.dropdown()
                self.entry1.config(state = DISABLED)
                self.entry2.config(state = DISABLED)
                self.entry3.config(state = DISABLED)
                self.checkoutbtn.config(state = DISABLED)
                self.informationOutput.config(text = self.entry1.get() + "\n" + 
                                    "Card#: " + self.entry2.get())
                self.receiptHeader.config(text = "**** MY STORE **** " + "\n" +
                                                "123 Some Street \n" + "Some City \n" +
                                                "State" + " " + self.entry3.get() + "\n" +
                                                "Trans# : 2367412" + "\n" + "-----------" + 
                                                "\n" + "\n" + "*** SALE ***")
        except ValueError:
            messagebox.showinfo("showinfo", "Card number and Zip Code must be numbers!!!")
            self.clear()

    def clear(self):
        self.entry1.delete(0, END)
        self.entry2.delete(0, END)
        self.entry3.delete(0, END)
        print("Cleared all text fields")

    def shopping(self):

        # Defining widgets
        self.label4 = Label(self.bottomFrame, text = 'Shopping', background = "beige",
                       padx = 5, pady = 5, font = ('Georgia', 18, 'bold', 'underline'), foreground = "Blue2")
        self.label4.grid(row = 0, column = 2, sticky = E)

        self.label5 = Label(self.bottomFrame, text = 'Qt', background = "beige",
                       padx = 5, pady = 5, font = ('helvetica', 12, 'bold'), foreground = "Blue2")
        self.label5.grid(row = 1, column = 2, sticky = E)

        self.label6 = Label(self.bottomFrame, text = 'Product', background = "beige",
                       padx = 5, pady = 5, font = ('helvetica', 12, 'bold'), foreground = "Blue2")
        self.label6.grid(row = 1, column = 3, sticky = E)

        self.label7 = Label(self.bottomFrame, text = 'Price', background = "beige",
                       padx = 5, pady = 5, font = ('helvetica', 12, 'bold'), foreground = "Blue2")
        self.label7.grid(row = 1, column = 4, sticky = E)

        self.label7 = Label(self.bottomFrame, text = 'Size', background = "beige",
                       padx = 5, pady = 5, font = ('helvetica', 12, 'bold'), foreground = "Blue2")
        self.label7.grid(row = 1, column = 5, sticky = E)

        self.label8 = Label(self.bottomFrame, text = 'Color', background = "beige",
                       padx = 5, pady = 5, font = ('helvetica', 12, 'bold'), foreground = "Blue2")
        self.label8.grid(row = 1, column = 6, sticky = E)

        self.label9 = Label(self.bottomFrame, text = 'Shirt', background = "beige",
                       padx = 5, pady = 5, font = ('helvetica', 12, 'bold'), foreground = "Black")
        self.label9.grid(row = 2, column = 3, sticky = E)

        self.label10 = Label(self.bottomFrame, text = 'Pant', background = "beige",
                       padx = 5, pady = 5, font = ('helvetica', 12, 'bold'), foreground = "Black")
        self.label10.grid(row = 3, column = 3, sticky = E)

        self.label11 = Label(self.bottomFrame, text = '$15.99', background = "beige",
                       padx = 5, pady = 5, font = ('helvetica', 12), foreground = "Black")
        self.label11.grid(row = 2, column = 4, sticky = E)

        self.label12 = Label(self.bottomFrame, text = '$20.99', background = "beige",
                       padx = 5, pady = 5, font = ('helvetica', 12), foreground = "Black")
        self.label12.grid(row = 3, column = 4, sticky = E)

        self.receiptHeader =  Label(self.bottomFrame, text = 'Receipt Header', background = "beige",
                       padx = 5, pady = 5, font = ('helvetica', 12, 'bold'), foreground = "Black")
        self.receiptHeader.grid(row = 8, column = 0, sticky = E)

        self.informationOutput =  Label(self.bottomFrame, text = '', background = "beige",
                       padx = 5, pady = 5, font = ('helvetica', 12, 'bold'), foreground = "Black")
        self.informationOutput.grid(row = 10, column = 0, sticky = E)

        self.shoppingOutputShirt =  Label(self.bottomFrame, text = '', background = "beige",
                       padx = 5, pady = 5, font = ('helvetica', 12, 'bold'), foreground = "Black")
        self.shoppingOutputShirt.grid(row = 12, column = 0, sticky = E)

        self.shoppingOutputPant =  Label(self.bottomFrame, text = '', background = "beige",
                       padx = 5, pady = 5, font = ('helvetica', 12, 'bold'), foreground = "Black")
        self.shoppingOutputPant.grid(row = 13, column = 0, sticky = E)

        # Creating text entry boxes

        self.entry_qt1 = Entry(self.bottomFrame, width = 2, borderwidth = 2, font = ('helvetica', 12, 'bold'))
        self.entry_qt1.grid(row = 2, column = 2, sticky = E)

        self.entry_qt2 = Entry(self.bottomFrame, width = 2, borderwidth = 2, font = ('helvetica', 12, 'bold'))
        self.entry_qt2.grid(row = 3, column = 2, sticky = E)

        # Creating buttons
        self.add_shirt = Button(self.bottomFrame, text = "ADD", font = ('helvetica', 10, 'bold'), foreground = "white", width = 5,
                          padx = 2, pady = 2, background = "gray", command = self.shirtCart)
        self.add_shirt.grid(row = 2, column = 7, sticky = E)

        self.add_pant = Button(self.bottomFrame, text = "ADD", font = ('helvetica', 10, 'bold'), foreground = "white", width = 5,
                          padx = 2, pady = 2, background = "gray", command = self.pantCart)
        self.add_pant.grid(row = 3, column = 7, sticky = E)

        self.cancelbtn = Button(self.bottomFrame, text = "CANCEL", font = ('helvetica', 10, 'bold'), foreground = "white", width = 8,
                          padx = 5, pady = 5, background = "red", command = self.cancel)
        self.cancelbtn.grid(row = 6, column = 6, sticky = E)

        self.checkoutbtn = Button(self.bottomFrame, text = "CHECK OUT", font = ('helvetica', 10, 'bold'), foreground = "white", width = 8,
                          padx = 5, pady = 5, background = "green2", command = self.checkout)
        self.checkoutbtn.grid(row = 6, column = 7, sticky = W)
    
    def cancel(self):
        self.topFrame.destroy()
        self.bottomFrame.destroy()
        self.__init__()
        #self.information()

    def dropdown(self):
        #self.bottomFrame = bottomFrame

        # Declaring variables
        size = ["Small","Medium + $2.50","Large + $3.50"]
        color = ["Green","White","Black"]
        
        # Creating dropdown menu
        # size_select1 = StringVar()
        # size_select2 = StringVar()
        # size_select1.set("Small")
        # size_select2.set("Small")

        # color_select1 = StringVar()
        # color_select1.set("Green")
        # color_select2 = StringVar()
        # color_select2.set("Green")
        self.shirt_size1 = OptionMenu(self.bottomFrame , self.size_select1, *size)
        self.shirt_size1.grid(row = 2, column = 5)

        self.shirt_color1 = OptionMenu(self.bottomFrame , self.color_select1 , *color)
        self.shirt_color1.grid(row = 2, column = 6)

        self.pant_size2 = OptionMenu(self.bottomFrame , self.size_select2, *size)
        self.pant_size2.grid(row = 3, column = 5)

        self.pant_color2 = OptionMenu(self.bottomFrame , self.color_select2 , *color)
        self.pant_color2.grid(row = 3, column = 6)

        #choice = size_select1.get()
        #print(choice)
        
    def shirtCart(self):
        try:
            int(self.entry_qt1.get())
            self.qtyShirt = 0            
            self.checkoutbtn.config(state = NORMAL)
            self.qtyShirt = self.entry_qt1.get()
            sizeSelected = self.size_select1.get()
            colorSelected = self.color_select1.get()
            self.shoppingOutputShirt.config(text = "\n" + self.entry_qt1.get() + " SHIRT(S) " + self.size_select1.get() + " " + 
                                    self.color_select1.get())
            self.entry_qt1.config(state = DISABLED)
            self.add_shirt.config(state = DISABLED)
            #self.entry_qt1.delete(0, END)
        except:
            messagebox.showinfo("showinfo", "Quantity must be a number!!!")
            self.entry_qt1.delete(0, END) 
            

    def pantCart(self):        
        try:
            self.qtyPant = 0
            self.checkoutbtn.config(state = NORMAL)
            self.qtyPant = self.entry_qt2.get()
            
            sizeSelected = self.size_select2.get()
            colorSelected = self.color_select2.get()
            self.shoppingOutputPant.config(text = self.entry_qt2.get() + " PANT(S) " + self.size_select2.get() + " " + 
                                    self.color_select2.get())
            self.entry_qt2.config(state = DISABLED)
            self.add_pant.config(state = DISABLED)            
            #self.entry_qt2.delete(0, END)
        except:
            messagebox.showinfo("showinfo", "Quantity must be a number!!!")
            self.entry_qt2.delete(0, END)

    # Resetting all value when Cancel button
    def resetAllValues(self):
        self.qtyShirt = 0
        self.qtyPant = 0

        self.size_select1.set("Small")
        self.size_select2.set("Small")

        self.color_select1.set("Green")
        self.color_select2.set("Green")

    # Computing customer order
    def checkout(self):
        try:
            #int(self.entry_qt1.get())
            #int(self.entry_qt2.get())

            # Code for Shirt Cart
            if (self.qtyShirt != ""):

                if (self.size_select1.get() == "Small"):
                    sizePrice = 0.0
                elif(self.size_select1.get() == "Medium + $2.50"):
                    sizePrice = 2.50
                else:
                    sizePrice = 3.50

                # print("Selected shirt size is: ", self.size_select1.get())

                if (self.color_select1.get() == "Green"):
                    colorPrice = 0.0
                elif(self.color_select1.get() == "White"):
                    colorPrice = 1.0
                else:
                    colorPrice = 2.0

                # print("Selected shirt color is: ", self.color_select1.get())

                if (self.entry_qt1 == ""):
                    unitPriceShirt = 0.0
                    colorPrice = 0.0
                    sizePrice = 0
                else:
                    # print("Selected shirt quantity is: ", self.qtyShirt)
                    unitPriceShirt = 15.99
                    self.totalShirtPrice = float((unitPriceShirt + colorPrice + sizePrice) * float(self.qtyShirt))
                    self.shoppingOutputShirt.config(text = "\n" + self.entry_qt1.get() + " SHIRT(S) " + self.size_select1.get() + " " + 
                                    self.color_select1.get() + "\n" + "${:.2f}".format(self.totalShirtPrice))
                
                if (self.totalShirtPrice == 0):
                    print("No shirt was purchased!!!")
                    print()
                else:
                    print("Selected shirt size is: ", self.size_select1.get())
                    print("Selected shirt color is: ", self.color_select1.get())
                    print("Selected shirt quantity is: ", self.qtyShirt)
                    print()
                    print("Total Shirt Price: ${:.2f}".format(self.totalShirtPrice))
                    print()                 
                # Shirt cart complete --------------------------


            # Code for Pant cart
            if (self.qtyPant != ""):            
                if (self.size_select2.get() == "Small"):
                    sizePrice = 0.0
                elif(self.size_select2.get() == "Medium + $2.50"):
                    sizePrice = 2.50
                else:
                    sizePrice = 3.50

                # print("Selected pant size is: ", self.size_select2.get())

                if (self.color_select2.get() == "Green"):
                    colorPrice = 0.0
                elif(self.color_select2.get() == "White"):
                    colorPrice = 1.0
                else:
                    colorPrice = 2.0

                # print("Selected pant color is: ", self.color_select2.get())

                if (self.entry_qt2 == ""):
                    unitPricePant = 0.0
                    colorPrice = 0.0
                    sizePrice = 0
                else:
                    #self.qtyPant = self.entry_qt2.get()
                    # print("Selected quantity is: ", self.qtyPant)
                    unitPricePant = 20.99
                    self.totalPantPrice = float((unitPricePant + colorPrice + sizePrice) * float(self.qtyPant))
                    self.shoppingOutputPant.config(text = "\n" + self.entry_qt2.get() + " PANT(S) " + self.size_select2.get() + " " + 
                                    self.color_select2.get() + "\n" + "${:.2f}".format(self.totalPantPrice))
                
                if (self.totalPantPrice == 0):
                    print("No pant was purchased")
                    print()
                else:
                    print("Selected pant size is: ", self.size_select2.get())
                    print("Selected pant color is: ", self.color_select2.get())
                    print("Selected quantity is: ", self.qtyPant)
                    print()
                    print("Total Pant Price: ${:.2f}".format(self.totalPantPrice))
                    print()

            subTotal = self.totalShirtPrice + self.totalPantPrice
            print("Subtotal: ${:.2f}".format(subTotal))
            print()

            taxPercent = 0.07

            tax = subTotal * taxPercent

            print("Tax: ${:.2f}".format(tax))

            checkoutTotal = (subTotal * taxPercent) + subTotal

            print("Total: ${:.2f}".format(checkoutTotal))

            self.resetAllValues()
            self.checkoutbtn.config(state = DISABLED)



        except ValueError:            
            self.resetAllValues()
            self.checkoutbtn.config(state = DISABLED)
            messagebox.showinfo("showinfo", "Quantity must be a number!!!")

        ########################################################################################################
        
        

        

        # self.entry_qt1.delete(0, END)
        # self.entry_qt2.delete(0, END)

        # if (self.size_select1.get() == "Small"):
        #     sizePrice = 0.0
        # elif(self.size_select1.get() == "Medium + $2.50"):
        #     sizePrice = 2.50
        # else:
        #     sizePrice = 3.50

        # if (self.color_select2.get() == "Green"):
        #     colorPrice = 0.0
        # elif(self.color_select2.get() == "White + $1.00"):
        #     colorPrice = 1.0
        # else:
        #     colorPrice = 2.0

        
   
        # print(self.qtyShirt)
        # totalShirtPrice = float((unitPriceShirt + colorPrice + sizePrice) * float(self.qtyShirt))
        #totalPantPrice = float((unitPricePant + colorPrice + sizePrice) * float(self.qtyShirt))

        #print(totalShirtPrice)
        #print(totalPantPrice)

        #subTotal = totalShirtPrice + totalPantPrice

        #print(subTotal)

        #print(f'\nYour Receit is as follows: ------> \n\nShirt size: {self.size_select1.get()} \nColor: {self.color_select1.get()} \nQuantity: {self.qtyShirt} \nUnit Price: ${unitPriceShirt} \n\nTotal Price: ${totalShirtPrice}')
        
        receipt = "******************* STORE NAME *******************"
        receipt += "\n123 Some Street"
        receipt += "\n03/11/2022"
        receipt += "\nTrans: 1234(random #)"
        receipt += "\nSALE\n"
        receipt += "\n[----- BAR CODE ----]"
        
       
        # PANT  Small  Color  ---------------------- $41.98
        #     2 @ $20.99

        # Subtotal -------------------------------- $41.98
        # Total Sales tax ------------------------- $2.00
        # Total ----------------------------------- $43.98
        #     Debit
        #         Card: Master Card
        #         Account: 1234
        #         AID: A0000000033623
        #         CVM: Verify by Pin
            
        #     Total Debit ------------------------ $43.98"
        #print(receipt)
        
        #print(f'\nSHIRT - {self.size_select1.get()} - {self.color_select1.get()} ({self.qtyShirt} @ ${unitPriceShirt}) ---------------------- ${totalShirtPrice}')
        '''
        ******************* STORE NAME *******************
        123 Some Street
        Some City, SS, 12345
        03/11/2022
        Trans: 1234(random #)

        SALE
        [----- BAR CODE ----]

        PANT  Small  Color  ---------------------- $41.98
            2 @ $20.99

        Subtotal -------------------------------- $41.98
        Total Sales tax ------------------------- $2.00
        Total ----------------------------------- $43.98
            Debit
                Card: Master Card
                Account: 1234
                AID: A0000000033623
                CVM: Verify by Pin
            
            Total Debit ------------------------ $43.98
        
        '''

        '''
        - Ensure Clear & submit button disapear upon submit
        - Ensure all data type  are properly validated (may use lambda)
        - Implement Pant logic
        - Save receipt to file
        - Display cart item on GUI (find how to print to label)

        '''

        



app = Order()