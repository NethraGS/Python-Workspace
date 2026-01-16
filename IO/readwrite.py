file = open("data.txt", "w")
file.write("Hello File")
file.close()

with open("data1.txt", "w") as file:
    file.write("Hello File111")

with open("data.txt", "r") as file:
    content = file.read()
    print(content)

file=open("data.txt", "r")
content=file.read()
print(content)
file.close()