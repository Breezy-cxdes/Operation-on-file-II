# Reading data from file1
with open('merge file.txt', 'r') as fp:
    data1 = fp.read()

# Reading data from file2
with open('merge file.txt', 'r') as fp:
    data2 = fp.read()

# Merging the two files, adding data from file2 on the next line
data1 += "\n" + data2

print("Merging two files....")

# Writing the merged data to a new file
with open('MergedFile.txt', 'w') as fp:
    fp.write(data1)

print("Files merged successfully!")
