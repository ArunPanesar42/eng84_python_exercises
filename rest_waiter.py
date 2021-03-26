# Lists - Restaurant Waiter Helper program

# Make a menu that is stored as a dictionary to have the food items and the cost
restaurantMenu = [
    {'item': 'Chicken Salad', 'category': 'main', 'price': 10.00},
    {'item': 'Steak', 'category': 'main', 'price': 16.00},
    {'item': 'Wings', 'category': 'side', 'price': 6.00},
    {'item': 'Chips', 'category': 'side', 'price': 4.00},
    {'item': 'Cola', 'category': 'drink', 'price': 2.00},
    {'item': 'Water', 'category': 'drink', 'price': 0.00},
]


# Function that will print the menu for the customer to see
def menu():
    print('Please choose an item by selection the number:')
    for idx, item in enumerate(restaurantMenu):
        print(f"\t{idx}. {item.get('item')}, ({item.get('category')}  £{item.get('price')})")


# Function that asks for input that is a digit and within a range
def ask_number(max_num):
    while True:
        choice = input()
        if choice.isdigit():
            if max_num > int(choice) >= 0:
                return int(choice)
        print('Bad value. Try again: ')


# Function that acts as main program
def main():
    # list to store choices
    choices = []
    # var to store the total cost of order (initialise to zero)
    total = 0
    # Only 3 choices allowed
    num_choices = 3

    # Ask for customer choices
    for i in range(num_choices):
        menu()
        print(f'Choose item {i + 1}:  ')
        # Append choice to list
        choices.append(ask_number(len(restaurantMenu)))
        # Add price to total
        total += restaurantMenu[choices[-1]].get('price')

    # Print order
    print(f'Here is what you ordered:')
    for idx, choice in enumerate(choices):
        print(f"  Item {idx}: {restaurantMenu[choice].get('item')} for ${restaurantMenu[choice].get('price')}")
    print('Total: {}'.format(total))


if __name__ == '__main__':
    main()
