#1. Multiplicaton table 
# num=int(input('Enter a number ::'))

# for i in range(1,11):
#     print(num*i)

#2 Largest of 3

# num1 = int(input("Enter a number :: "))
# num2 = int(input("Enter a number :: "))
# num3 = int(input("Enter a number :: "))

# if(num1>num2 and num1>num3):
#     print(f"{num1} is the largest")
# elif(num2>num1 and num2>num3):
#     print(f"{num2} is the largest")
# else:
#     print(f"{num3} is the largest")

#3 Leap year check
# year = int(input('Enter a year to check :: '))

# if(year%400==0):
#     print(f'{year} is a leap year')
# elif(year%100==0):
#     print(f'{year} not a leap year')
# elif(year%4==0):
#     print(f'{year} is a leap year')
# else:
#     print(f'{year} not a leap year')

#4 Sum of digits
# num = int(input("Enter a number :: "))

# sum=0
# temp=abs(num)
# while(temp>0):
#     sum+=temp%10
#     temp=temp//10
# print(sum)


#5 Fibonacci series

# n = int(input('Enter a limit:: '))

# fibo1 = 0
# fibo2 = 1
# #0,1,1,2,3,5,8
# for i in range(n+1):
#     print (fibo1,end=" ")
#     fibo_next = fibo1+fibo2
#     fibo1=fibo2
#     fibo2=fibo_next

#6. Factorial Using loop
# num = int(input('Enter a limit:: '))
# fact=1
# for i in range(num,1,-1):
#     fact*=i
# print(fact)

#7. Reverse a number
# num = int(input('Enter a limit:: '))
# num=abs(num)
# if(num<10 and num >0):
#     print("Single digit number cannot be reversed")
# else:
#     temp=num
#     rev_num =0
#     while(temp>0):
#         digit = temp%10
#         rev_num=rev_num*10+digit
#         temp=temp//10
#     print(rev_num)

#8. Count positive, negative, zero numbers in list
# list=[1,5,8,3,0,0,3,0,-1,-4,-98]
# pos_count=0
# neg_count=0
# zero_count=0
# for val in list:
#     if(val>0):
#         pos_count+=1
#     elif(val<0):
#         neg_count+=1
#     else:
#         zero_count+=1
# print(f"Positive - {pos_count}",f"Negative - {neg_count}",f"Zero. - {zero_count}")

#9 Prime number
# num = int(input("Enter a number"))

# for i in range(2,num):
#     if(num%i==0):
#         print(f'{num} is not a prime number')
#         break
# else:
#     print(f'{num} is a prime number')

#10 Armstrong number in range
# num = int(input("Enter a number :: "))
# for i in range(num+1):
#     if(i<10 and i>0):
#         print(f"{i} is an armstrong number")
#         continue
#     digit=0
#     temp=abs(i)
#     while(temp>0): 
#             digit+=1
#             temp=temp//10
#     #print(f'{i} has digit : {digit}')
#     temp=abs(i)
#     sum=0
#     while(temp>0):
#          sum+=((temp%10)**digit)
#          temp=temp//10
#     #print(f"sum of {i} having {digit} digits is {sum}")
#     if(sum==i):
#          print(f'{i} is an armstrong number')
#     else:
#          print(f'{i} is not an armstrong number')
         





    
    
