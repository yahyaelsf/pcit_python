# grade = 85
# if grade >= 90 :
#     print("Excellent")
# elif grade >=70 :
#     print("good")
# elif grade >=80 :
#     print("very good")

# else :
#     print("you must keep going")
# nested if 
# is_login = True 
# is_admin = False
# if is_login : 
#     print("Login Successfully")
#     if is_admin : 
#         print("wlcome in admin")
#     else :
#         print("welcome user ")
# else : 
#     print("faild to Login")
# ternary condetion operator :
# is_admin = False
# print("wlcome in admin") if is_admin else print("welcome user ")
# start piont 
# count = 1
# while count <= 10 :
#     if count == 5 :
#         pass
#     print(count)
#     count = count + 1 # count += 1
# names = ["yahya" , "ali" , "samar" , "maryam" , "ahmed"]
# for name in range(len(names)) :
#     print(f"indes is {name} : name is {names[name]}")
# for x , y in enumerate(names) :
#     print(f"indes is {x} : name is {y}")
# new_names = list(enumerate(names))
# print(new_names)
# user = {
#     "name" : "yahya" ,
#     "age" : 28 ,
#     "gender" : "male" ,
#     "is_graduated" : True
# }
# for key , value in user.items() :
#     print(f"the key is : {key} , value is : {value}")
# count = 5
# skills = []
# while count >-0 :
#     skill = input("Enter Your value :")
#     skills.append(skill)
#     count -=1 

# print(skills) 
# list_names = ["yahya" , "ali" , "ahmed" , "samer"]
# bin = "1234"
# attempts = 3
# is_login = False
# while not is_login and attempts > 0 :
#     password = input("Enter your password :")
#     if password == bin :
#         print("Login Successfully")
#         is_login = True
#     else :
#         print("Faild to Login")
#         attempts -=1 

# while is_login :
#     name = input("Enter Your admin name :")
#     if name in list_names : 
#         print("Select the operation :")
#         print("1_Edit your username")
#         print("2_Delete Your username :")
#         choise = input("Enter Your choise :")
#         if choise == "1" :
#             new_val = input("Enter new value :")
#             indx = list_names.index(name)
#             list_names[indx] = new_val
#             print("the username Edit Successfully")
#         elif choise == "2" :
#            list_names.remove(name) 
#            print("the username deleted Successfully")
#         else : 
#             print("Wrong in choise")
#         print(list_names)
#     else : 
#         print("the input name not exist")
# list1 = [1 , 2, 3,4 ,5]
# my_itreator = iter(list1)
# print(next(my_itreator))
# print(next(my_itreator))
# print(next(my_itreator))
# print(next(my_itreator))
# print(next(my_itreator))
# print(next(my_itreator))
