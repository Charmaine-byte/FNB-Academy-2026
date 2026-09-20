#Student information formatter

#collect user inputs
name = input("Enter your Name: ")
surname = input("Enter your Surname: ")
age = int(input("Enter your Age: "))
fav_num= float(input("Enter your favourite number: "))

#Display a formatted greeting
print (f"Welcome {name} {surname}!")

#Display the full name in uppercase and title case
full_name = f"{name} {surname}"
print (full_name.upper())
print (full_name.title())

#Display the age in months
age_in_months = age * 12
print ("age in months is:", age_in_months)

#Round off favourite number to 2 decimal places
print("Favourite number (rounded off): ", round(fav_num,2))

#Display the data types
print (type(name))
print (type(surname))
print (type(age))
print (type(fav_num))