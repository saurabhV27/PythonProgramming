#1. Print numbers from 1 to 100
# i=1
# while i<=100:
#     print(i)
#     i+=1

#2. Print numbers from 100 to 1

# i=100

# while i>=1:
#     print(i)
#     i-=1

#3. Print the multiplication table for a number n

# n = int(input("Enter a number :: "))
# i=1

# while i<=10:
#     print(n,"*",i," =",n*i)
#     i+=1

#4. Print the elements in the given list using loops
 
# list = [1,4,9,16,25,36,49,64,81,100]
# i = 0
# while i<len(list):
#     print(list[i])
#     i+=1

#5 Search for a number x in the given tuple

# tup=(1,4,9,16,25,36,49,64,81,100,)
# num = int(input("Enter a number to search : "))
# i = 0

# while i<len(tup):
#     if(tup[i] == num):
#         print(num," found at index " ,i)
#         break
#     # else:
#     #     print(num," is not present")
#     i+=1

#################################################################

#For Loop

#1. Print the following list using loop

# list = [1,4,9,16,25,36,49,64,81,100]

# for items in list:
#     print(items)

#2. Search for number x in the tuple 

# tup = (1,4,9,16,25,36,49,64,81,100)
# num = int(input("Enter a number :: "))
# print(type(tup))


# for items in tup :
#     if(items == num):
#         print("Found")
#         break;
# else : 
#     print("Not found")   
# 
# ##################################################
# 
# 
#Range

#1. Print numbers from 1 to 100

# for i in range(1,101):
#     print(i)

#2. Print numbers from 100 to 1

# for num in range(100,0,-1):
#     print(num)

#3. Print multiplication table of number n

# num = int(input("Enter a number :: "))

# for i in range(1,11):
#     print(num,"*",i,"= ",num*i)