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