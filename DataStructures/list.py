numbers = [1, 2, 3, 4]
numbers.append(5)
print(numbers)

myList=[10,"apple",12,13,14]
print("--------")
print(myList)
print(myList[1:2])
print(myList[1:3])
print(myList[:2])
print(myList[2:])

items=["apple","banana","cherry","orange","kiwi","melon","mango"]
if "apple" in items:
    print("Yes, 'apple' is in the fruits list")
elif "banana" in items:
    print("Yes, 'banana' is in the fruits list")
else:
    print("fruit not found")

print("--------")
for i in items:
    if i=="apple":
        print("100 rupees per kg")
    elif i=="banana":
        print("30 rupees per dozen")
    elif i=="cherry":
        print("50 rupees per kg ")
    elif i=="orange":
        print("80 rupees per kg")
    else:
        print("price not found")