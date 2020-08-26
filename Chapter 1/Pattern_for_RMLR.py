# Pattern for Reading Multi-line Records from a File

# First the file must be opened
file = open(filename, "r")

# Read the first line of the first record in the file. Of course, firstLine should be
# called something that makes sense in your program.
firstLine = file.readline().strip()

while firstLine != "":
    # Read the rest of the record
    secondLine = file.readline().strip()
    thirdLine = file.readline().strip()
    # ...

    # Then process the record. This will be determined by the program you are
    # writing.
    print(firstLine, secondLine, thirdLine)

    # Finally, finish the loop by reading the first line of the next record to
    # set up for the next iteration of the loop.
    firstLine = file.readline().strip()

# It's good idea to close the file, but it will be automatically, closed when your
# program terminates.
file.close()

