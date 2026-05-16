#1. Factorial using recursion

# def fact_rec(num):
    
#     if(num==1 or num == 0):
#         return 1  
#     else:
#         return (num*fact_rec(num-1))
# fact = fact_rec(int(input("Enter a number :: ")))
# print(fact)

#2. Prime number check function

# def check_prime(num):
#     if(num==0 or num==1):
#         print(f'{num} is not a prime number')
#         return
#     for n in range(2,num):
#         if(num%n==0):
#             print(f'{num} is not a prime number')
#             break
#     else:
#         print(f'{num} is a prime number')
        

# num = int(input('Enter a number to check :: '))
# check_prime(num)

# #3. Calculator using function

# def add_numbers(num1,num2):
#     return num1+num2

# def subtract_numbers(num1,num2):
#     if(num1>num2):
#         return num1-num2
#     else:
#         return num2-num1

# def multiply_numbers(num1,num2):
#     return abs(num1*num2)

# def divide_numbers(num1,num2):
#     return num1/num2


# sum = add_numbers(4,6)
# diff = subtract_numbers(4,6)
# mul = multiply_numbers(4,6)
# div =divide_numbers(4,6)
# print(sum)
# print(diff)
# print(mul)
# print(div)

#4. Palindrome check

# def palindrome_num(num):
#     rev_num=0
#     temp=num
#     while(temp>0):
#         digit = temp%10
#         rev_num=rev_num*10+digit
#         temp=temp//10
#     print(rev_num)
#     if(rev_num==num):
#         return f"{num} is a palindrome"
#     else:
#         return f"{num} is not a palindrome"
    
# def palindrome_string(user_input):
    
#     rev_str=""
#     input=user_input.lower()
#     for ch in input:
#         rev_str=ch+rev_str
#     print(rev_str)
#     if(input==rev_str):
#         return f"{user_input} is a palindrome"
#     else:
#         return f"{user_input} is not a palindrome"


# while True:
#     options = input("Please select 1 to check Palindrome number or 2 to check for String Palindrome ::")
#     if(options=='1'):
#         num=int(input("Enter a number of choice :: "))
#         result = palindrome_num(num)
#         print(result)
#         break
#     elif(options=='2'):
#         string_input = input("Enter a String of choice :: ")
#         result = palindrome_string(string_input)
#         print(result)
#         break
#     elif(options=='Q' or options=='q'):
#         break
#     elif(options!='1' and options!='2'):
#         print("Invalid option please try again")

#5. Armstrong number check

# def check_armstrong(num):
#     digit =0
#     temp = num
#     while temp>0:
#         digit+=1
#         temp=temp//10
#     print(digit)
#     temp=num
#     armstrong_num=0
#     while temp>0:
#         armstrong_num+=((temp%10)**digit)
#         temp=temp//10

#     if(num==armstrong_num):
#         return f"{num} is an armstrong number"
#     else:
#         return f"{num} is not an armstrong number"
    

# result = check_armstrong(153)
# print(result)

#6 Greatest common divisor of two numbers

# def check_gcd(num1,num2):
#     remainder=0
    
#     while (num2!=0):
#         remainder = num1%num2
#         num1=num2
#         num2=remainder
#     print(num1)

# check_gcd(48,18)


#7. Find the LCM of 2 numbers
# import math

# def lcm_check(num1,num2):
#     lcm = abs((num1*num2)//(math.gcd(num1,num2)))
#     return lcm

# result = lcm_check(4,6)
# print (result)

#8. Check for perfect number
# def perfect_number(number):
#     addition = 0
#     for i in range(1,number):
#         if(number%i==0):
#             addition+=i
    
#     print(addition)
#     if(addition==number):
#         print(f"{number} is a perfect number")

# num = int(input("Enter a number :: "))
# perfect_number(num)

#9. nCr combination

# def get_nCr_combination(n,r):
#     fact_n=1
#     fact_r=1
#     fact_n_r=1
#     for i in range(1,n+1):
#         fact_n*=i
#     for i in range(1,r+1):
#         fact_r*=i
#     for i in range(1,abs(n-r)+1):
#         fact_n_r*=i
#     combi = (fact_n//(fact_r*fact_n_r))
#     return int(combi)

# result = get_nCr_combination(10,5)
# print(result)

############### Alternate ###############
# import math

# def nCr_combi(n,r):
#     combi = math.factorial(n)//(math.factorial(r)*math.factorial(n-r))
#     return combi
# n = int(input("Enter the value for n :: "))
# r = int(input("Enter the value for r :: "))

# result = nCr_combi(n,r)
# print(result)

#10. nPr permutation
# import math 

# def nPr_combi(n,r):
#     permu_combi = math.factorial(n)//(math.factorial(n-r))
#     return permu_combi

# result = nPr_combi(10,5)
# print(result)



    



        

