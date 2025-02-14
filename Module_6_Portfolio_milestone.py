class ItemToPurchase:
    def __init__(self, name = "", price = 0.0, quantity = 0,description = ""):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.description = description

    #method to get total cost
    def print_item_cost(self):
        print(self.name + " " + str(self.quantity) + " @ $" + str(self.price) + " = " + str(self.price * self.quantity))

class ShoppingCart:
    def __init__(self, customer_name = "none", current_date = "January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []
    #Methods
    def add_item(self, ItemToPurchase):
        self.cart_items.append(ItemToPurchase)
    
    def remove_item(self, itemName):
        if itemName in self.cart_items:
            self.cart_items.remove(itemName)
        else:
            print('Item not found in cart. Nothing removed.')
    
    def modify_item(self, ItemToPurchase):
        if ItemToPurchase in self.cart_items:
            if ItemToPurchase.name != "" and ItemToPurchase.price != 0.0 and ItemToPurchase.quantity != 0:
                ItemToPurchase.name = input('What would you like to modify the name of the item to?')
                ItemToPurchase.price = float(input('What would you like to modify the price to?'))
                ItemToPurchase.quantity = int(input('What would you like to modify the quantity to?'))
        else:
            print('Item not found in cart. Nothing modified.')
    
    def get_num_items_in_cart(self):
        return len(self.cart_items)

    def get_cost_of_cart(self):
        cost = 0.0
        for item in self.cart_items:
            cost = cost + item.price
        print('$'+str(cost))

    def print_total(self):
        if len(self.cart_items) == 0:
            print('SHOPPING CART IS EMPTY')
        else:
            print(f"{self.customer_name}'s shopping cart - {self.current_date}")
            print(f"Number of Items: {len(self.cart_items)}")
            total = 0.0
            for item in self.cart_items:
                print(f"{item.name} {item.quantity} @ ${item.price} = {(item.quantity * item.price)}")
                total = total + (item.quantity * item.price)
            print(f"Total: ${total}")
    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        if self.get_num_items_in_cart() > 0:
            for item in self.cart_items:
                print(f"{item.name}: {item.description}")
        else:
            print('SHOPPING CART IS EMPTY')

def print_menu(ShoppingCart,user,dateVar):
    enteredKey = ""
    while (enteredKey) != "q":
        print('MENU')
        print('a - Add item to cart')
        print('r - Remove item from cart')
        print('c - Change item quantity')
        print("i - Output items' descriptions")
        print('o - Output shopping cart')
        print('q - Quit')
        enteredKey = input('Choose an option:')
        if enteredKey == "a":
            nameToAdd = input("Which item would you like to add")
            for item in ShoppingCart.cart_items:
                if item.name == nameToAdd:
                    itemToAdd = item
                    ShoppingCart.add_item(itemToAdd)
                    break
        elif enteredKey == "r":
            nameToRemove = input("Which item would you like to remove")
            for item in ShoppingCart.cart_items:
                if item.name == nameToRemove:
                    itemToRemove = item
                    ShoppingCart.remove_item(itemToRemove)
                    break
        elif enteredKey == "c":
            itemToModify = input('What item would you like to modify?')
            ShoppingCart.modify_item(itemToModify)
        elif enteredKey == "i":
            ShoppingCart.print_descriptions()
        elif enteredKey == "o":
            ShoppingCart.print_total()
        elif enteredKey == "q":
            pass
        else:
            print('Please enter a valid input.')
        
    
    

def main():
    counter = 0
    totalCost = 0
    inputVar = ""
    itemStore = []
    while counter < 2:
        nameVar = str(input("Enter the item name"))
        priceVar = float(input("Enter the item price"))
        descVar = str(input("Enter the item description"))
        qtyVar = int(input("Enter the item quantity"))
        if counter == 0:
            item = ItemToPurchase(nameVar, priceVar, qtyVar, descVar)
            itemStore.append(item)
        else:
            item1 = ItemToPurchase(nameVar, priceVar, qtyVar, descVar)
            itemStore.append(item1)
        totalCost = totalCost + (priceVar * qtyVar)
        counter += 1
    
    userName = input('Enter your name.')
    cartDate = input('Enter the date.')
    myCart = ShoppingCart(userName, cartDate)
    for item in itemStore:
        item.print_item_cost()
        myCart.add_item(item)
    print("Total: $" + str(totalCost))
    print_menu(myCart, userName, cartDate)

main()  