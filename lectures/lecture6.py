#1. create a functions to find the avereage of 3 numbers

# def num_avg(a,b,c):
#     avg = (a+b+c)/3
#     return avg

# result = num_avg(2,3,4)

# print(result)

#2. WAF to print the length of the list.(List is the parameter)

# def list_len(list):
#     print(len(list))

# list = [1,5,6,4,33,7,8,8,2]

# list_len(list)

#3. WAF to print the elements of a list in a single line.

# def elements_List(list):
#     for el in list:
#         print(el,end=" ")


# list = [1,5,6,4,33,7,8,8,2]
# elements_List(list)

#4. WAF to find the factorial of n.(n is the parameter)

# def factorial(num=5):

#     fact=1
#     for n in range(1,num):
#         fact = fact*n
#     return fact


# userInput = int(input("Enter a number to find factorial :: "))

# result = factorial(userInput)

# print(result)

#5.WAF to convert US $ to rupees.

# def curr_Convert(currency):

#     rupees = 92*currency
#     return rupees

# amount = float(input("Enter amount to be converted : "))

# money = curr_Convert(amount)

# print(money)

#6. WAF to segregate numbers as odd or even

# def odd_Even(number):

#     if(number%2==0):
#         return "Even"
#     else:
#         return "Odd"


# num = int(input("Enter a number to check :: "))

# Result = odd_Even(num)

# print(Result)


#7. Write a recursive function to calculate the sum of first n natural numbers
#1,2,3,4,5 -> n,n-1,n-2,n-3,...

# def calc_Sum(n):
#     if(n==0):
#         return 0
    
#     return calc_Sum(n-1)+n

# result  = calc_Sum(5)
# print(result)


#8. Write a recursive function to print all the elements of a list


# def list_el(list,idx):
#     if(idx==-1):
#         return
#     print (list[idx]) 
#     list_el(list,idx-1)

# list=[1,5,3,6,8,9]
# list_el(list,len(list)-1)

#Solution 2

# def list_el(list,idx):
#     if(idx == len(list)):
#         return
#     print(list[idx])
#     list_el(list,idx+1)

# list=[4,8,5,3,1,6,8]
# list_el(list,0)