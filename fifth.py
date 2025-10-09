#LOOPS
#WHILE loop
# count=1 #initialization
# while count<=5:
#     print("hello")
#     count += 1

# print(count)

#print numbers from 1 to 5
# i=1
# while i<=5:
#     print(i)
#     i+=1

#reverse order
# i=5
# while i>=1:
#     print(i)
#     i-=1

#questions
#  Q1
# i=1
# while i<=100:
#     print(i)
#     i+=1

#  Q2
# i=100
# while i>=1:
#     print(i)
#     i-=1

#  Q3
# i=1
# n=int(input("enter number: "))
# while i<=10:
#     print(n*i)
#     i+=1

#  Q4
# num=[1,4,9,16,25,36,49,64,81,100]
# idx=0
# while idx < len(num):
#     print(num[idx])  #nums[0],nums[1] ...   
#     idx+=1

#  Q5
# num=(1,4,9,16,25,36,49,64,81,100)
# x=int(input("enter number you want to search: "))
# i=0
# while i<len(num):
#     if(num[i]==x):
#         print("found at index", i)
#     i+=1

#BREAK AND CONTINUE
# i=1
# while i<=5:
#     print(i)
#     if(i==3):
#         break  #will terminate the loop at 3
#     i+=1

# i=0
# while i<=5:
#     if(i==2):
#         i+=1
#         continue  #will print from 0 to 5 except 2
#     print(i)
#     i+=1

#print odd numbers till 10
# i=1
# while i<=10:
#     if(i%2==0):
#         i+=1
#         continue 
#     print(i)
#     i+=1

#print even numbers till 10
# i=1
# while i<=10:
#     if(i%2!=0):
#         i+=1
#         continue 
#     print(i)
#     i+=1

#FOR LOOP
# list=[1,2,3,4,5,6]
# for values in list:
#     print(values)

# str="bilal ahmed"
# for char in str:
#     print(char)
# else:              #optional to use
#     print("end")

#PRACTICE
#Q1
# a=[1,4,9,16,25,36,49,64,81,100]
# for num in a:
#     print(num)

#Q2
#linear search
# tup=(1,4,9,16,25,36,64,81,100)
# x=int(input("enter number from the tuple: "))
# for num in tup:
#     if(num==x):
#         print("number found ",num)
#         break
#     print(num)

#2nd way
# tup=(1,4,9,16,25,36,64,81,100)
# x=int(input("enter number from the tuple: "))
# idx=0
# for num in tup:
#     if(num==x):
#         print("number found at ",idx)
#     idx+=1

#RANGE FUNCTION
# for el in range(5):   #range(stop)
#     print(el)

# for el in range(2,5):   #range(start,stop)
#     print(el)   

# for el in range(2,10,2):   #range(start,stop,step)
#     print(el)   

#PRACTICE
#Q1
# for i in range(1,101):
#     print(i)

#Q2
# for i in range(100,0,-1):
#     print(i)

#Q3
#Multiplication table
# n=int(input("enter number: "))
# for i in range(1,11):
#     print(n*i)

#PASS statement
# for i in range(10):
#     pass

# if (i>=5):
#     pass

# print("the above loop is left empty for future code")

#PRACTICE
#Q1
# find the sum of first n natural numbers. (using while and for)
#natural numbers sum = 1+2+3+4+...
# n=int(input("enter number:"))
# sum=0
# for i in range(1,n+1):
#     sum+=i
# print("total sum = ",sum)

# n=int(input("enter number:"))
# sum=0
# i=1
# while i<=n:
#     sum+=i
#     i+=1
# print("total sum = ",sum)

#Q2
# find the factorial of first n natural numbers. (using for and while)
# n=int(input("enter number:"))
# factorial=1
# for i in range(1,n+1):
#     factorial*=i
# print("factorial is", factorial)

# n=int(input("enter number:"))
# fac=1
# i=1
# while i<=n:
#     fac*=i
#     i+=1
# print("factorial is", fac)