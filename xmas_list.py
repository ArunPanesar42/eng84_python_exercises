
xmas_list = []  # Makes the list

print("What would you like this Christmas? (write 'exit' to stop program)")

while True:                 # Create infinite loop
    wish = input()      # Gets the users input
    if wish.lower() == 'exit':      # Check if input was 'exit' without case sensitivity
        break   # if input was exit, it breaks the loop ending the program

    xmas_list.add(wish)     # add the item to list
    # Ask for new item
    print("Noted. What else?")

print("\n\nWhat i need to buy:")
# Print full list
for idx, item in enumerate(xmas_list):
    print(f"  {idx+1}. {item.upper()}")