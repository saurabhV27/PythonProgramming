#1. Student marks management (add, update, search, display)

# student = {
#     "name" : "Saurabh",
#     "subject" : {
#         "Chemistry" : 98,
#         "Physics" : 78,
#     },
#     "cgpa" : 9.6,
# }

# while True:
#     print("****** Menu ******")
#     print("1. Add Subject Marks")
#     print("2. Update Subject marks")
#     print("3. Search Subject")
#     print("4. Display Subject Marks")
#     print("5. Quit")
#     print("********************")
#     user_input= int(input("Please choose from the option :: "))

#     if user_input==1:
#         sub = input("Enter Subject Name :: ")
#         marks = int(input("Enter marks obtained :: "))
#         student["subject"][sub] = marks
#         print(f"{marks} obtained in subject {sub}")
#     elif user_input==2:
#         sub = input("Enter subject name :: ")
#         if(sub in student["subject"]):
#             marks = int(input("Enter the marks obtained :: "))
#             student["subject"][sub] = marks
#             print(f"Marks updated !!")
#         else:
#             print("Subject not found !!")
#     elif user_input==3:
#         sub = input("Enter the subject name to search. :: ")
#         if(sub in student["subject"]):
#             print(f"{sub} : {student['subject'][sub]} marks")
#         else:
#             print(f"{sub} not found ")
#     elif user_input==4:
#         for sub,marks in student["subject"].items():
#             print(f"{sub} : {marks}")
#     elif user_input==5:
#         print("********** Exiting Program *********")
#         break
#     else:
#         print("Invalid input !!")

#2. Count word frequency in a sentence
# sentence = "Saurabh wants to try harder Saurabh Saurabh"
# freq = {}

# for val in sentence.split(" "):
#     if(val in freq):
#         freq[val]+=1
#     else:
#         freq[val]=1
# print(freq)

#3. Convert 2 lists in a dictionary
# list1 = ["Phy","Chem","Math","Eng"]
# list2 = [78,89,90,67]
# i=0
# sub={}
# while(i<len(list2)):
#     for val in list1:
#         sub[val]=list2[i]
#         i+=1
# print (sub)

############# Alternate #############
# list1 = ["Phy","Chem","Math","Eng"]
# list2 = [78,89,90,67]

# sub = dict(zip(list1,list2))
# print (sub)

# #4.Find the key with max value
# student={
#     "name" : "Saurabh",
#     "subject" : {
#         "chem" : 98,
#         "phy" : 56,
#         "math" : 100

#     }
# }
# mark=0
# subject =""
# for sub,marks in student["subject"].items():
#     if(marks>mark):
#         mark = marks
#         subject=sub
# print(subject ,":", mark)

# #5.Merge 2 dictionary

# student ={
#     "name" : "Saurabh",
#     "subject" : {
#         "chem" : 98,
#         "phy" : 56,
#         "math" : 100

#     }

# }

# student2 ={
#     "name2" : "Priya",
#     "subject2" : {
#         "chem2" : 96,
#         "phy2" : 97,
#         "math2" : 65

#     }

# }
# student.update(student2)
# print(student)

# #6. Delete a key from dictionay

# student ={
#     "name" : "Saurabh",
#     "subject" : {
#         "chem" : 98,
#         "phy" : 56,
#         "math" : 100

#     }

# }

# del student["name"]
# print(student)


#7. Sort the dictionay by values

# student = {
#     "name":"Saurabh",
#     "name2": "priya",
#     "subject" : {

#         "chem" : 98,
#         "phy" : 56,
#         "math" : 100

#     }

# }
# sorting = dict(sorted(student["subject"].items(),key=lambda x: x[1]))
# print(sorting)

#8 Invert a dictionary

# student ={
#     "name":"Saurabh",
#     "name2": "priya",
#     "subject" : {

#         "chem" : 98,
#         "phy" : 56,
#         "math" : 100
# }
# }

# inverted = {value:key for key,value in student["subject"].items()}
    
    
# print(inverted)

# #9. Check if key exists
# student ={
#     "name":"Saurabh",
#     "name2": "priya",
#     "subject" : {

#         "chem" : 98,
#         "phy" : 56,
#         "math" : 100
# }
# }
# if "Saurabh" in student.values():
#     print("Saurabh exists in students")







