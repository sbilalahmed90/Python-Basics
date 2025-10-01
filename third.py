#list(arrays)
# marks=[94.5,32.6,77.9,]
# print(marks)
# print(type(marks))
# print(len(marks))
# print(marks[1])

# student=["Bilal",88,"grade A",3.77]
# print(student)

#list slicing
# score=[22,33,44,55,66,77,88]
# print(score[1:4])
# print(score[:4])
# print(score[4:])
# print(score[4:len(score)])  #same function as line 15
# print(score[-2:-5])

#list functions
# list=[2,1,3,5,5]
# list.append(4)
# list.sort()
# print(list)
# list.sort(reverse=True)
# print(list)
# list.reverse()
# list.insert(2,"hi")
# print(list)
# list.remove(5)
# list.pop(1)
# print(list)

# TUPLES
tup=(1,3,5,7,9)
print(type(tup))
print(tup[2])

#empty tuple
tup1=()
print(tup1)

#tuple with single element
tup2=(3,)
print(tup2)

#slicing in tuples
tup3=(7,9,3,15,56,33,45)
print(tup3[1:5])
print(tup3[:5])
print(tup3[3:])
print(tup3[3:len(tup3)]) #same as line 50
print(tup3[-1:-5])

#functions of tuples
tup4=(2,2,3,4,5,5,6)
print(tup4.index(5))
print(tup4.count(2))

#ask a user to input name of 3 series and insert them in a list
# series=[]
# ser1=input("enter 1st series: ")
# ser2=input("enter 2nd series: ")
# ser3=input("enter 3rd series: ")
# series.append(ser1)
# series.append(ser2)
# series.append(ser3)

# series.append(input("enter 4th series: ")) #can also write like this
# print(series)

#check if a list is a palindrome
# list1=[1,2,1]
# list2=[1,2,3]
# copy_list1=list1.copy() #copy of list 1
# copy_list1.reverse()

# if(copy_list1 == list1 ):
#     print("palindrome")
# else:
#     print('not palindrome')

# #count no.of students with grade A in a tuple
# grade=("C","D","A","A","B","A")
# print(grade.count("A"))

# #store above grades in a list and sort from A to D (ascending order)
# grade=["C","D","A","A","B","A"]
# grade.sort() #ascending order
# print(grade)
# grade.sort(reverse=True) #descending order
# print(grade)
