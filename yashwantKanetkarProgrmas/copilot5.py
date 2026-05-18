#1. Find largest element in list
# list_user=[]
# while True:
#     user_input = input("Enter a number :: ")
#     if user_input == 'q' or user_input=='Q':
#         break     
#     elif not user_input.isdigit():
#         print("Invalid input please try again")
#     else:
#         list_user.append(user_input)
# print(list_user)
# dup=[]
# unique=[]
# for val in list_user:
#     if val in unique:
#         dup.append(val)
#     else:
#         unique.append(val)
# print(unique)
# print(dup)

#3. Sort the list without sort
# list_user = [1,5,7,3,4,7,9,2,5,9]

# for i in range(len(list_user)) :
#     for j in range(len(list_user)-i-1):
#         if(list_user[j]>list_user[j+1]):
#             list_user[j],list_user[j+1] = list_user[j+1],list_user[j]

# print(list_user)


#4. Merge Two list

# list1 = [1,2,5,7,8]
# list2 = [2,4,6,8,9]
# list3 =[]
# for val in list1:
#     list3.append(val)
# for val in list2:
#     list3.append(val)

# print(list3)

#5.Find the second largest element in the list
# list1 = [1,4,7,6,3,82,6,9,5,3]
# largest=max(list1[0],list1[1])

# second=min(list1[0],list1[1])
# for val in list1:
#     if(val>largest):
#         second=largest
#         largest=val
#     elif val>second and val!=largest:
#         second = val

# print(f"Largest = {largest}")
# print(f"Second largest = {second}")

#6.  Rotate list elements

#list_user = [1,5,7,3,4,7,9,2,5,9]

# for i in range(len(list_user)):
#     print(list_user)
#     list_user= list_user[1:]+[list_user[0]]

#7. Sum of the elements of the list

# list1 = [1,5,7,3,4,7,9,2,5,9]
# sum1=0
# for val in list1:
#     sum1=sum1+val
# print(sum1)

#8 Find the common elements in two lists
# list1 = [1,2,5,7,8,6,3,6]
# list2 = [2,4,6,8,9]
# common = []

# for i in list1:
#     for j in list2:
#         if(i==j):
#             common.append(i)

# print(common)

#################### Alternate #################

# list1 = [1,2,5,7,8,6,3,6]
# list2 = [2,4,6,8,9]
# common=[]

# common = list(set(list1).intersection(list2))

# print(common)


#9. Split list into odd or even

# list1 = [1,5,7,3,4,7,9,2,5,9]
# odd=[]
# even=[]

# for val in list1:
#     if(val%2==0):
#         even.append(val)
#     else:
#         odd.append(val)

# print(odd)
# print(even)


