import random
import string
#Random Password Generator
#This is a simple way
# value = string.ascii_letters+string.digits+string.punctuation
# passLen = int(input("What should be the length of the password(in number :: "))
# password = ""
# for i in range(passLen):
#     password+=random.choice(value)
# print(password)


#Complex way
#Called as list comprehension way
value = string.ascii_letters+string.digits+string.punctuation
passLen = int(input("What should be the length of the password(in number :: "))

res="".join((random.choice(value))for i in range(passLen))
print(res)


