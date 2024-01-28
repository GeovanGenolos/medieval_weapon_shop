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

    def display_products(self):
        print("Available Products:")
        for product in self.products.values():
            print(f"{product.name} - Damage: {product.damage} | Capacity: {product.capacity} | Price: {product.price}")

    def buy_weapon(self, weapon_name, quantity):
        if weapon_name in self.products:
            weapon = self.products[weapon_name]
            total_price = weapon.price * quantity

            print(f"\nYou are buying {quantity} {weapon_name}(s) with total damage {quantity * weapon.damage}.")
            print(f"Total Price: {total_price} gold coins.")
        else:
            print(f"\nSorry, {weapon_name} is not available in our store.")

# Main program
if __name__ == "__main__":
    buying_system = BuyingSystem()

    print("Welcome to the Medieval Weapons Store!")
    buying_system.display_products()

    while True:
        user_choice = input("\nEnter the name of the weapon you want to buy (or 'exit' to quit): ")
        
        if user_choice.lower() == 'exit':
            print("Thank you for shopping with us!")
            break

        if user_choice in buying_system.products:
            quantity = int(input(f"How many {user_choice}s would you like to buy? "))
            buying_system.buy_weapon(user_choice, quantity)
        else:
            print("Invalid choice. Please select a valid weapon from the list.")
