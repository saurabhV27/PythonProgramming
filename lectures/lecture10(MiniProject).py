import random

#Solution 1 (using recurision)

# class GuessingGame :
#     def __init__(self,num):
#         self.num = num


#     def numberGuess(self):

#         userInput= int(input("Guess the Numer :: "))

#         if(userInput==self.num):
#             print("You have guessed the number",self.num ,"correct !! yay!!")
            
#         elif(userInput>self.num):
#             print("Incorrect guess!! Try Again !!") 
#             print("HINT :  Your number is greater than the expected number !!")
#             return self.numberGuess()
#         elif(userInput<self.num):
#             print("Incorrect guess!! Try Again !!") 
#             print("HINT :  Your number is smaller than the expected number !!")
#             return self.numberGuess()


# luckyNo = random.randint(1,100)
# gg = GuessingGame(luckyNo)
# gg.numberGuess()

#Solution 2(using loop)

randomNo = random.randint(1,100)
attempt= 0

while True:

    userInput = int(input("Guess the number :: "))
    attempt+=1

    if userInput==randomNo:
        print("You have guessed it right in",attempt,"attempts !! ")
        break
    elif userInput>randomNo:
        print("Incorrect!! Please try again !!")
        print("HINT : Number entered is greater than the expected number")
        
    else:
        print("Incorrect!! Please try again !!")
        print("HINT : Number entered is smaller than the expected number")
        