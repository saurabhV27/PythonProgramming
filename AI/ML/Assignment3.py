#Student Enrollment
#1. Given a list of tuples with info (name ,subject)
#-> List all unique courses 
#->list student erolled in english
#->Create dictionary (student, set of courses)

# info=[("Alice","Math"),
#       ("Bob","Science"),
#       ("Alice","Science"),
#       ("Charlie","Math"),
#       ("Bob","Math"),
#       ("Alice","English"),
#       ("Charlie","English")
#       ]

# course = set()

# # for val in info:
# #     course.add(val[1])
# #     if val[1]=="English":
# #         print(f"{val[0]} have subject as english")

# # print(course)

#Alternate way

# info=[("Alice","Math"),
#       ("Bob","Science"),
#       ("Alice","Science"),
#       ("Charlie","Math"),
#       ("Bob","Math"),
#       ("Alice","English"),
#       ("Charlie","English")
#       ]

# dict={}

# for name,course in info:
#     if course=="English":
#         print(name)
    
#     if name not in dict:
#         dict[name]=[]
#     dict[name].append(course)

# print(dict)
    






