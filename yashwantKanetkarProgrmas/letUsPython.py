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

# seed = 6
# seedValue = seed + int(time.time())
# random.seed(seedValue)

# print(seedValue)


# print(random.randint(10,50))
# print(random.randint(10,50))
# print(random.randint(10,50))
# print(random.randint(10,50))
# print(random.randint(10,50))


# 4. Use trunc(),floor() and ceil() on numbers -2.8,-0.5,0.2,1.5 and 2.9 and understand the difference 

# #trunc rounds up or down towards zero
# print("Explaining the trunc() method")
# print(math.trunc(-2.8))#-2,0,0,1,2
# print(math.trunc(-0.5))
# print(math.trunc(0.2))
# print(math.trunc(1.5))
# print(math.trunc(2.9))

# #floor rounds down towards negative infinity
# print("Explaining the floor() method")
# print(math.floor(-2.8))#-3,-1,0,1,-3
# print(math.floor(-0.5))
# print(math.floor(0.2))
# print(math.floor(1.5))
# print(math.floor(-2.9))

# #ceil rounds down towards positive infinity
# print("Explaining the ceil() method")
# print(math.ceil(-2.8)) #-2,0,1,2,-2
# print(math.ceil(-0.5))
# print(math.ceil(0.2))
# print(math.ceil(1.5))
# print(math.ceil(-2.9))

#5. WAP to convert faren temp in celcius and print both temp
# tempFaren = float(input("Enter the temperature of the city(F) ::")) 

# tempCel = (tempFaren-32)*(5/9)

# print("Temperature in farenheit is. :: ",tempFaren)
# print("Temperature in celsius is. :: ",tempCel)

#6. Given 3 sides of triangle WAP to obtain and print 
# the values of 3 angles rounded to the next integer

# a=int(input("Enter value for side of triangle :: "))
# b=int(input("Enter value for side of triangle :: "))
# c=int(input("Enter value for side of triangle :: "))

# cosA = ((b**2)+(c**2)-(a**2))/(2*b*c)
# cosB = ((a**2)+(c**2)-(b**2))/(2*a*c)
# cosC = ((b**2)+(a**2)-(c**2))/(2*b*a)

# angleA = math.degrees(math.acos(cosA))
# angleB = math.degrees(math.acos(cosB))
# angleC = math.degrees(math.acos(cosC))

# angA = math.ceil(angleA)
# angB = math.ceil(angleB)
# angC = math.ceil(angleC)

# sum = angA+angB+angC

# print(angA)
# print(angB)
# print(angC)

# print (sum)

