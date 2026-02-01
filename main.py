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
