# The GoToCommand with XML Creation Code

# The following classes define the different commands that
# are supported by the drawing application.
class GoToCommand:
    def __init__(self, x, y, width=1, color="black"):
        self.x = x
        self.y = y
        self.width = width
        self.color = color

    # The draw method for each command draws the command
    # using the given turtle
    def draw(self, turtle):
        turtle.width(self.width)
        turtle.pencolor(self.color)
        turtle.goto(self.x, self.y)

    # The __str__ method is a special method that is called
    # when a command is converted to a string. The string
    # version of the command is how it appears in the graphics
    # file format.
    def __str__(self):
        return '<Command x="' + str(self.x) + '" y="' + str(self.y) + '" width="' + str(self.width) + '" color="' + self.color + '">GoTo</Command>"'

