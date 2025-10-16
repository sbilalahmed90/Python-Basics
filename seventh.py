# FILE I/O

# read mode

# f=open("demo.txt","r")
# data=f.read()
# print(data)
# print(type(data))
# f.close()

# f=open("demo.txt","r")
# a=f.read(6)  # read 6 characters
# print(a)
# f.close()

# f=open("demo.txt","r")
# b=f.readline() # read one line at a time
# print(b)
# c=f.readline()
# print(c)
# f.close()

# write mode

# f=open("demo.txt","w")  #truncates old data of the file and over writes the new one.
# f.write("i hate my university.369")
# f.close()


# f=open("demo.txt","a")  #append the data in the file
# f.write("\neveryone is fake")
# f.close()

# read and write mode
# f=open("demo.txt","r+") #file won't be truncated
# f.write("abcde")
# print(f.read()) #will start reading from where data is over written and the pointer is pointing.
# f.close()

# f=open("demo.txt","w+") #file will be truncated
# print(f.read()) 
# f.write("abcde")
# f.close()

# f=open("demo.txt","a+") #file won't be truncated
# print(f.read()) 
# f.write("\tabcde") #text will be appended(added at the end)
# f.close()

# "with" syntax
# with open("demo.txt","r") as f:
#     print(f.read())
#     # "with" will automatically close the file, no need of f.close()

# deleting a file using "os" module
# import os
# os.remove("sample.txt")

# practice
# with open("practice.txt","w") as f:
#     f.write("Hi everyone\nwe are learning file I/O\n")
#     f.write("using python\nI like programming in python.")

# with open("practice.txt","r") as f:
#     data=f.read()

# new_data=data.replace("python","java")  #as file has strings
# print(new_data)

# with open("practice.txt","w") as f:
#     f.write(new_data)

# def check():
#     word="learning"
#     with open("practice.txt","r") as f:
#         data=f.read()
#         if(word in data):         #if the word exist in data
#             print("found")
#         else:
#             print("not found")

# check()

# def checkline():
#     word="learning"  
#     data=True        #value is true for initializing the loop. at empty string loop won't be executed
#     line=1
#     with open("practice.txt","r") as f:
#         while data:              #till data has a valid value the loop will iterate
#             data=f.readline()
#             if(word in data):
#                 print(line)
#                 return
#             line+=1

#     return -1

# checkline()

      

     

