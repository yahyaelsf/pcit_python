names = ["yahya" , "ahmed" , "ali" , "yahya"]
# names.append("sss")
# names.insert(1 , "aaa")
# names[0] = "elsaftawi"
# names.remove("yahya")
# names.pop(1)

# print("ahmeds" in names)
# tuple 

# typle1 = ( 1 , 2 , 3 , 4)
# print(typle1[0])

# set1 = {1 , 2 , 2 , 3 ,5}
# fruits = {"apple", "orange", 
# "banana"}
# fruits.pop()
# set1 = {1,2,3}
# set2 = {3,4,5}
# print(set1.difference(set2))
# dic ={
#     "id" : 2,
#     "name" : "yahya" ,
#     "skills" : ["python" , "html" , "css"],
#     "age" : 26,
# }
# new_dic = {"is_emploeed" : True}
# dic.update(new_dic)
# dic |= {"is_emploeed" : True}
# dic.pop("age")
# print(dic)
# currency = {
#     "usd" : 2.9,
#     "eur" : 4.5 ,
#     "god" : 4.2
# }
# select_cur = input("Enter your curencu enverter : (usd , eur , god) :")
# amount = int(input("Enter your amount :"))
# value = currency.get(select_cur)
# total = amount * value
# print(f"the total number is {total} TLS")

# if condition :
# age = 30 
# if age <= 25 :
#     print("you are stell young")
# elif age > 25 :
#     print("You are Youth ")
# else :
#     print("you are old man")
for i in range(1,101):
    if i % 3 == 0 and i % 5==0 :
        print("FizzBuzz")
        
    elif i % 5 == 0 :
        print("Buzz")
    elif i % 3 == 0  :
        print("Fizz")
    else :
        print(".....")
