import tkinter as tk
from tkinter import ttk

class Weapon:
    def __init__(self, name, damage, capacity, price):
        self.name = name
        self.damage = damage
        self.capacity = capacity
        self.price = price

class BuyingSystem:
    def __init__(self):
        self.products = {
            'Bow': Weapon('Bow', 20, 1, 50),
            'Crossbow': Weapon('Crossbow', 30, 1, 80),
            'Sword': Weapon('Sword', 40, 1, 100),
            'Knife': Weapon('Knife', 10, 1, 20)
        }

    def buy_weapon(self, weapon_name, quantity):
        if weapon_name in self.products:
            weapon = self.products[weapon_name]
            total_price = weapon.price * quantity

            result_text.set(f"You are buying {quantity} {weapon_name}(s) with total damage {quantity * weapon.damage}.\nTotal Price: {total_price} gold coins.")
            
            # Display additional labels
            class_label.config(text=f"Class: {weapon_name}")
            amount_label.config(text=f"Amount: {quantity}")
        else:
            result_text.set(f"Sorry, {weapon_name} is not available in our store.")

# Function to handle the buy button click
def buy_button_click():
    weapon_name = weapon_combobox.get()
    quantity = quantity_entry.get()

    try:
        quantity = int(quantity)
        if quantity > 0:
            buying_system.buy_weapon(weapon_name, quantity)
        else:
            result_text.set("Invalid quantity. Please enter a positive integer.")
    except ValueError:
        result_text.set("Invalid input. Please enter a valid quantity.")

# Create Tkinter window
root = tk.Tk()
root.title("Medieval Weapons Store")

# Create BuyingSystem instance
buying_system = BuyingSystem()

# Label for displaying available products
product_label = ttk.Label(root, text="Available Products:")
product_label.grid(row=0, column=0, columnspan=2, pady=10)

# Labels for additional information during buying
class_label = ttk.Label(root, text="Class: ")
class_label.grid(row=1, column=0, pady=5)

amount_label = ttk.Label(root, text="Amount: ")
amount_label.grid(row=1, column=1, pady=5)

# Combobox for weapon selection
weapon_combobox = ttk.Combobox(root, values=list(buying_system.products.keys()), state="readonly")
weapon_combobox.grid(row=2, column=0, pady=5)

# Entry for entering the quantity
quantity_entry = ttk.Entry(root)
quantity_entry.grid(row=2, column=1, pady=5)

# Button for buying
buy_button = ttk.Button(root, text="Buy", command=buy_button_click)
buy_button.grid(row=3, column=0, columnspan=2, pady=10)

# Label for displaying the result
result_text = tk.StringVar()
result_label = ttk.Label(root, textvariable=result_text)
result_label.grid(row=4, column=0, columnspan=2, pady=10)

# Run the Tkinter event loop
root.mainloop()
