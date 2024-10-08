'''
Armon Perez 
CPSC 323 Project 1
Question #4 , Prog2
Group 7
'''

with open("file.txt", "r") as file1:
    lines = file1.readlines()

clean_lines = []

for words in lines:
    words = words.strip()


    if words.startswith("//") or words == "":
        continue
    
    if "//" in words:
        words = words.split("//")[0].strip()

    words = ' '.join(words.split())

    words = words.replace("=", " = ")
    words = words.replace(",", " , ")
    words = words.replace("+", " + ")
    words = words.replace("cin >>", "cin>>")

    for statement in words.split(';'):
            if statement.strip():
                clean_lines.append(statement.strip() + ' ;')

   
with open("clean.txt", "w") as file2:
    for line in clean_lines:
        line = ' '.join(line.split())
        line = line.replace(" =", " =").replace(" ,", " ,").replace(" +", " +")
        file2.write(line + "\n")

        