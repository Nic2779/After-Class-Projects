def print_mirrored_triangle(rows):
    for i in range(1, rows + 1):
        # Print spaces for left alignment
        print(" " * (rows - i), end="")
        # Print stars
        print("* " * i)

# Get the number of rows from the user
n = int(input("Enter the number of rows for the mirrored right-angled triangle: "))
print_mirrored_triangle(n)