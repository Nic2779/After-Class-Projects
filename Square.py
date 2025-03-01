import turtle

# Create a turtle screen
screen = turtle.Screen()

# Create a turtle named "square_turtle"
square_turtle = turtle.Turtle()

# Function to draw a square
def draw_square(side_length):
    for _ in range(4):
        square_turtle.forward(side_length)  # Move forward by the specified side length
        square_turtle.right(90)              # Turn right by 90 degrees

# Set the side length of the square
side_length = 100

# Draw the square
draw_square(side_length)

# Finish the drawing
turtle.done()