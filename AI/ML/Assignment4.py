#1. Check if the string given by the user is a palindrome

# userInput = input("Please enter a String :: ")
# userInput = userInput.lower()

# str1 = ""
# for ch in userInput:
#    # print(type(ch))
#     str1 = ch+str1
# if str1==userInput:
#     print(f"{str1} is a palindrome")
# else:
#     print(f"{userInput} is not a palindrome")

#Alternate Approach
# userInput = input("Please enter a String :: ")
# userInput = userInput.lower()
# userInput = userInput[::-1]
# print(userInput)

#2. Given a list of integer compute the average of the list

# list=[1,5,7]
# sum = 0
# avg = 0
# for val in list:
#     sum+=val
# avg= sum/len(list) 
# print(f"Average is {avg}")

#3. Input 2 lists from user . Merge them and sort the list

# list1=[1,4,5]
# list2=[3,6,7,9]

# result = list1+list2
# print(result)

# result.sort()

# print(result)

#4. Given a tuple of integers: 1. Create a tuple of all even number interger 
# and one of all odd numbers

# tup = (1,2,3,4,5,6,7,8,9,10,11,12)
# tup1=[]
# tup2=[]

# for val in tup:
#     if(val%2==0):
#         tup1.append(val)
#     else:
#         tup2.append(val)
# tup1=tuple(tup1)
# tup2=tuple(tup2)

# print(tup1)
# print(tup2)

#Alternate (One liner comprehension style)
# tup = (1,2,3,4,5,6,7,8,9,10,11,12)
# tup1,tup2=[],[]

# evens= tuple(x for x in tup if x%2==0)
# odds= tuple(x for x in tup if x%2!=0)

# print(evens)
# print(odds)


#5. Create a dictionary where: 
# keys = student names
# values = marks(Integers)

#Write a menu based program where the user presses a 
# key(A,B,C,D) depending on the operations
#they want to perform 
#A -> Add student
#B -> Update marks
#C -> Search for student
#D -> Display all all the students and marks

# student={}

# while True:
#     print("************** MENU **************")
#     print("A -> Add Student")
#     print("B -> Update marks for student")
#     print("C -> Search for a Student")
#     print("D -> Display all the student with marks")
#     print("Q -> Quit")

#     userInput=input("Please select an option :: ").upper()

#     if(userInput=='A'):
#         student_name = input("Enter the name of the student :: ")
#         student_marks = int(input("Enter the marks obtained :: "))
#         student[student_name]=student_marks
    
#     elif(userInput=='B'):
#         student_name = input("Enter the name of the student ::")
#         if(student_name in student):
#             student_marks=int(input("Enter the marks obtained :: "))
#             student[student_name]= student_marks
#         else:
#             print("Error -> Student not found !!")
        
#     elif(userInput=='C'):
#         student_name = input("Enter the name of the student :: ")
#         if student_name in student:
#             print(f"{student_name} has obtained {student[student_name]}")
#         else:
#             print("Error -> Student not found !!")
    
#     elif(userInput=='D'):
#         if student:
#             for studen_name,student_marks in student.items():
#                 print(f"{student_name} :: {student_marks}")
#         else:
#             print("Error -> Empty Dictionary")
    
#     elif(userInput== 'Q'):
#         print("Thankyou !!")
#         break
    
#     else:
#         print("Invalid entry !!")

#6. Given a list of words create a dictionary that maps each word to its length.

# words=["apple","banana","kiwi","cherry","mango"]
# words_len={}
# for word in words:
#     words_len[word]=len(word)

# print(words_len)

#7. Write a program that takes string input from the user and print the number of spaces

# userInput=input("Enter a String :: ")
# count=0
# for ch in userInput:
#     if(ch == " "):
#         count+=1
#     else:
        
#         continue
# print(f"Number of Spaces :: {count}")

#8. Write a program to check whether two list share no common elements
# list1 =[1,2,3] 
# list2 =[3,4]
# set1 = set(list1)
# set2 = set(list2)

# common = set1.intersection(set2)

# print(common)

# if not common:
#     print("No common Elements")
# else:
#     print(f"Common elements are {common}")

#Alternate Approch
# list1 =[1,2,3] 
# list2 =[3,4]

# if set(list1).isdisjoint(list2):
#     print("No common elements")
# else:
#     print("List share common elements")

#9. Given list , print all the elements that appear more than 
# one in the given list

# list1=[1,2,2,5,3,7,7,8,3,3,9]
# duplicate = set()
# i=0

# while(i<len(list1)):
#     j=i+1
#     while(j<len(list1)):
#         if(list1[i]==list1[j]):
#             duplicate.add(list1[i])
#         j+=1
#     i+=1
# print(duplicate)

#10. Ask the user to enter a string and print all unique character
#  and count of all unique characters

# userInput = input("Enter a string. :: ").lower()
# unique = set()

# for ch in userInput:
#     unique.add(ch)
# print(unique)
# print(unique.__len__())

    
        















