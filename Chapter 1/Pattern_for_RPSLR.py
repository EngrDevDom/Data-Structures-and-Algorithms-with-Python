# Pattern for Reading Single Line Records from a File

# First the file must be opened.
file = open(filename, "r")

# The body of the for loop is executed once for each line in the file.
for line in file:
    # Process each record of the file. Each record must be exactly one line of the
    # input file. What processing a record means will be determined by the
    # program you are writing.
    print(line)

# Closing the file is always a good idea, but it will be closed when your program
# terminates if you do not close it explicitly.
file.close()

