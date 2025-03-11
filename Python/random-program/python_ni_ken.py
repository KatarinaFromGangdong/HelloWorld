coffee =["Classic", "Hazelnut", "Almond", "Caramel Machiatto"]
prices = [50,50,50,50]

myOrderCoffee=[]
myOrderCost=[]
counter=0 

print ("Welcome to KOFF-IE")

order = input("Can i take your order?")
if order =="No":
    exit()
else:
    print ("Thank you")
    
nextOrder = True   

while nextOrder==True:
    coffeeOrder = input("Please enter coffee")
    if coffeeOrder == ("Classic"):
       myOrderCoffee.append(coffee[0])
       myOrderCost.append(prices[0])
       Counter=counter+1 
    
    elif coffeeOrder == ("Hazelnut"):
       myOrderCoffee.append(coffee[1])
       myOrderCost.append(prices[1])
       Counter=counter+1 
    
    elif coffeeOrder == ("Almond"):
       myOrderCoffee.append(coffee[2])
       myOrderCost.append(prices[2])   
       Counter=counter+1 
    
    elif coffeeOrder == ("Caramel Machiatto"):
       myOrderCoffee.append(coffee[3])
       myOrderCost.append(prices[3])  
       Counter=counter+1 
       
    else:
        print ("Not on Menu")
    finished = input("Have you finished ordering")
    if finished == ("N"):
      nextOrder=True
    else:
        nextOrder = False

y=0 
while y <counter:
    print ("Here is your order")
print ("    ")
print ("******")
print (myOrderCoffee[y])
print(Counter)