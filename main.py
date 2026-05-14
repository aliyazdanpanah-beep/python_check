# this code show that text you write in matn.txt on output

with open("matn.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())


# this code create a file with text you,r write It


text = input("Enter your text want show: ")

with open("newfile.txt", "w", encoding="utf-8") as file:
    file.write(text)

print("New text save succsesful !")
