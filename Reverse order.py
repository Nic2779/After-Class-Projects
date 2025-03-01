def count_digits(number):
    # Convert the number to string and get its length
    return len(str(abs(number)))

# Main program
try:
    user_input = input("Please enter a number: ")
    number = int(user_input)  # Convert input to integer
    total_digits = count_digits(number)
    print(f"The total number of digits in {number} is: {total_digits}")
except ValueError:
    print("Invalid input! Please enter a valid integer.")2