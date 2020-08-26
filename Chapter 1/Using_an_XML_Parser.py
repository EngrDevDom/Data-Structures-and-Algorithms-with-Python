# Using an XML Parser

for commandElement in graphicsCommands:
    print(type(commandElement))
    command = commandElement.firstChild.data.strip()
    attr = commandElement.attributes
    if command == "GoTo":
        x = float(attr["x"].value)
        y = float(attr["y"].value)
        width = float(attr["width"].value)
        color = attr["color"].value.strip
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

    self.append(cmd)

