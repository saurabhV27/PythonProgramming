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

src = "/Users/saurabhvalunjkar/Python/PythonProgramming/yashwantKanetkarProgrmas/sample.txt"
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


 



