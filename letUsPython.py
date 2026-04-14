import math
import random
import time
#1. Swap 2 numbers without using the third
# a=5
# b=6
# print(a,b)
# a=a+b
# b=a-b
# a=a-b
# print (a,b)


#2. write a program that makes use of trignometric functions available in math module

#angle_deg =60

#Converting normal angle to radians as the Trignometric functions expect radian

# angle_rad = math.radians(angle_deg)

# print (angle_rad)
# #Basic Trignometric function
# print("Sin : ",math.sin(angle_rad))
# print("Cos : ",math.cos(angle_rad))
# print("Tan : ",math.tan(angle_rad))

# #Inverse trignometric function expect value and not the angle so fetch the value

# value = 0.04719

# print("Asin : ",math.degrees(math.asin(value)))
# print("Acos : ",math.degrees(math.acos(value)))
# print("Atan : ",math.degrees(math.atan(value)))

# print(math.hypot(3,4))

#3. WP to generate 5 random number between 10 to 50 with seed value 6
#    make sure you change the seed value everytime you execute 
#     the program by associating it with time of execution

seed = 6
seedValue = seed + int(time.time())
random.seed(seedValue)

print(seedValue)


print(random.randint(10,50))
print(random.randint(10,50))
print(random.randint(10,50))
print(random.randint(10,50))
print(random.randint(10,50))