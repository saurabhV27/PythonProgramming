#1. Read and write to a file

# f=open("/Users/saurabhvalunjkar/Python/PythonProgramming/yashwantKanetkarProgrmas/sample.txt","w+")
# data=f.read()
# print("Before :: ",data)
# str1="This is a sample file where\n i am trying to write somethings to \nmake sure it is visible in the file"
# f.write(str1)
# f.seek(0)
# data1=f.read()
# print("After :: ",data1)

# f.close()

#2. Count the sentence,line, words of a file

# f=open("/Users/saurabhvalunjkar/Python/PythonProgramming/yashwantKanetkarProgrmas/sample.txt","r")
# data = f.read()
# print("Current Data :: ",data)

# #Lines
# lines = data.splitlines()
# count_lines = len(lines)

# #Words
# words = data.split()
# count_words = len(words)

# #sentences
# import re
# sentences = re.split(r'[.?!]',data)
# sentences = [s.strip() for s in sentences if s.strip()]
# count_sent = len(sentences)

# print(count_lines)
# print(count_words)
# print(count_sent)

#3. Copy contents from one file to another

#src = "/Users/saurabhvalunjkar/Python/PythonProgramming/yashwantKanetkarProgrmas/sample.txt"
# des = "/Users/saurabhvalunjkar/Python/PythonProgramming/yashwantKanetkarProgrmas/sample2.txt"

# with open(src,"r") as f_src :
#     data = f_src.read()

# with open(des,"w") as f_des :
#     f_des.write(data)

#4. Append text to file

# str1 = "I want this appended at the end"
# with open(src,"a") as f:
#     f.write(str1)

# with open(src,"r") as f2:
#     data=f2.read()
#     print(data)

#5. Search for a word in the file


# word = input("Please enter a word to search :: ")
# found = False
# with open(src,"r") as f:
#     #data=f.read()
#     for line_no,line in enumerate(f,start=1):
#         if word in line:
#             print(f"{word} found at line {line_no} :: {line.strip()} !!")
#             found=True

# if not found:
#     print("Not Found!!")

#6. Remove blank lines from the files

# src = "/Users/saurabhvalunjkar/Python/PythonProgramming/yashwantKanetkarProgrmas/sample.txt"

# with open(src,"r") as f:
#     lines = f.readlines()

# with open(src,"w") as f2:
#     for line in lines:
#         if line.strip():
#             f2.write(line)

#7.Find the longest line in the file
# src = "/Users/saurabhvalunjkar/Python/PythonProgramming/yashwantKanetkarProgrmas/sample.txt"
# with open(src,"r") as f:
#     longest = max(f,key=len)
#     print(longest.strip())

#8. Replace a word in the file
# src = "/Users/saurabhvalunjkar/Python/PythonProgramming/yashwantKanetkarProgrmas/sample.txt"

# oldword = "testing"
# newword = 'test'
# with open(src,"r") as f:
#     data = f.read()

#     updated = data.replace(oldword,newword)

# with open(src,"w") as f1:
#     f1.write(updated)

#9.Compare two files line by line
#file1 = "/Users/saurabhvalunjkar/Python/PythonProgramming/yashwantKanetkarProgrmas/sample.txt"
# file2 = "/Users/saurabhvalunjkar/Python/PythonProgramming/yashwantKanetkarProgrmas/sample2.txt"

# list_common= []
# list_diff = [] 

# with open(file1,"r") as file1, open(file2,"r")as file2:
#     data1 = file1.readlines()
#     data2 = file2.readlines()

#     for i in range(min(len(data1),len(data2))):
#         if data1[i]==data2[i]:
#             list_common.append(data1[i].strip())
#         else:
#             list_diff.append((i+1,data1[i].strip(),data2[i].strip()))

# print(list_common)
# print(list_diff)

#10.Store list of numbers into file and read back
# src = "/Users/saurabhvalunjkar/Python/PythonProgramming/yashwantKanetkarProgrmas/sample2.txt"

# list1 = [1,2,4,5,6,7,8]

# with open(src,"w") as f:
#     for val in list1:
#         f.write(str(val)+'\n')

# with open(src,"r") as f:
#     data = f.readlines()
    
# numbers = [int(line.strip()) for line in data]
# print(numbers)
    



        
    
 



