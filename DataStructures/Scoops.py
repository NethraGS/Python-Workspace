# Tuple – Fixed menu (cannot be changed)
MENU = ("Vanilla", "Chocolate", "Strawberry")

# Dictionary – Price list
PRICE = {
    "Vanilla": 50,
    "Chocolate": 60,
    "Strawberry": 55
}

# Frozenset – Allowed serving types (STRICT RULE)
SERVING_TYPES = frozenset(["cone", "cup"])

toppings = {"choco_chips", "nuts", "sprinkles"}

# List – Order history
orders = []


def place_order(flavor, serving, toppings):
    """Places an ice cream order"""

    if flavor not in MENU:
        print("Flavor not available")
        return

    if serving not in SERVING_TYPES:
        print("Invalid serving type. Choose cone or cup.")
        return

    order = {
        "flavor": flavor,
        "serving": serving,
        "toppings": toppings
    }

    orders.append(order)
    print("Order placed successfully!")


def show_orders():
    """Displays all orders"""
    print("\n--- Order Summary ---")
    for order in orders:
        print(order)


def calculate_bill():
    """Calculates total bill"""
    total = 0
    for order in orders:
        total += PRICE[order["flavor"]]
    print("\nTotal Bill: ₹", total)

while True:
    print("\nAvailable Flavors:", MENU)

    flavor = input("Enter flavor: ").title()
    serving = input("Enter serving (cone/cup): ").lower()

    toppings_input = input("Enter toppings (comma separated): ")
    toppings = set(t.strip().lower() for t in toppings_input.split(","))  

    place_order(flavor, serving, toppings)

    choice = input("Do you want to place another order? (yes/no): ").lower()
    if choice != "yes":
        break

show_orders()
calculate_bill()
