#1. Store the following word meaning in a dictionary
#table: "a piece of furniture","list of facts and figures"
#cat: " a small animal"

# firstDict = {}

# firstDict.update(table="a piece of furniture. list of facts and figures")
# firstDict.update(cat="a small animal")
# print(firstDict)

#Correct sol : dict = {
#  "cat" : "a small animal",
#  "table" : ["a piece of furniture","list of facts and figures"],
# }

#2. You are given a list of subjects for students. Assume one class room is required
# for 1 subject . how many classroom are required by all the students

# subjects = {"python","java","c++","python","javascript","java","python","java","c++","c"}

# numberOfClassrooms = len(subjects)
# print(numberOfClassrooms)

#3. WAP to enter marks of 3 subjects from the user and store them in a dictionary.
#Start with empty dictionary and add one by one. Use subject name as key and marks as value

# students = {}
# print(type(students))
# students.update(Math = input("Marks Obtained in math : "))
# students.update(Chem = input("Marks Obtained in chem : "))
# students.update(Phy = input("Marks Obtained in phy : "))
# print(students)


#4. Figure out a way to store 9 and 9.0 as seperate value in set. You can take help of built in
# data types
#Solution 1
# store = {9,str(9.0)}
# print(store)

#Solution 2
store = {("float",9.0),("int",9)}
print(store)