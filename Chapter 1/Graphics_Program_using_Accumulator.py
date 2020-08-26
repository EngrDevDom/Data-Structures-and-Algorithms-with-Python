# A Graphics Program using Accumulator Pattern

import turtle

# Command classes would be inserted here but are left out because they
# were defined earlier in the chapter.
# This is our PyList class. It holds a list of our graphics
# commands.

class Pylist:

    def __init__(self):
        self.items = []

    def append(self, item):
        self.items = self.items + [item]

    # if we want to iterate over this sequence, we define the special method
    # called __iter__(self). Without this we’ll get "builtins.TypeError:
    # ’PyList’ object is not iterable" if we try to write
    # for cmd in seq:
    # where seq is one of these sequences. The yield below will yield an
    # element of the sequence and will suspend the execution of the for
    # loop in the method below until the next element is needed. The ability
    # to yield each element of the sequence as needed is called "lazy" evaluation
    # and is very powerful. It means that we only need to provide access to as
    # many of elements of the sequence as are necessary and no more.
    def __iter__(self):
        for c in self.items:
            yield c

def main():
    filename = input("Please enter drawing filename: ")

    t = turtle.Turtle()
    screen = t.getscreen()
    file = open(filename, "r")

    # Create a PyList to hold the graphics commands that are
    # read from the file.
    graphicsCommands = Pylist()

    command = file.readline().strip()

    while command != "":
        # Now we must read the rest of the record and then process it. Because
        # records are variable length, we’ll use an if-elif to determine which
        # type of record it is and then we’ll read and process the record.
        # In this program, processing the record means creating a command object
        # using one of the classes above and then adding that object to our
        # graphicsCommands PyList object.
        if command == "goto":
            x = float(file.readline())
            y = float(file.readline())
            width = float(file.readline())
            color = file.readline().strip()
            cmd = GoToCommand(x, y, width, color)

        elif command == "circle":
            radius = float(file.readline())
            width = float(file.readline())
            color = file.readline().strip()
            cmd = CircleCommand(radius, width, color)

        elif command == "beginfill":
            color = file.readline().strip()
            cmd = BeginFillCommand(color)

        elif command == "endfill":
            cmd = EndFillCommand()

        elif command == "penup":
            cmd = PenUpCommand()

        elif command == "pendown":
            cmd = PenDownCommand()

        else:
            # raising an exception will terminate the program immediately
            # which is what we want to happen if we encounter an unknown
            # command. The RuntimeError exception is a common exception
            # to raise. The string will be printed when the exception is
            # printed.
            raise RuntimeError("Unknown Command: " + command)

        # Finish processing the record by adding the command to the sequence,
        graphicsCommands.append(cmd)

        # Read one more line to set up for the next time through the loop.
        command = file.readline().strip()

    # This code iterates through the commands to do the drawing and
    # demonstrates the use of the __iter(self)__ method in the
    # PyList class above.
    for cmd in graphicsCommands:
        cmd.draw(t)

    file.close()
    t.ht()
    screen.exitonclick()
    print("Program Execution Completed.")

if __name__ == '__main__':
    main()

