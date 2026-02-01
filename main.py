print("Welcome to our Cafe!")
print("We are happy to serve you!")
print("-" * 40)
# Main menu with prices
menu = {
    "coffee": 60,
    "tea": 40,
    "burger": 80,
    "pizza": 150,
    "sandwich": 70
}

# Star items with reviews
star_items = {
    "coffee": {"price": 60, "review": "Best seller (4.8/5)"},
    "pizza": {"price": 150, "review": "Customer favorite  (4.7/5)"}
}

# Today's specials
special_items = {
    "cold coffee": {"price": 90, "review": "Limited offer"},
    "combo meal": {"price": 200, "review": "Chef recommendation"}
}
#To validate the order of the user
master_menu = {}

# add main menu
master_menu.update(menu)

# add star items
for item, details in star_items.items():
    master_menu[item] = details["price"]

# add specials
for item, details in special_items.items():
    master_menu[item] = details["price"]

print("\nWhat would you like to see?")
print("1. Full Menu")
print("2. Star Items ")
print("3. Today's Specials ")

choice = input("Enter your choice (1/2/3): ")
if choice == "1":
    print("\n--- Full Menu ---")
    for item, price in menu.items():
        print(f"{item.title()} : ₹{price}")

elif choice == "2":
    print("\n--- Star Items ---")
    for item, details in star_items.items():
        print(f"{item.title()} : ₹{details['price']} | {details['review']}")

elif choice == "3":
    print("\n--- Today's Specials ---")
    for item, details in special_items.items():
        print(f"{item.title()} : ₹{details['price']} | {details['review']}")

else:
    print("Invalid choice. Please restart program.")
ordered_items = []
total_cost = 0
item_count = 0
while True:
    item = input("\nEnter item to place order: ").lower()

    if item in master_menu:
        qty = int(input(f"Enter quantity for {item}: "))

        ordered_items.append((item, qty))
        total_cost += master_menu[item] * qty
        item_count += qty

        print(f"{qty} x {item.title()} added to your order!")
    else:
        print("Sorry, item not available.")

    more = input("Do you want to order anything else? (yes/no): ").lower()

    if more == "no":
        break
# Customer discount
print("\nAre you a new or regular customer?")
customer_type = input("Enter 'new' or 'regular': ").lower()

discount = 0

if customer_type == "new":
    discount = total_cost * 0.05
    print("New customer discount applied (5%)")

elif customer_type == "regular":
    discount = total_cost * 0.10
    print("Regular customer discount applied (10%)")

total_after_discount = total_cost - discount

# Coupon logic
coupon_discount = 0

if item_count > 15:
    coupon_discount = total_after_discount * 0.05
    print(" Coupon applied! Extra 5% off!")

final_total = total_after_discount - coupon_discount
print(final_total)
print("\nWe value your feedback!")

rating = input("Rate your experience (1-5): ")
review = input("Write your review: ")

with open("reviews.txt", "a") as file:
    file.write(f"Rating: {rating} | Review: {review}\n")

print("Thank you for your review! ")




