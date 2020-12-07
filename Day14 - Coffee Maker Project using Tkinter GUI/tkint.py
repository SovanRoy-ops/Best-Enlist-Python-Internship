
from tkinter import *
import tkinter.messagebox as tmsg


class CoffeeMaker:
    water=1000
    milk=500               # intialised the ingridients
    coffee=300
    money=0

    def __init__(self,value):      # value of drink given by user
        self.value=value


    def report(self,value):            # displays current value of the ingridients in the machine
        s = f"Water :{self.water}ml\nMilk: {self.milk}ml\nCoffee: {self.coffee}g\nMoney: ${self.money}"
        return s

    def makeCoffee(self,value):    # this method makes the desired drink by calculating the available resources in the machine and also checks whether sufficient resources are present for making the coffee
        if(value=="latte"):
            self.water=self.water-50
            self.milk=self.milk-70
            self.coffee=self.coffee-50
            self.money=self.money+2.50
            print("Here is your latte. Enjoy!")

        elif(value=="espresso"):
            self.water=self.water-100
            self.milk=self.milk-10
            self.coffee=self.coffee-100
            self.money=self.money+3.50
            print("Here is your espresso. Enjoy!")

        else:
            self.water=self.water-70
            self.milk=self.milk-50
            self.coffee=self.coffee-70
            self.money=self.money+4.50
            print("Here is your cappucino. Enjoy!")


    def transaction(self,value,amount):  # this method calculates and makes the transaction of the drink and checks whether the user can buy the drink or not
        if(value=="latte"):
            if(amount<2.50):
                print("Sorry that's not enough money. Money refunded.")
            elif(amount>2.50):
                print("Here is $",round(amount-2.50,2),"dollars in change.")
                self.makeCoffee(value)
            else:
                self.makeCoffee(value)

        elif(value=="espresso"):
            if(amount<3.50):
                print("Sorry that's not enough money. Money refunded.")
            elif(amount>3.50):
                print("Here is $",round(amount-3.50,2),"dollars in change.")
                self.makeCoffee(value)
            else:
               self.makeCoffee(value)

        else:
            if(amount<4.50):
                print("Sorry that's not enough money. Money refunded.")
            elif(amount>4.50):
                print("Here is $",round(amount-4.50,2),"dollars in change.")
                self.makeCoffee(value)
            else:
                self.makeCoffee(value)


    def coinValueConversion(self,value):   # This method calculates the total amount based on the coin corrency values and gives the result
        quarters=0.25
        dimes=0.10
        nickles=0.05
        pennies=0.01
        print("Insert coins!")
        q=int(input("Enter number of quarters:"))
        d=int(input("Enter number of dimes:"))
        n=int(input("Enter number of nickles:"))
        p=int(input("Enter number of pennies:"))
        amount=(q*quarters)+(d*dimes)+(n*nickles)+(p*pennies)
        self.transaction(value,amount)


    def resources(self,value):   # this method checks the availability of the resources or ingredients required for making the user's drink
        if(value=="latte"):
            if(self.water<50):
                print("Sorry there is not enough water!")
            elif(self.milk<70):
                print("Sorry there is not enough milk!")
            elif(self.coffee<50):
                print("Sorry there is not enough coffee!")
            else:
                self.coinValueConversion(value)
        elif(value=="espresso"):
            if(self.water<100):
                print("Sorry there is not enough water!")
            elif(self.milk<10):
                print("Sorry there is not enough milk!")
            elif(self.coffee<100):
                print("Sorry there is not enough coffee!")
            else:
                self.coinValueConversion(value)
        else:
            if(self.water<70):
                print("Sorry there is not enough water!")
            elif(self.milk<50):
                print("Sorry there is not enough milk!")
            elif(self.coffee<70):
                print("Sorry there is not enough coffee!")
            else:
                self.coinValueConversion(value)
       
    
machineValue="on"                     # this variable determines the current state of the machine
c=CoffeeMaker(machineValue)          # object of the Coffee Maker is created

while(True):    # this loop controls the display menu and overall flow of operations of the machine

    root = Tk()
    root.geometry("455x233")
    root.minsize(400,200)
    root.title("SUPER COFFEE MAKER")
    

    def order():

        tmsg.showinfo("Order Received!", f"We have received your order for {var.get()}. Thanks for ordering")

    def rep():
        tmsg.showinfo("Report",c.report(machineValue))
        

    var = StringVar()
    var.set("Radio")

    Label(root, text = "What would you like to have sir?",font="lucida 19 bold",justify=LEFT).pack()

    radio1 = Radiobutton(root, text="Latte: $2.50", padx=14, variable=var, value="Latte").pack(anchor="w")
    radio2 = Radiobutton(root, text="Espresso: $3.50", padx=14, variable=var, value="Espresso").pack(anchor="w")
    radio3 = Radiobutton(root, text="Cappucino: $4.50", padx=14, variable=var, value="Capuccino").pack(anchor="w")

    
    Button(text="Order Now", command=order).pack(padx = 10, pady = 10)
    Button(text="Show Report", command=rep).pack(side=LEFT, padx=23)
    root.mainloop()

    print("\n\nWELCOME TO THE SUPER COFFEE EXPRESS!!!\n\nLatte:$2.50\nEspresso:$3.50\nCappucino:$4.50")
    machineValue= var.get()

    if(machineValue=="off"):     # admins have special code("off") to turn of the machine 
        break
    
    if(machineValue=="report"):  # using the code "report" gives the current quantity of the ingredients available in the machine
        c.report(machineValue)
        continue

    c.resources(machineValue)   

