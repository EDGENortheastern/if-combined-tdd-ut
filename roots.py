def sq_num(n):
    """Return the square root of a given number."""
    return n**0.5

while True:
    user_input = input("Enter a positive number: ")
    try:
        number = float(user_input)  # ensure the input can be turned into a number
        if number >= 0:
            break
        else:
            print("Please enter zero or more.")
    except ValueError:
        print("Please enter a valid number.")

print("The square root is:", sq_num(number))
