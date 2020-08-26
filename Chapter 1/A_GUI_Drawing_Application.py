# A GUI Drawing Application

# This class defines the drawing application. The following line says that
# the DrawingApplication class inherits from the Frame class. This means
# that a DrawingApplication is like a Frame object except for the code
# written here which redefines/extends the behavior of a Frame.

class DrawingApplication(tkinter.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.buildWindow()
        self.graphicsCommands = PyList()

    # This method is called to create all the widgets, place them in the GUI,
    # and define the event handlers for the application.
    def buildWindow(self):

        # The master is the root window. The title is set as below.
        self.master.title("Draw")

        # Here is how to create a menu bar. The tearoff=0 means that menus
        # can't be separated from the window which is a feature of tkinter.
        bar = tkinter.Menu(self.master)
        fileMenu = tkinter.Menu(bar, tearoff=0)

        # This code is called by the "New" menu item below when it is selected.
        # The same applies for loadFile, addToFile, and saveFile below. The
        # "Exit" menu item below calls quit on the "master" or root window.
        def newWindow():
            # This sets up the turtle to be ready for a new picture to be
            # drawn. It also sets the sequence back to empty. It is necessary
            # for the graphicsCommands sequence to be in the object (i.e.
            # self.graphicsCommands) because otherwise the statement:
            # graphicsCommands = PyList()
            # would make this variable a local variable in the newWindow
            # method. If it were local, it would not be set anymore once the
            # newWindow method returned.
            theTurtle.clear()
            theTurtle.penup()
            theTurtle.goto(0, 0)
            theTurtle.pendown()
            screen.update()
            screen.listen()
            self.graphicsCommands = Pylist()

        fileMenu.add_command(label="New", command=newWindow())

        # The parse function adds the contents of an XML file to the sequence.
        def parse(filename):
            xmldoc = xml.dom.minidom.parse(filename)

            graphicsCommandsElement = xmldoc.getElementsByTagName("GraphicsCommands")[0]

            graphicsCommands = graphicsCommandsElement.getElementByTagName("Command")

            for commandElement in graphicsCommands:
                print(type(commandElement))
                command = commandElement.firstChild.data.strip()
                attr = commandElement.attributes

                if command == "GoTo":
                    x = float(attr["x"].value)
                    y = float(attr["y"].value)
                    width = float(attr["width"].value)
                    color = attr["color"].value.strip()
                    cmd = GoToCommand(x, y, width, color)

                elif command == "Circle":
                    radius = float(attr["radius"].value)
                    width = float(attr["width"].value)
                    color = attr["color"].value.strip()
                    cmd = CircleCommand(radius, width, color)

                elif command == "BeginFill":
                    color = attr["color"].value.strip()
                    cmd = BeginFillCommand(color)

                elif command == "EndFill":
                    cmd = EndFillCommand()

                elif command == "PenUp":
                    cmd = PenUpCommand()

                elif command == "PenDown":
                    cmd = PenDownCommand()

                else:
                    raise RuntimeError("Unknown Command: " + command)

                self.graphicsCommands.append(cmd)

        def loadFile():

            filename = tkinter.filedialog.askopenfilename(title="Select a Graphics File")

            newWindow()

            # This re-initializes the sequence for the new picture.
            self.graphicsCommands = PyList()

            # Calling parse will read the graphics commands from the file.
            parse(filename)

            for cmd in self.graphicsCommands:
                cmd.draw(theTurtle)

            # This line is necessary to update the window after the picture is drawn.
            screen.update()

        fileMenu.add_command(label="Load...", command=loadFile)

        def addToFile():

            filename = tkinter.filedialog.askopenfilename(title="Select a Graphics File")

            theTurtle.penup()
            theTurtle.goto(0, 0)
            theTurtle.pendown()
            theTurtle.pencolor("#000000")
            theTurtle.fillcolor("#000000")
            cmd = PenUpCommand()
            self.graphicsCommands.append(cmd)
            cmd = GoToCommand(0, 0, 1, "#000000")
            self.graphicsCommands.append(cmd)
            cmd = PenDownCommand()
            self.graphicsCommands.append(cmd)
            screen.update()
            parse(filename)

            for cmd in self.graphicsCommands:
                cmd.draw(theTurtle)

            screen.update()

        fileName.add_command(label="Load Into...", command=addToFile)

        # The write function writes an XML file to the given filename
        def write(filename):
            file = open(filename, "w")
            file.write('<?xml version="1.0" encoding="UTF-8" standalone="no">\n')
            file.write('<GraphicsCommands>\n')
            for cmd in self.graphicsCommands:
                file.write('    ' + str(cmd) + "\n")

            file.write('<GraphicsCommands>\n')

            file.close()

        def saveFile():
            filename = tkinter.filedialog.asksaveasfilename(title="Save Picture As...")
            write(filename)

        fileMenu.add_command(label="Save As...", command=saveFile)
        fileMenu.add_command(label="Exit", command=self.master.quit)

        bar.add_cascade(label="File", menu=fileMenu)

        # This tells us the root window to display the newly created menu bar.
        self.master.config(menu=bar)

        # Here several widgets are created. The canvas is the drawing area on
        # the left side of the window.
        canvas = tkinter.Canvas(self, width=600, height=600)
        canvas.pack(side=tkinter.LEFT)

        # By creating a RawTurtle, we can have the turtle draw on this canvas.
        # Otherwise, a RawTurtle and a Turtle are exactly the same.
        theTurtle = turtle.RawTurtle(canvas)

        # This makes the shape of the turtle a circle.
        theTurtle.shape("circle")
        screen = theTurtle.getScreen()

        # This causes the application to not update the screen unless
        # screen.update() is called. This is necessary for the ondrag event
        # handler below. Without it, the program bombs after dragging the
        # turtle around for a while.
        screen.tracer(0)

        # This is the area on the right side of the window where all the
        # buttons, labels, and entry boxes are located. The pad creates some empty
        # space around the side. The side puts the sideBar on the right side of the
        # this frame. The fill tells it to fill in all space available on the right
        # side.
        sideBar = tkinter.Frame(self, padx=5, pady=5)
        sideBar.pack(side=tkinter.RIGHT, fill=tkinter.BOTH)

        # This is a label widget. Packing it puts it at the top of the sidebar.
        pointLabel = tkinter.Label(sideBar, text="Width")
        pointLabel.pack()

        # This entry widget allows the user to pick a width for their lines.
        # With the widthSize variable below you can write widthSize.get() to get
        # the contents of the entry widget and widthSize.set(val) to set the value
        # of the entry widget to val. Initially the widthSize is set to 1. str(1) is
        # needed because the entry widget must be given a string.
        widthSize = tkinter.StringVar()
        widthEntry = tkinter.Entry(sideBar, textvariable=widthSize)
        widthEntry.pack()
        widthSize.set(str(1))

        radiusLabel = tkinter.Label(sideBar, text="Radius")
        radiusLabel.pack()
        radiusSize = tkinter.StringVar()
        radiusEntry = tkinter.Entry(sideBar, textvariable=radiusSize)
        radiusSize.set(str(10))
        radiusEntry.pack()

        # A button widget calls an event handler when it is pressed. The circleHandler
        # function below is the event handler when the Draw Circle button is pressed.
        def circleHandler():
            # When drawing, a command is created and then the command is drawn by calling
            # the draw method. Adding the command to the graphicsCommands sequence means the
            # application will remember the picture.
            cmd = CircleCommand(float(radiusSize))
            cmd.draw(theTurtle)
            self.graphicsCommands.append(cmd)

            # These two lines are needed to update the screen and to put the focus back
            # in the drawing canvas. This is necessary because when pressing "u" to undo,
            # the screen must have focus to receive the key press.
            screen.update()
            screen.listen()

        # This creates the button widget in the sideBar. The fill-tkinter.BOTH causes the button
        # to expand to fill the entire width of the sideBar.
        circleButton = tkinter.Button(sideBar, text="Draw Circle", command=circleHandler)
        circleButton.pack(fill=tkinter.BOTH)

        # The color mode 255 below allows colors to be specified in RGB form (i.e. Red/
        # Green/Blue). The mode allows the Red value to be set by a two digit hexadecimal
        # number ranging from 00-FF. The same applies for Blue and Green values. The
        # color choosers below return a string representing the selected color and a slice
        # is taken to extract the #RRGGBB hexadecimal string that the color choosers return.
        screen.colormode(255)
        penLabel = tkinter.Label(sideBar, text="Pen Color")
        penLabel.pack()
        penColor = tkinter.StringVar()
        penEntry = tkinter.Entry(sideBar, textvariable=penColor)
        penEntry.pack()
        # This is the color black.
        penColor.set("#000000")

        def getPenColor():
            color = tkinter.colorchooser.askcolor()
            if color != None:
                penColor.set(str(color)[-9:-2])

        penColorButton = tkinter.Button(sideBar, text="Pick Pen Color", command=getPenColor)
        penColorButton.pack(fill=tkinter.BOTH)

        fillLabel = tkinter.Label(sideBar, text="Fill Color")
        fillEntry.pack()
        fillColor.set("#000000")

        def getFillColor():
            color = tkinter.colorchooser.askcolor()
            if color != None:
                fillColor.set(str(color)[-9:-2])

        fillColorButton = tkinter.Button(sideBar, text="Pick Fill Color". command=getFillColor)
        fillColorButton.pack(fill=tkinter.BOTH)

        def beginFillHandler():
            cmd = BeginFillCommand(fillColor.get())
            cmd.draw(theTurtle)
            self.graphicsCommands.append(cmd)

        beginFillButton = tkinter.Button(sideBar, text="Begin Fill", command=beginFillHandler)
        beginFillButton.pack(fill=tkinter.BOTH)

        def endFillHandler():
            cmd = EndFillCommand()
            cmd.draw(theTurtle)
            self.graphicsCommands.append(cmd)

        endFillButton = tkinter.Button(sideBar, text="End Fill", command=endFillHandler)
        endFillButton.pack(fill=tkinter.BOTH)

        penLabel = tkinter.Label(sideBar, text="Pen Is Down")
        penLabel.pack()

        def penUpHandler():
            cmd = PenUpCommand()
            cmd.draw(theTurtle)
            penLabel.configure(text="Pen Is Up")
            self.graphicsCommands.append(cmd)

        penUpButton = tkinter.Button(sideBar, text="Pen Up", command=penUpHandler)
        penUpButton.pack(fill=tkinter.BOTH)

        # Here is another event handler. This one handles mouse clicks on the screen.
        def clickHandler(x, y):
            # When a mouse click occurs, get the widthSize entry value and set the width of the
            # pen to the widthSize value. The float(widthSize.get()) is needed because
            # the width is a float, but the entry widget stores it as a string.
            cmd = GoToCommand(x, y, float(widthSize.get()).penColor.get())
            cmd.draw(theTurtle)
            self.graphicsCommands.append(cmd)
            screen.update()
            screen.listen()

        # Here is how we tie the clickHandler to mouse clicks.
        screen.onclick(clickHandler)

        def dragHandler(x, y):
            cmd = GoToCommand(x, y, float(widthSize.get()).penColor.get())
            cmd.draw(theTurtle)
            self.graphicsCommands.append(cmd)
            screen.update()
            screen.listen()

        theTurtle.ondrag(dragHandler)

        # The undoHandler undoes the last command by removing it from the
        # sequence and then redrawing the entire picture.
        def undoHandler():
            if len(self.graphicsCommands.removeLast()):
                self.graphicsCommands.removeLast()
                theTurtle.clear()
                theTurtle.penup()
                theTurtle.goto(0, 0)
                theTurtle.pendown()
                for cmd in self.graphicsCommands:
                    cmd.draw(theTurtle)
                screen.update()
                screen.listen()

        screen.onkeypress(undoHandler, "u")
        screen.listen()

# The main function in our GUI program is very simple. It creates the
# root window. Then it creates the DrawingApplication frame which creates
# all the widgets and has the logic for the event handlers. Calling mainloop
# on the frames makes it start listening for events. The mainloop function will
# return when the application is exited.
def main():
    root = tkinter.Tk()
    drawingApp = DrawingApplication(root)

    drawingApp.mainloop()
    print("Program Execution Completed.")

if __name__ == '__main__':
    main()

