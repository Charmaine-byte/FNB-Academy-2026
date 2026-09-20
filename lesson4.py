#Basic if/else statement

age = int(input("Enter your age: "))
section_pass = input("Do you have a vip ticket ? (yes/no) ").lower()

if age >= 18 and section_pass == "yes":  #comparison statement if age is greater or equal to 18.   
    print("Access granted to vip section!!!") 
elif age >= 18:  #elif statement for short of if else40
    print("Access granted to the general setion !!!")    
else: #fall back plan if everything fails
    print("Access denied !!!")    