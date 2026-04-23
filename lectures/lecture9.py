#1. Define a circle class to create a cisrcle with radius r using the constructor .
#Define an area method of the class which calculates the area of the circle.
#Define a perimeter method of the class which allows you to calculate the perimeter

# class Circle:
#     def __init__(self,radius):
#         self.radius = radius

#     __pi = 3.14
    
#     def calc_Area(self):
#         area = self.__pi*(self.radius**2)
#         return area
    
#     def calc_Peri(self):
#         perimeter = 2*self.__pi*self.radius
#         return perimeter
    
# cir = Circle(int(input("Enter the radius :: ")))
# circleArea = cir.calc_Area()
# circlePerimeter = cir.calc_Peri()

# print("Area of circle :: ",circleArea)
# print("Perimeter of circle :: ",circlePerimeter)


#2. Define an employee class with attributes role, department and salary. This class also
#contains a showDetails() method.
#Create an Engineer class that inherits the Employee and 


# class Emp:
#     def __init__(self,role,department,salary):
#         self.role =role
#         self.department = department
#         self.salary = salary

#     def showDetails(self):
#         print("Employee details are as follows :: ","\n","Role :: ",self.role,"\n","Department :: ",self.department,"\n",
#               "Salary :: ",self.salary)
        

# class Engineer(Emp):
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         super().__init__("Dev","IT",50000)


# e1 = Engineer("Rudar",33)
# e1.showDetails()

#3. Create a class called as Order which stores itema and its price .
# use dunder function __gt__() to convey that :
# order1>order 2 if the price of order1>order 2

# class Order:
#     def __init__(self, item,price):
#         self.item = item
#         self.price = price

#     def __gt__(self,ord2):
#         return self.price>ord2.price
    
# ord1 = Order("Apple",55)
# ord2 = Order("Oranges",23)

# print(ord1>ord2)








