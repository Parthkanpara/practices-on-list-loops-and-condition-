#List examples
name = ["ram","shyam","balram"]
print(name[0])
print(name[1])
print(name[2])

number = [1,2,5,7,9]
print(number[4])

new = [1,3,6]
print(new)
print(new[1])

#List Operations
number = [1,1,1,1,1]
number[2] = 5
print(number) # thi function prints the list item with brackets"[ ]"

print(number*2) #number is print twise in brackets"[ ]"

#add new lit in another list
number2 = [6,7,8,9]
print("number1 + number2 : ",number+number2) #number and number2 print together

#check item is available or not using "in":
fruits = ["Apple","Mango","Banana","Peach"]
print("Apple" in fruits) #it return true because apple is in the fruit list.
print("Oranges" in fruits) #it return flase because orange is not in the fruit list.

#add item in list using append function:
fruits.append("Oranges") #now we add Oranges in the fruits list
fruits.append("Watermelon") # add Watermelon in the fruits lit
print(fruits)

print("updated list count is ",len(fruits),"\n") # It returns length of the updated list. "\n is use for new line.

#Add item in fruits list using insert function:
fruits.insert(1,"pineapple") # It put the items in fruits list at specific index.
print(fruits)

print("updated list count is ",len(fruits),"\n") # It returns length of the updated list.

#find the index of item in list("fruits") :
print("Index of Oranges in fruits is ",fruits.index("Oranges"))
print("Index of Banana in fruits is ",fruits.index("Banana"))

