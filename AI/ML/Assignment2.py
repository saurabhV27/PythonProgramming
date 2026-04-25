import random
#1. WAP to segregate between chil teenager and adult depending on their age.

# age = int(input("Please enter the age of the person :: "))


# if age<=0 or age>=105:
#     print("Invalid age !! Please enter the correct age")
# elif age<= 13:
#     print("Person is a child")
# elif age>13 and age<=18:
#     print("Person is a teenager")
# else:
#     print("Person is a adult")

#2. Count the number of vowels in a given string

# userStr = input("Enter a string :: ")
# count = 0
# vowels = "aeiou"
# for ch in userStr.lower():
#     if ch in vowels :
#         count+=1
# print(count)

#3. Print the sum of first n natural numbers

# n = int(input("Enter a limit ::"))
# sum = 0
# for i in range(n):
#     sum=sum+i

# print(sum)

#4. Take 3 numbers as input and return the average value

# def calc_avg(num1,num2,num3):
#     sum = num1+num2+num3
#     avg = sum/3
#     return avg

# avg = calc_avg(4,5,6)
# print(avg)

#5. WAP to print factorial of n

# def factorial(num):
#     fact = 1
#     for i in range(1,num+1):
#         fact *=i
#     print (fact)

# factorial(5)
## Recursion
# def factorial(n):
#     fact=0
#     while n==0 or n==1:
#         return 1
#     return n*factorial(n-1)

# fact = factorial(5)
# print(fact)


################################ Assignment Questions ##########################

#1.WAP that takes salary as a input . Using conditional statements calculate the final tax
#based on the rules below
# if salary < 30000->5 %
# if salary 30000-70000 -> 15%
# if salary >70000-> 25%

# salary = int(input("Enter the salary :: "))

# if salary<=0:
#     print('Invalid input')
# elif(salary>0 and salary<30000):
#     tax = '5%'
#     print ('Tax applicable on salary is ',tax)
#     print('Take home salary is :: ',salary-(salary*0.05))
# elif(salary>30000 and salary<70000):
#     tax = '15%'
#     print ('Tax applicable on salary is ',tax)
#     print('Take home salary is :: ',salary-(salary*0.15))
# else:
#     tax = '25%'
#     print ('Tax applicable on salary is ',tax)
#     print('Take home salary is :: ',salary-(salary*0.25))

#2. Write a function that takes 2 inputs a and b and print all the even number between 
# them 

# def print_even(a,b):
#     for i in range(a,b+1):
#         if(i%2==0):
#             print(i)

# print_even(2,20)

#3. Write a function that prints the digits of number n.

# def num_digits(num):
#     if(num<=9):
#         print(num)
#     else:
#         digits=[]
#         temp = num
#         while temp>0:
#             digit=temp%10
#             temp=int(temp/10)
#             digits.append(digit)
#             #print(digits)
        
#         for d in reversed(digits):
#             print(d)

    
# userInput = int(input("Enter a number of choice :: "))
# num_digits(userInput)

#4. WAF to return the count of digits in a number n.

# def digit_count(num):
#     num = abs(num)
#     count = 0
#     if(num==0):
#         return 1
#     else:
#         while num>0:
#             num=int(num/10)
#             count+=1
#     return count

# num = digit_count(-415)
# print(num)

#5. Write a program to return the cum of digits

# def sum_of_digits(num):
#         temp=abs(num)
#         sum=0
#         while temp>0:
#             digit = temp%10
#             temp//=10
#             sum+=digit
#         print (sum)


# sum_of_digits(3)

#6. WAP to print numbers that are divisible by both 3 and 5

# for num in range(1,101):
#     if(num%3==0 and num%5 ==0):
#         print(num)
    
#7. Design a program to continuously input a number from the user and print
# if its positive or negative until the user enters 'Quit'
# num=''
# while num!='Quit':
#     num = input('Enter a number :: ')
#     if(num=='Quit'):
#         break
#     elif(int(num)<0):
#         print(num,'is a negative num')
#         print('If you want to quit please enter "Quit"')
#     elif(int(num)>0):
#         print(num, 'is a positive number')
# print("Game Ended !!")

#8. create a simple calculator that performs arithemetic operations. create a function 
# calculator(a,b,'operation') that performs addition, subtraction,multiplication and division
# based on the operation parameter. [operation parameter can have '+','-','*','/'].

# def calculator(a,b,operation):
#     match operation:
#         case "+":
#             sum=a+b
#             print(sum)
        
#         case "-":
#             diff=a-b
#             print(diff)
        
#         case "*":
#             multi=a*b
#             print(multi)

#         case "/":
#             div=a/b
#             print(div) 
    
# calculator(5,4,"+")
# calculator(5,4,"-")
# calculator(5,4,"*")
# calculator(8,4,"/")

#9. Write a function is_prime(n) that returns True 
# if n is a prime number and false if the number is not prime
#using loop

# def is_prime(n):
#     if(n<=1):
#         return False
#     for i in range(2,n):
#         if(n%i==0):
#             return False
#     return True
        
# userInput = int(input("Enter a number :: "))
# prime = is_prime(userInput)
# print(userInput," is prime? ",prime)

#10. Lets create a number guessing game given a secret number write a program to ask the user
#ask the user to guess and print it


# secret_num = random.randint(1,100)

# while True :
#     userInput=input("Enter a number or press Q to (quit) ::  ")
#     if(userInput=='q' or userInput=="Q"):
#         break

#     if(int(userInput)>secret_num):
#         print("Too High !! Please try again!!")
#     elif(int(userInput)<secret_num):
#         print("Too Low !! Please try again")
#     elif(int(userInput)==secret_num):
#         print("Correct you win!!")



