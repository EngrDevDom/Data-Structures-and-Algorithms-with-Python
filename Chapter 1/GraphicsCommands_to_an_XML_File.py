# Writing Graphics Commands to an XML File

file = open(filename, "w")
file.write('<?xml version="1.0" encoding="UTF-8" standalone="no" ?>\n')
file.write('<GraphicsCommands>\n')
for cmd in self.graphicsCommands:
    file.write('    ' + str(cmd) + "\n")

file.write('</GraphicsCommands>\n')
file.close()

