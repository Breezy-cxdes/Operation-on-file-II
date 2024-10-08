with open("Breezy.txt","w") as f:
    f.write("adde something else")
f.close()

with open("breezy.txt","r") as file:
    data=file.readlines()
    for line in data:
      word=line.split()
      print(word)
file.close()

new_file=open("snow.txt","x")
new_file.close()
import os
 
if os.path.exists("newfile.txt"):
    os.remove("my file.txt")
else:
    print("the file does not exist")


    
    
# Creating the output file
outputFile = open('UpdatedFile.txt', 'w')

# Reading the input file
inputFile = open('Repeated.txt', 'r')

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
