def decimal_to_binary(decimal_number):
    if decimal_number < 0:
        return "Negative numbers are not supported."
    elif decimal_number == 0:
        return "0"

    binary_number = ""
    
    while decimal_number > 0:
        remainder = decimal_number % 2
        binary_number = str(remainder) + binary_number
        decimal_number //= 2  # Use floor division to get the quotient

    return binary_number

# Input from user
try:
    decimal_input = int(input("Enter a decimal number: "))
    binary_output = decimal_to_binary(decimal_input)
    print(f"The binary representation is: {binary_output}")
except ValueError:
    print("Please enter a valid decimal integer.")