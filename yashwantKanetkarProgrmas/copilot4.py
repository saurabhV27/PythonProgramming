#1. Revese a string


# while True:
#     user_input= input("Enter a string :: ")
#     rev=""
#     if user_input.isdigit():
#         print("Invalid input !! Please try again")
#     else:
#         for val in range(0,len(user_input)):
#             rev=user_input[val]+rev

#         print(rev)
#         break

#2. Count the vowels and consonants
# user_Input=input("Enter a String ")
# count_vowel = 0
# count_conso = 0

# if(user_Input.isdigit()):
#     print("Invalid input")
# else:
#     stri = user_Input.lower()
#     for ch in stri:
#         if ch.isalpha():
#             if(ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u'):
#                 count_vowel+=1
#             else:
#                 count_conso+=1
# print(f"Vowels :: {count_vowel}")
# print(f"Consonants :: {count_conso}")

#3. Check Anagram
# def is_anagram(str1,str2):
#     str1 = str1.replace(" ","").lower()
#     str2 = str2.replace(" ","").lower()

#     if(sorted(str1) == sorted(str2)):
#         return True
#     else:
#         return False

# str1 = input("Enter a String :: ")
# str2 = input("Enter a String :: ")

# if is_anagram(str1,str2):
#     print("Strings are anagram")
# else:
#     print("Strings are not anagram")

#4. Remove Duplicates from a String
# user_input = input("Enter a string :: ")
# user_input = user_input.replace(" ","").lower()
# dup=""
# string=""
# for ch in user_input:
#     if ch in string:
#         if ch in dup:
#             continue
#         else:
#             dup+=ch
#     else:
#         string+=ch
# print(string)
# print(dup)

#5. Find frequency of characters

# user_input = input("Enter a string :: ").replace(" ","").lower()
# freq={}
# print(type(freq))
# for ch in user_input:
#     freq[ch] = freq.get(ch,0)+1

# print(freq)

# #6. Check substring presence
# user_input = input("Enter a String:: ").lower()
# substring = input("Enter a String:: ").lower()

# if substring in user_input:
#     print(f"{substring} is present")
# else:
#     print("Not present")

#7. Longest word in sentence

# user_input = input("Enter a sentence :: ")
# word_length =0
# longest = []

# for word in user_input.split(" "):
#     if(len(word)>word_length):
#         word_length=len(word)
#         longest = [word]
#     elif len(word) == word_length:
#         longest.append(word)
        
# print(longest)
    






 
 
