from prettytable import PrettyTable
table = PrettyTable(['Item Name', 'Item Price'])
totalAmount = 0
flavor = ["Classic", "Hazelnut", "Almond", "Caramel macchiatto"]
price = [50, 60, 70, 80]
orderedFlavor = []
orderedPrice = []


def mainProgram():
    order = input("Enter your order here: ")
    while True:
        if order == "a":
            orderedFlavor.append(flavor[0])
            orderedPrice.append(price[0])
            receipt()
        elif order == "b":
            orderedFlavor.append(flavor[1])
            orderedPrice.append(price[1])
            receipt()
        elif order == "c":
            orderedFlavor.append(flavor[2])
            orderedPrice.append(price[2])
            receipt()
        elif order == "d":
            orderedFlavor.append(flavor[3])
            orderedPrice.append(price[3])
            receipt()
        else:
            print("Not in the MENU!")
            mainProgram()


def receipt():
    global totalAmount, orderedPrice
    while True:
        checkout = input("Check out? [y/n]: ")
        if checkout is 'y':
            itemName = ('\n'.join(orderedFlavor))
            itemPrice = map(str, orderedPrice)
            itemPrice = ('\n'.join(itemPrice))
            table.add_row([itemName, itemPrice])
            totalAmount = sum(orderedPrice)
            table.add_row(["TOTAL", totalAmount])
            print(table)
            print('\nThanks for shopping with us :)')
            print('Your total bill amount is ', totalAmount, '/-')
            exit()
        else:
            mainProgram()


print(""" 
+-----------------------------------------+
|                                         |
|           WELCOME TO KOFF-IE            |
|                 by ken                  |
+-----------------------------------------+
|           AVAILABLE COFFEES             |
+-----------------------------------------+
|         FLAVOR         |     PRICE      |
+-----------------------------------------+
| [a] CLASSIC            |       50       |
| [b] HAZELNUT           |       60       |
| [c] ALMOND             |       70       |
| [d] CARAMEL MACCHIATTO |       80       |
+-----------------------------------------+
""")
mainProgram()
