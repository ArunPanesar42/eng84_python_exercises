# LEts make a fully functioning calculator

# Define functions for calculations
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


def area_of_circle(radius):
    return 3.1415 * radius * radius


def area_of_square(side):
    return side * side


def area_of_triangle(base, height):
    return height * base / 2


def ask_choice(max_num):
    while True:
        choice = input()
        if choice.isdigit():
            if int(choice) < max_num and int(choice) >= 0:
                return int(choice)
        print('Bad value. Try again: ')


def ask_number():
    while True:
        choice = input()
        if choice.isdigit():
            return int(choice)
        print('Bad value. Try again: ')


def ask_nonzero():
    while True:
        choice = input()
        if choice.isdigit():
            if int(choice) != 0:
                return int(choice)
        print('Bad value. Try again: ')


def ask_positive_number():
    while True:
        choice = input()
        if choice.isdigit():
            if int(choice) >= 0:
                return int(choice)
        print('Bad value. Try again: ')


def menu():
    print("Please choose an operation")
    print("""
            0. Addition
            1. Subtraction
            2. Multiplication
            3. Division
            4. Area of circle
            5. Area of square
            6. Area of triangle
            7. Exit
            """)


def calculator():
    while True:
        menu()
        choice = ask_choice(8)
        # Addition
        if choice == 0:
            print('First number?')
            x = ask_number()
            print('Second number?')
            y = ask_number()
            print(f'Result: {add(x, y)}')
        # Subtraction
        elif choice == 1:
            print('First number?')
            x = ask_number()
            print('Second number?')
            y = ask_number()
            print(f'Result: {subtract(x, y)}')
        # Multiplication
        elif choice == 2:
            print('First number?')
            x = ask_number()
            print('Second number?')
            y = ask_number()
            print(f'Result: {multiply(x, y)}')
        # Division
        elif choice == 3:
            print('First number?')
            x = ask_number()
            print('Second number?')
            y = ask_nonzero()
            print(f'Result: {divide(x, y)}')
        # Area of a circle
        elif choice == 4:
            print('Radius?')
            x = ask_positive_number()
            print(f'Result: {area_of_circle(x)}')
        # Area of a square
        elif choice == 5:
            print('Side length?')
            x = ask_positive_number()
            print(f'Result: {area_of_square(x)}')
        # Area of a triangle
        elif choice == 6:
            print('Height?')
            x = ask_positive_number()
            print('Base?')
            y = ask_positive_number()
            print(f'Result: {area_of_triangle(x, y)}')
        # Exit
        elif choice == 7:
            print('Goodbye')
            return
        else:
            print('Wrong input, try again')
        print('\n')


if __name__ == '__main__':
    calculator()
