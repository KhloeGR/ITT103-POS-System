#Authors : Khloe Griffiths, Akayla Stewart, Halla Henry
#Date: April 14, 2026
#Programming Techniques ITT103
#Github: https://github.com/KhloeGR/ITT103-POS-System

#Best Buy Retail Store Point Of Sale System(POS)

products = {
    "Digicel Phone Card": {"price": 125, "stock": 200},
    "Flow Phone Card":    {"price": 125, "stock": 120},
    "Rice":               {"price": 80, "stock": 100},
    "Flour":              {"price": 75, "stock": 100},
    "Sugar":              {"price": 85, "stock": 120},
    "Matches":            {"price": 35, "stock": 25},
    "Oil":                {"price": 170, "stock": 30},
    "Chicken Back":       {"price": 160, "stock": 50},
    "Salt":               {"price": 65, "stock": 60},
    "Tissue":             {"price": 90, "stock": 105},
    "Washing Soap":       {"price": 115, "stock": 300},  
    "Butter":             {"price": 140, "stock": 10},
    "Cal's Bag Juice":    {"price": 35, "stock": 200},
    "Dishwashing Liquid": {"price": 140, "stock": 20}
}

cart = {}

TAX= 0.10
DISCOUNT = 0.05

def show_products():
    print("\n-------- Product List --------")
    print(f"{'Name':<22} {'Price':>8} {'Stock':>8}")
    print("-" *50)
    for name in products:
        p = products [name]
        if p["stock"] <5:
            print(f"{name:<22} ${p['price']:>7} {p['stock']:>7} LOW STOCK")
        else:
            print(f"{name:<22} ${p['price']:>7} {p['stock']:>7}")
    print("-" * 40)

def show_cart():
    if len(cart) == 0:
        print("\nNo Items in cart.")
        return
    print("\n-------- Shopping Cart --------")
    print(f"{'Item':<22} {'Qty':>5} {'Unit Price':>10} {'Total':>10}")
    print("-" * 50)
    for item in cart:
        qty = cart[item]["qty"]
        price = cart[item]["price"]
        total = qty * price
        print(f"{item:<22} {qty:>5} ${price:>9} ${total:>9}")
    print("-" * 50)

def add_item():
    show_products()
    name = input("\nEnter product name: ").title()

    if name not in products:
        print("Item not found.")
        return

    try:
        qty = int(input("Enter quantity: "))
    except ValueError:
        print("Enter a valid number.")
        return

    if qty <= 0:
        print("Quantity must be at least 1.")
        return

    if qty > products[name]["stock"]:
        print("Not enough stock. Only " + str(products[name]["stock"]) + " remaining.")
        return

    if name in cart:
        cart[name]["qty"] += qty
    else:
        cart[name] = {"qty": qty, "price": products[name]["price"]}

    products[name]["stock"] -= qty
    print(qty, "x", name, "added to cart.")

def remove_item():
    if len(cart) == 0:
        print("Cart is empty.")
        return

    show_cart()
    name = input("\nEnter product name to remove: ").title()

    if name not in cart:
        print("That item is not in the cart.")
        return

    products[name]["stock"] += cart[name]["qty"]
    del cart[name]
    print(name + " removed from cart.")

def checkout():
    if len(cart) == 0:
        print("Cart is empty. Nothing to checkout.")
        return

    subtotal = 0
    for item in cart:
        subtotal += cart[item]["qty"] * cart[item]["price"]

    discount = 0
    if subtotal > 5000:
        discount = subtotal * DISCOUNT
        print("5% discount applied!")

    after_discount = subtotal - discount
    tax = after_discount * TAX
    total = after_discount + tax

    print("\n-------- Checkout --------")
    print("Subtotal:  $" + str(round(subtotal, 2)))
    if discount > 0:
        print("Discount:  $" + str(round(discount, 2)))
    print("Tax (10%): $" + str(round(tax, 2)))
    print("Total:     $" + str(round(total, 2)))
    print("-" * 26)

    while True:
        try:
            paid = float(input("Amount paid: $"))
        except ValueError:
            print("Enter a valid amount.")
            continue
        if paid < total:
            print("Not enough. Total is $" + str(round(total, 2)))
        else:
            break

    change = paid - total
    print("Change:    $" + str(round(change, 2)))
    print_receipt(subtotal, discount, tax, total, paid, change)
    cart.clear()
    print("\nCheckout complete!")

def print_receipt(subtotal, discount, tax, total, paid, change):
    print("\n")
    print("=" * 40)
    print("     Best Buy Retail Store")
    print("     Group 14")
    print("       Kingston, Jamaica")
    print("=" * 40)
    print(f"{'Item':<20} {'Qty':>4} {'Price':>7} {'Total':>7}")
    print("-" * 40)
    for item in cart:
        qty = cart[item]["qty"]
        price = cart[item]["price"]
        line = qty * price
        print(f"{item:<20} {qty:>4} ${price:>6} ${line:>6}")
    print("-" * 40)
    print("Subtotal:        $" + str(round(subtotal, 2)))
    if discount > 0:
        print("Discount (5%):  -$" + str(round(discount, 2)))
    print("Tax (10%):        $" + str(round(tax, 2)))
    print("Total:            $" + str(round(total, 2)))
    print("Amount Paid:      $" + str(round(paid, 2)))
    print("Change:           $" + str(round(change, 2)))
    print("=" * 40)
    print("    Thank you for shopping with us!")
    print("         Please come again!")
    print("=" * 40)

def main():
    print("\nWelcome to Best Buy Retail Store")
    print("Group 14")
    while True:
        print("\n-------- Main Menu --------")
        print("1. View Products")
        print("2. Add Item to Cart")
        print("3. Remove Item from Cart")
        print("4. View Cart")
        print("5. Checkout")
        print("6. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            show_products()
        elif choice == "2":
            add_item()
        elif choice == "3":
            remove_item()
        elif choice == "4":
            show_cart()
        elif choice == "5":
            checkout()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

main()



    
                
