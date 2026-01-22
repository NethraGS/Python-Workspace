class Food:
    def __init__(self,food_id,name,category,price):
        self.food_id=food_id
        self.name=name
        self.category=category
        self.price=price

    def __str__(self):
        return f"{self.food_id}.{self.name} ({self.category})-{self.price:}"

class Outlet:
    def __init__(self,outlet_id,name):
        self.outlet_id=outlet_id
        self.name=name
        self.menu=[]

    def add_food(self,food):
        self.menu.append(food)

    def show_menu(self):
        print(f"\nMenu for {self.name}(Outlet ID:{self.outlet_id})")
        for i in self.menu:
            print(i)

    def get_food_by_id(self,food_id):
        for food in self.menu:
            if food.food_id==food_id:
                return food
        return None


class Cart:
    def __init__(self):
        self.items={}

    def add_item(self,food,quantity):
        if food in self.items:
            self.items[food]+=quantity
        else:
            self.items[food]=quantity
        print(f"Added {quantity} {food.name} to cart.")

    def view_cart(self):
        if not self.items:
            print("\nCart is empty.")
            return
        print("\nYour cart ")
        total=0
        for food,q in self.items.items():
            subtotal=food.price*q
            total+=subtotal
            print(f"{food.name} {q}=Rs.{subtotal}")
        print(f"Total Bill:Rs.{total}")
    
    def remove_item(self,food,quantity):
        if food not in self.items:
            print("Item not found in cart")
            return

        if quantity>=self.items[food]:
            del self.items[food]
            print(f"{food.name} removed from cart")
        else:
            self.items[food]-=quantity
            print(f"Removed {quantity} {food.name} from cart")

    def checkout(self):
        if not self.items:
            print("\nCart is empty.")
            return
        total = sum(food.price*qty for food,qty in self.items.items())
        print("\nOrder placed successfully")
        print("Bill")
        for food, qty in self.items.items():
            print(f"{food.name}{qty} = {food.price*qty:}")
        print(f"Total Amount:Rs.{total}")
        self.items.clear() 


def main():
    outlet = Outlet(1,"Pizza Hut")
    outlet.add_food(Food(101, "Margherita Pizza","Veg Pizza",800))
    outlet.add_food(Food(102, "Pepperoni Pizza","Non-veg Pizza",100))
    outlet.add_food(Food(103, "Veggie Pizza","Veg Pizza",900))
    outlet.add_food(Food(104, "Chicken Wings","Starters",500))
    outlet.add_food(Food(105, "Coke","Beverages",109))
    cart = Cart()

    while True:
        print("\nPIZZA HUT FOOD APP")
        print("1.Show Menu")
        print("2.Add Item to Cart")
        print("3.Remove Item from Cart")
        print("4.View Cart")
        print("5.Place Order")
        print("6.Exit")

        choice = input("Enter your choice: ")
        if choice=="1":
            outlet.show_menu()
        elif choice=="2":
            outlet.show_menu()
            food_id=int(input("Enter food ID to add to cart:"))
            quantity=int(input("Enter quantity:"))
            food_item=next((f for f in outlet.menu if f.food_id==food_id),None)
            if food_item:
                cart.add_item(food_item,quantity)
            else:
                print("Invalid ID")
        elif choice=="3":
            cart.view_cart()
            food_id = int(input("Enter Food ID to remove:"))
            qty=int(input("Enter quantity to remove: "))
            food = outlet.get_food_by_id(food_id)
            if food:
                cart.remove_item(food, qty)
            else:
                print("Invalid Food ID")
        elif choice=="4":
            cart.view_cart()
        elif choice=="5":
            cart.checkout()
        elif choice=="6":
            print("Thank you for visiting Pizza Hut!")
            break
        else:
            print("Invalid choice")

main()

                