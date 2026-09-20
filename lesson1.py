#make the computer talk to you
print("hello world")

# variables,write my name down 
name = "Yandisa"   #declaring a variable
print(name)

age = 22
print(age)

#make greetings using formatted 
print(f"Welcome, {name}")

name = input("Enter your name: ")
age = int(input("Enter your age: "))

age = 40
price = 20.55
first_name = "Thembi"
is_online = False # a boolean value we use capital letter F because lowercase f is not recognised in python
print(age)
print(price)
print(first_name)
print(is_online)

#patient records
patient_name = "John Smith"
print(patient_name)
age = 20
print(age)

name = input("What is your name? ")
print("Hello " + name)
age = 20
print(age)

#int is for interger representing a whole number e.g 2020
#str is string represnting e.g birth_year
#float a number with decimal number
birth_year = input('Enter your birth year:')
age = 2020 - int(birth_year)
print(age)

#Basic calculator programme
first = input("First: ")
second = input("Second: ")
sum = float(first) + float(second)  #concartinating 2 strings
print("sum")

#strings
course = 'Python for Beginners'
print(course.upper())  #we can also put find,replace,lower methods etc.
print(course)

#Arithmetic operators
#/ gives float number with decimals
#// gives an interger which is a whole number
#** exponent
#== an equal to
#+ addition
print(10//3)

#comparison oprerators,used to compare values
x =3 > 2
print(x)

price = 25
print(price > 10 and price < 30)

temperature = 25

if temperature > 30:
    print("it's a hot day")
    print("Drink plenty of water")
elif temperature > 20:  #(20,30) # we can have many conditions as we want 
    print("it's a nice day")
else:
    print("it's cold")    
print("Done")

#weigth converter
weight = input("Weight: ")
unit = input("(K)g or (L)bs:")
if unit.upper() =="K":
    converted = weight /0.45
    print("Weight in Lbs: " + str(converted))
else:
    converted = weight * 0.45
    print("Weight in kgs: " + str(converted))


#while loops
#to repeat a block of code multiple times
i = 1
while i <= 5:
    print(i)
    i = i + 1

#lists
names = ["Thembi", "Alicia", "Zinhle","Yandisa"] 
print(names [0]) ="jon" #0 represents the first element and -1 represents the last
print(names[0:3]) #this will give us names from 0 t0 3

#list methods
numbers = [1, 2, 3, 4, 5]
numbers.append(6) #can also use remove,insert,
print(numbers)

#len returns number of elements
numbers = [1, 2, 3, 4, 5]
print(len(numbers))

#for loops
numbers = [1, 2, 3, 4, 5]
for item in numbers:
    print (item)

#while loop
i = 0
while i < len(numbers):
    print(numbers[i])
    i = i + 1   

# the range function to generate a sequence of numbers
numbers = range(5, 10, 2)
for number in numbers:
    print(number)

#tuples cannot be changed when created
numbers (1, 2, 3)
numbers.count