import math

def calculate_circumference(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    circumference = 2 * math.pi * radius
    return circumference

# Example usage:
if __name__ == "__main__":
    try:
        radius = float(input("Enter the radius of the circle: "))
        circumference = calculate_circumference(radius)
        print(f"The circumference of the circle with radius {radius} is: {circumference:.2f}")
    except ValueError as e:
        print(e)