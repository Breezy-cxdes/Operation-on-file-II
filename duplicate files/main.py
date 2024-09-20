# Creating the output file
outputFile = open('UpdatedFile.txt', 'w')

# Reading the input file
inputFile = open('duplicate lines.txt', 'r')

# Holds lines already seen
lines_seen_so_far = set()

print("Eliminating duplicate lines....")

# Iterating through each line in the file
for line in inputFile:
    # Checking if the line is unique
    if line not in lines_seen_so_far:
        # Writing unique lines to the output file
        outputFile.write(line)
        # Adding the unique line to lines_seen_so_far
        lines_seen_so_far.add(line)

# Closing the files
inputFile.close()
outputFile.close()

print("Duplicate lines removed successfully!")
