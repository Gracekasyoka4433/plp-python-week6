def get_number():
    try:
        number = int(input("Enter a whole number: "))
        return number
    except ValueError:
        print("Not a valid number.")
        return None


number = get_number()

if number is not None:
    print(f"You entered: {number}")
else:
    print("The program is still running safely.")