"""Final Project  SDEV140  Eric Brummett"""

from breezypythongui import EasyFrame
import sys
from tkinter import PhotoImage
"""Sets up the window and widgets."""
class Pizza(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self,title="Papa Hut Pizza",width=700,height=700)
        self.setBackground("#DC143C")
        self.addLabel("Choose Pizza Size --->", row=1, column=0,sticky="NSEW")
        
        #Adds an image at the top of the frame
        img = PhotoImage(file='./IMG/PizzaLogo.png')
        lbl = self.addLabel(text="",row=0,column=0,columnspan=3,sticky="NSEW",background="#DC143C")
        lbl.config(image=img)
        lbl.image = img
         # Create a menu bar
        self.menuBar = self.addMenuBar(row=1, column=1, columnspan=2,sticky="NSEW")
        self.sizeMenu = self.menuBar.addMenu("Pizza Size")

        # Add size options to the menu
        self.sizeMenu.addMenuItem("Small", command=lambda: self.setPizzaSize("Small"))
        self.sizeMenu.addMenuItem("Medium", command=lambda: self.setPizzaSize("Medium"))
        self.sizeMenu.addMenuItem("Large", command=lambda: self.setPizzaSize("Large")) 
       
       
         # Toppings options
        self.addLabel("Choose Toppings:", row=2, column=0,sticky="NSEW")
        self.pepperoniVar = self.addCheckbutton("Pepperoni", row=3, column=0)
        self.mushroomsVar = self.addCheckbutton("Mushrooms", row=3, column=1)
        self.bellPeppersVar = self.addCheckbutton("Bell Peppers", row=4, column=0)
        self.onionsVar = self.addCheckbutton("Onions", row=4, column=1)
        self.sausageVar = self.addCheckbutton("Sausage",row=3,column=2)
        self.bananaVar = self.addCheckbutton("Banana Pepper",row=4,column=2)
        
        # Order button
        self.addButton("Place Order", row=6, column=0,rowspan=5,columnspan=5,sticky="NSEW" ,command=self.showTotalWindow).config(bg="light green")

        # Initial pizza size
        self.selected_size = "Small"

    def setPizzaSize(self, size):
        # Set the selected pizza size
        self.selected_size = size

    def calculateCost(self):
        # Prices
        size_prices = {"Small": 8.99, "Medium": 11.99, "Large": 14.99}
        topping_price = 1.50  # per topping

        # Get selected size
        selected_size = self.selected_size

        # Calculate total cost based on size and toppings
        total_cost = size_prices[selected_size]
        total_cost += self.pepperoniVar.isChecked() * topping_price
        total_cost += self.mushroomsVar.isChecked() * topping_price
        total_cost += self.bellPeppersVar.isChecked() * topping_price
        total_cost += self.onionsVar.isChecked() * topping_price
        total_cost += self.sausageVar.isChecked() * topping_price
        total_cost += self.bananaVar.isChecked() * topping_price
        return total_cost

    def showTotalWindow(self):
        total_cost = self.calculateCost()

        
        # Create a new window for displaying the total
        total_window = TotalWindow(total_cost,self.exitApplication)
        total_window.mainloop()
    #Function for exit button
    def exitApplication(self):
        sys.exit()

#New window for total
class TotalWindow(EasyFrame):
    def __init__(self, total_cost,exit_callback):
        EasyFrame.__init__(self, title="Order Total")

        # Display the total cost
        self.addLabel("Total Cost:", row=0, column=0,sticky="NSEW")
        self.addLabel(f"${total_cost:.2f}", row=0, column=1,sticky="NSEW")
        #Adds exit button
        self.addButton("Exit", row=3, column=0, columnspan=2, command=exit_callback,sticky="NSEW").config(bg="red")
        #Adds image in total window
        img2 = PhotoImage(file='./IMG/ThankYou.png')
        lbl2 = self.addLabel(text="",row=1,column=1,sticky="NSEW")
        lbl2.config(image=img2)
        lbl2.image = img2






def main():
    Pizza().mainloop()

if __name__ =="__main__":
    main()      