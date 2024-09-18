with open("Breezy.txt","w") as f:
    f.write("adde something else")
f.close()

with open("breezy.txt","r") as file:
    data=file.readlines()
    for line in data:
      word=line.split()
      print(word)
file.close()
