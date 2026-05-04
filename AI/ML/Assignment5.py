# class Products :
#     count = 0

#     def __init__(self,name,price):
#         self.name = name
#         self.price = price
#         Products.count+=1

#     def get_product(self):
#         print(f"The price of {self.name} is Rs. {self.price}")

#     @classmethod
#     def get_count(cls):
#         print(f"The total count is {cls.count}")

#     @staticmethod
#     def product_discount(price,discount):
#         product_price = price-(price*(discount/100))
#         print(f"Discount offered is {discount}% and the final price is Rs. ",product_price)

# p1 = Products("laptop",90_000)
# p2 = Products("iphone",100_000)

# p1.get_product()
# p2.get_product()

# Products.get_count()

# Products.product_discount(90000,8)

#1. create a bankaccount class with attributes (account_number,owner name and balance) 
# and add methods to deposit, withdraw and check balance.

# class BankAccount:
#     def __init__(self,account_number,owner_name,balance):
#         self.account_number = account_number
#         self.owner_name = owner_name
#         self.__balance = balance
    
#     def check_balance(self):
#         return self.__balance
    
#     def deposit(self,amount_depo):
#         if amount_depo<=0:
#             print("Please enter a Valid value")
#         else:
#             self.__balance+=amount_depo
#             print(f"Deposited {amount_depo} in Account : {self.account_number}")
#             print(f"The updated balance is Rs. {self.__balance}")
    
#     def withdraw(self,amount_withdraw):
#         if amount_withdraw<=0:
#             print("Invalid Amount")
#         elif(amount_withdraw > self.__balance):
#             print("Insufficient Funds")
#         else:
#             self.__balance-=amount_withdraw
#             print(f"Rs. {amount_withdraw} withdrawn from Account {self.account_number}")
#             print(f"The updated balance is Rs. {self.__balance}")

# owner1 = BankAccount(1234,'sid',10000)
# bal = owner1.check_balance()
# print(f"Balance is Rs. {bal}")
# owner1.deposit(50_000)
# owner1.withdraw(20_000)

#2. Create a class book  with the following attribute :
# Title
#Author
#list of reviews
#And add methods to add a new review, count reviews display all reviews
#use Encapsulation

# class Book:

    
#     def __init__(self,title,author):
#         self.title=title
#         self.author = author
#         self.__review=[]
    

#     def add_review(self):
#         user_review = input("Please write a review :: ")
#         self.__review.append(user_review)
    
#     def review_count(self):
#         print(f"The count of reviews is :: {len(self.__review)}")

#     def display_review(self):
#         print(f"{self.__review}")


# b1=Book("How","who")
# b1.add_review()
# b1.review_count()
# b1.display_review()

#3. Create a class student with private attributes _name,_roll_no and _marks
#provide getter setter methods for validation.(Ex. marks cant be negative , roll 
# number has to be between 1 to 100 and name cannot be empty. )

# class Student:
#     def __init__(self):
#         self.__name = ''
#         self.__roll_no = 1
#         self.__marks=0

#     def get_attributes(self):
#         return(f"Student : {self.__name} having roll no : {self.__roll_no} has obtained {self.__marks} marks")
    
#     def set_name(self):
#         while True:
#             userInput = input("Please enter the name of the student :: ")
#             if(userInput == "" or userInput==" "):
#                 print("Name cannot be empty !! Try again")
#             elif any(ch.isdigit() for ch in userInput):
#                 print("Invalid name please try again !!")
#             else:
#                 self.__name=userInput
#                 break
    
#     def set_roll_no(self):
#         while True:
#             userInput = int(input("Enter the Roll No.(between 1-100)"))
#             if(userInput==""):
#                 print("RollNo cannot be empty try again!!")
#             elif (userInput<=0 or userInput>100):
#                 print("Invalid roll no try again!!")
#             else:
#                 self.__roll_no=userInput
#                 break
    
#     def set_marks(self):
#         while True:
#             userInput = int(input("Enter the marks(between 1-100)"))
#             if(userInput==""):
#                 print("RollNo cannot be empty try again!!")
#             elif (userInput<0 or userInput>100):
#                 print("Invalid roll no try again!!")
#             else:
#                 self.__marks=userInput
#                 break
    
            

# s1 = Student()
# s1.set_name()
# s1.set_roll_no()
# s1.set_marks()
# student_info = s1.get_attributes()
# print(student_info)


#4. Create a class Shape with a method area().
#  Create subclasses circle,rectangle and triangle that 
#  override area() method

# class Shape:
#     def __init__(self,cir_rad=0,rec_len=0,rec_bre=0,tri_base=0,tri_hei=0):
#         self.cir_rad=cir_rad
#         self.rec_len=rec_len
#         self.rec_bre=rec_bre
#         self.tri_base=tri_base
#         self.tri_hei=tri_hei
    
#     def area(self):
#         pass

# class Circle(Shape):
#     def __init__(self,cir_rad):
#         super().__init__(cir_rad=cir_rad)
#     def area(self):
#         circle_area = 3.14*(self.cir_rad**2)
#         print(f"Area of a circle :: {circle_area}")

# class Rectangle(Shape):
#     def __init__(self,rec_len,rec_bre):
#         super().__init__(rec_len=rec_len,rec_bre=rec_bre)
#     def area(self):
#         rectagle_area = self.rec_len*self.rec_bre
#         print(f"Area of a Rectangle :: {rectagle_area}")

# class Triangle(Shape):
#     def __init__(self,tri_base,tri_hei):
#         super().__init__(tri_base=tri_base,tri_hei=tri_hei)
#     def area(self):
#         triagle_area = (self.tri_base*self.tri_hei)/2
#         print(f"Area of a Triangle :: {triagle_area}")

# c1=Circle(5)
# c1.area()
# r1=Rectangle(6,3)
# r1.area()
# t1=Triangle(4,8)
# t1.area()

# #5. Create a base class Vehicle with attributes like brand and model.
# # Create 2 subclasses Car and Bike that add extra attributes - Seats (in car)
# # engine-cc(in bike)
# # Concept to use ->Inheritance

# class Vehicle:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model

# class Car(Vehicle):
#     def __init__(self,brand,model):
#         super().__init__(brand,model)
#         self.seats = input("Enter the type of seat :: ")

#     def new_car(self):
#         print(f"Please put {self.seats} in my {self.brand} -{self.model} car ")


# class Bike(Vehicle):
#     def __init__(self,brand,model):
#         super().__init__(brand,model)
#         self.engine = int(input(" Please enter the power of the bike :: "))
        
    
#     def power_bike(self):
#         print(f"The bike {self.brand}- {self.model} should have {self.engine} cc engine")

# c1=Car("Toyota","ignis")
# c1.new_car()

# b1=Bike("Triumph","Street Triple 765")
# b1.power_bike()

#6.Create an abstract class Employee with an abstract method calculate_salary().
# Create sub class Intern,FullTimeEmployee and ContractEmployee that implement 
# the method differently
# from abc import ABC,abstractmethod
# class Employee(ABC):
    
#     @abstractmethod
#     def calculate_salary(self):
#         pass

# class InternEmp(Employee):
#     def __init__(self):
#         self.salary=int(input("Enter the salary for intern :: "))

#     def calculate_salary(self):
#         print(f"The salary for an intern is {self.salary}")

# class ContractEmp(Employee):
#     def __init__(self):
#         self.salary=int(input("Enter the salary for Contract Emp :: "))

#     def calculate_salary(self):
#         print(f"The salary for an ContractEmp is {self.salary}")

# class FullTimeEmp(Employee):
#     def __init__(self):
#         self.salary=int(input("Enter the salary for FullTime :: "))

#     def calculate_salary(self):
#         print(f"The salary for an FullTime is {self.salary}")

# i1=InternEmp()
# i1.calculate_salary()

# c1=ContractEmp()
# c1.calculate_salary()

# f1 = FullTimeEmp()
# f1.calculate_salary()
    

# #7. Crete a class Person taht allows the constructor to work with :
# #name
# #name+age
# #name+age+address

# #As direct constructor overloading are not allowed but we have to 
# # use default parameters to simulate constructor overloading

# class Person:
#     def __init__(self,name,age=0,address=None):
#         self.name=name
#         self.age=age
#         self.address=address
    
#     def person(self):
#         return (f"Name : {self.name} Age: {self.age} Address : {self.address} ")
    
# p1=Person("Sav")
# Person1 = p1.person()

# p2=Person("Sav",33)
# Person2 = p2.person()

# p3=Person("Sav",33,"India")
# Person3 = p3.person()

# print(Person1)
# print(Person2)
# print(Person3)

#8. Create a class Player with
# a class variable player_count
# instance variable name and level 

#track how many players were created

# class Player:
#     player_count = 0

#     def __init__(self,name,level):
#         self.name = name
#         self.level=level
#         Player.player_count+=1
#         self.id = Player.player_count


#     def create_player(self):
#         return(f"Player {self.id} -> Name : {self.name} Level : {self.level}")


# p1= Player("Priya",2)
# p2= Player("Nishu",4)

# Player1 = p1.create_player()
# Player2 = p2.create_player()

# print(Player1)
# print(Player2)


#9. Create the following classes Herbivore,Carnivore and Omnivore 
# with some attributes and methods. Then create a class Bear that inherits
#  from all the above classes to showcase how multiple inheritance works

# class Herbivore:
#     def __init__(self,food):
#         self.food=food
    
#     def animal(self):
#         print(f"A herbivore eats {self.food} when hungry")

# class Carnivore:
#     def __init__(self,hunt):
#         self.hunt=hunt
    
#     def ani(self):
#         print(f"A carnivore hunts {self.hunt} for food")

# class Omnivore:
#     def __init__(self,eats):
#         self.eats=eats
#     def anim(self):
#         print(f"An omnivore can survive on {self.eats}")

# class Bear(Herbivore,Carnivore,Omnivore):
#     def __init__(self,type,eats,hunt,food):
#         self.type=type
#         Herbivore.__init__(self,food)
#         Carnivore.__init__(self,hunt)
#         Omnivore.__init__(self,eats)

#     def bear_type(self):
#         print(f"Bear can be {self.type}")


# b1=Bear("Brown and polar","grass","meat","Plant and Meat")
# b1.ani()
# b1.animal()
# b1.bear_type()




