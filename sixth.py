#FUNCTIONS
# a=3
# b=2
# sum=(a+b)
# print(sum)

# def calculate(a, b):   #function definition (parameters)
#     sum=a+b
#     print(sum)
#     return sum

# calculate(3, 6)   #function call (arguments)
# calculate(5, 9)
# calculate(6, 7)

# def hello():
#     print("hello")

# hello()

#average of 3 numbers
# def average(a,b,c):
#     avg=(a+b+c)/3
#     print(avg)
#     return avg

# average(3,5,2)

# def product(a=2,b=5):  #default parameters
#     x=a*b
#     print(x)
#     return x
    
# product(3,3) 
# product() #can also give result using default parameters as arguments 

#PRACTICE
#Q1
# cities=["karachi","frankfurt","canberra"]
# bowlers=["amir","asif","starc","steyn","bumrah"]
# def length(list):
#     print(len(list))

# length(cities)
# length(bowlers)

#Q2
# def line(list):
#     for item in list:
#         print(item,end=" ")

# line(bowlers)

#Q3
# def factorial(n):
#     fact=1
#     for i in range(1, n+1):
#         fact *= i
#     print("factorial is", fact)

# factorial(4)
# factorial(8)

#Q4
# def convertor(usd):
#     pkr=usd*283
#     print(usd, "USD = ", pkr, "PKR")
#     return pkr

# convertor(int(input("enter usd value: ")))

#Q5
# def nature(n):
#     if(n%2==0):
#         print("EVEN")
#     else:
#         print("ODD")

# nature(int(input("enter number: ")))

#shorter way
# def nature(n):
#     print("even" if n%2==0 else "odd")

# nature(int(input("enter number: ")))

# RECURSION
# def show(n):     #recursive function
#     if(n==0):    #base case
#         return
#     print(n)
#     show(n-1) #function called in the same finction

# show(5) # 5,4(n-1),3(n-2),2(n-3),1

#factorial using recursion
# def fact(n):
#     if(n==0 or n==1):
#         return 1         # 1 is the default factorial of 0 and 1
#     return fact(n-1)*n

# print(fact(4))

#PRACTICE
#Q1
# def cal(n):
#     if(n==0):
#         return 0
#     return cal(n-1)+n

# print(cal(5))
# print(cal(12))

#Q2
# def print_list(list,idx):
#     if(idx==len(list)):
#         return
#     print(list[idx],end=" ")
#     print_list(list,idx+1)

# cities=["karachi","mumbai","new york","edinburgh","berlin","sydney"]
# print_list(cities,0)





