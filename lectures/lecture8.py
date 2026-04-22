#1. Create a student class and take name marks of 3 subject as argument in constructor 
#then create a method to calculate the average.

# class Student:
#     def __init__(self,name,sub1,sub2,sub3):
#         self.name = name
#         self.sub1 = sub1
#         self.sub2 = sub2
#         self.sub3 = sub3
    
#     def calc_Avg(self):
#         avg = (self.sub1+self.sub2+self.sub3)/3
#         print(avg)

# s1 = Student("Karan",93,74,63)
# s1.calc_Avg()

#Alternate Solution

# class Student :
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks

#     def calc_Avg(self):
#         sum=0
#         for el in self.marks:
#             sum=sum+el
#         print("Average is ::",sum/3)

# List = (91,92,95)
# s1 = Student("Asta",List)
# s1.calc_Avg()



#2.Create a account class with 2 attributes balance and account number.
# Create methods for credit debit and printing the balance


# class Account :
#     def __init__(self,balance,accNo):
#         self.balance = balance
#         self.accNo = accNo
    
#     def credit(self,cred):
#         self.balance+=cred
#         print(cred," rupees credited to your account")

    
#     def debited(self,deb):
#         if(self.balance<deb):
#             print("ERROR : Insufficient Funds")
#         else:
#             self.balance-=deb
#             print(deb, " rupees debited from your account")
    
#     def accBal(self):
#         accNo = int(input("Enter the account Number :: "))
#         if(accNo==self.accNo):
#             print("Your Current Balance is :: ",self.balance)
#             return
#         else:
#             print("Incorrect Account Number !!")
#             self.accBal()
        


# ac1 = Account(10000,1234)
# ac1.debited(2000)
# ac1.credit(500)
# ac1.accBal()
        
    


