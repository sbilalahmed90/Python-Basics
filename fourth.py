#Dictionary
# info={
#          "key": "value",
#         "name": "BILAL",
#         "number": 337788,
#         "is_adult":True,
#         "courses":["python","oop","sql"] #list
# }
# print(info)
# print(type(info))
# print(info["number"])
# info["surname"]="AHMED" #addition in the dictionary
# print(info)
# info["name"]="SAAD"
# print(info) #overwrites the value of the old key

#Nested Dictionary
# student={
#     "name" : "BILAL",
#     "score": {
#                "physics": 90,
#                "chemistry": 88,
#                "maths": 85

#     }
# }
# print(student)
# print(student["score"]["maths"])

# #dictionary methods
# print(student.keys())
# print(list(student.keys()))  #type casting in the form of list
# print(student.values())
# print(student.items())
# print(student.get("name"))
# (student.update({"city":"karachi"})) #donot works with the print function
# print(student)

#Sets
# set={1,2,3,4,5,"bilal"}
# print(set)
# print(type(set))

# #repeated values are stored only once
# set2={1,1,2,2,3,3,"bilal","bilal"}
# print(set2)

# collection={}  #empty dictionary
# collection2=set()  #empty set
# set methods
# collection2.add(1)
# collection2.add(2)
# collection2.add(3)
# collection2.remove(1)
# collection2.add(("bilal","ahmed","ali"))
# collection2.pop() #returns random value/s from the set
# collection2.clear() #empties the set
# print(collection2)
# set1={1,2,3}
# set2={2,3,4}
# print(set1.union(set2))
# print(set1.intersection(set2))

#practice questions
#Q1
# dictionary={
#     "table": ["a piece of furniture","list of facts and figures"], #list
#     "cat": "a small animal"

# }
# print(dictionary)

#Q2
# classroom={"python","java","c++","python","javascript","java","python","java","c++","c"}
# print(len(classroom))  #number of rooms required

#Q3
# marks={}
# x=int(input("enter physics marks: "))
# y=int(input("enter chemistry marks: "))
# z=int(input("enter maths marks: "))

# marks.update({"physics":x})
# marks.update({"chemistry":y})
# marks.update({"maths":z})

# print(marks)

#Q4
# set={9,"9.0"}
# print(set)