# def calculter(num1 , num2 , operator = "+" ):
#     result = 0
#     if operator == "+" :
#         result =  num1 + num2
#     elif operator == "-" :
#         result = num1 - num2
#     elif operator == "*" :
#         result = num1 *  num2
#     else :
#         result = num1 / num2
#     return result

# result = calculter(num2 =2 , num1=5 , operator="/")
# print(result)

# def add(operator , *args) :
#     ruselt = 1
#     for i in args :
#       ruselt = eval(f"{ruselt}  {operator}  {i}")
#     return ruselt
    


# value = add("*", 10 , 30 ,20)
# print(value)
# def info(**params) :
#     for key , value in params.items() : 
#         print(f"the key is : {key} and value is : {value}")

# data = {
#     "first_name" : "yhaya" , 
#     "last_name" : "elsaftawi" ,
#     "age" : 28
# }      
# info(**data)
# def info():
#     global x
#     x = 0 
#     print("welcome")

# info()
# print(x)

# def factorial(n):
#     if n == 1:       # base case
#         return 1
#     return n * factorial(n - 1)

# print(factorial(10))
# import math
# import datetime as dt
# import mathplotlip as plt
# print(dir(datetime.datetime))
# print(datetime.datetime.now().time().microsecond)
# print(dt.datetime(2025 , 10 , 31).date())
# import login as lg
# print(lg.login("yahya" , "123456**"))
from termcolor import colored 
print(colored("welcome" , color="light_green"))

