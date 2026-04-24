#1. WAP that asks user for theie name and age then prints sentence like ->
# "Hello Shraddha , you are 21 years old!"

# name = input("Enter your name :: ")
# age = int(input("Enter your age :: "))

# print("Hello",name,",you are",age,"years old!")

#2. Take 2 numbers as input from the user and print their sum,difference,product and quotient

# num1 = int(input("Enter first number :: "))
# num2 = int(input("Enter second number :: "))

# #Sum
# sum = num1+num2
# print("Sum = ",sum)

# #Difference
# diff = num1-num2
# print("Difference = ",diff)

# #Product
# product = num1*num2
# print("Product = ",product)

# #Quotient
# quotient = num1/num2
# print("Quotient = ",quotient)

#3. Ask the user to enter two integers and one float. Convert them all to floats and print 
# their average.

# num1 = int(input("Enter first number :: "))
# num2 = int(input("Enter second number :: "))
# num3 = float(input("Enter third number :: "))

# sum = float(num1)+float(num2)+num3
# avg = sum/3
# print(avg)


#4. User enters a string containing number. Convert it to :
# a. Integer
# b. Float
# c. String again 
# Print all the 3 values with their types

# str1 = input("Enter a number :: ")
# print(str1)
# print(type(str1))

# num1 = int(str1)
# print(num1)
# print(type(num1))

# num2 = float(str1)
# print(num2)
# print(type(num2))

# str2 = str(str1)
# print(str2)
# print(type(str2))

#5. Evaluate and print the result of the following expression
# x = 10+3*2**2

# x= 10+(3*(2**2))
# print (x)

#6. Swap value of 2 numbers entered by the user

# num1 = int(input("Enter a number :: "))
# num2 = int(input("Enter a number :: "))
# print("Num 1 :: ",num1," - Num 2 ::",num2)
# num1=num1+num2
# num2 = num1-num2
# num1 = num1-num2
# print("Num 1 :: ",num1," - Num 2 ::",num2)


#7. Ask temperature in celsium, convert it to float and calculate the the temperature in farenheit

# temp_cel = float(input("Enter the temperature in degree celsius :: "))

# temp_faren = (temp_cel*(9/5))+32

# print(temp_faren)


#8. Take radius as a user input and print the area of circle pi*r**2

# pi = 3.14
# radius = int(input("Enter the radius of the circle :: "))

# Area = pi*(radius**2)
# print(Area)

#9. Ask user for Principle, rate of interest and time and get the simple interest 

# p = float(input("Enter the principle :: "))
# r = float(input("Enter the rate of interest :: "))
# t = float(input("Enter the time :: "))
# si = (p*r*t)/100
# print("Simple Interest :: ",si)


#10. Take decimal number as input and. print the output seprate as in integer seperate and 
# decimal seperate

# userInput = float(input("Enter a number of choice :: "))

# num_int = int(userInput)
# print(num_int)

# num_dec = userInput-num_int
# print(num_dec)


