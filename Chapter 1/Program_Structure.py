# Python Program Structure

# Imports at the top
import turtle

# Other function definitions followed by the main function definition
def main():
    # The main code of the program goes here
    t = turtle.Turtle()

# This code calls the main function to get everything started. The condition in this
# if statement evaluates to True when the module is executed by the interpreter, but
# not when it is imported into another module.
if __name__ == '__main__':
    main()

