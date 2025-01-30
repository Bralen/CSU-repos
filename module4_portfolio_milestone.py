class ItemToPurchase:
    def __init__(self, name = "", price = 0.0, quantity = 0):
        self.name = name
        self.price = price
        self.quantity = quantity

    #method to get total cost
    def print_item_cost(self):
        print(self.name + " " + str(self.quantity) + " @ $" + str(self.price) + " = " + str(self.price * self.quantity))

def main():
    counter = 0
    itemList = []
    while counter < 2:   
        nameVar = str(input("Enter the item name"))
        priceVar = float(input("Enter the item price"))
        qtyVar = int(input("Enter the item quantity"))
        if counter == 0:
            item1 = ItemToPurchase(nameVar, priceVar, qtyVar)
            itemList.append(item1)
        else:
             item2 = ItemToPurchase(nameVar, priceVar, qtyVar)
             itemList.append(item2)
        counter += 1
    totalCost = 0
    for item in itemList:
        item.print_item_cost()
        totalCost = totalCost + (item.quantity * item.price)
    print("Total: $" + str(totalCost))

    #print("Total: $" + str((item1.quantity * item1.price) + (item2.quantity * item2.price)))

main()

