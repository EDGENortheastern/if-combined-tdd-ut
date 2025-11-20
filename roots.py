def sq_num(n):
    """Return the square root of a given number."""
    return n**0.5

if __name__ == "__main__":
    user_input = input("Enter a positive number: ")
    print("The square root is:", sq_num(int(user_input)))
