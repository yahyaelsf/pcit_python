# def check_password(password) :
#     length = len(password) >= 8
#     is_digit = any(char.isdigit() for char in password)
#     # is_digit = False 
#     # nums = "123456789"
#     # for i in password:
#     #     if i in nums :
#     #         is_digit = True
#     #         break
#     is_upper = any(char.isupper() for char in password)
#     speials = "!@#$%^&*"
#     is_speial = any(char in speials  for char in password)
#     total = sum([length , is_digit , is_upper , is_speial ])
#     if total == 4 : 
#         print("Password is Vary Strong")
#     elif total == 3 : 
#         print("Password is Strong")
#     elif total == 2 :
#         print("Password is midd")
#     elif total == 1 : 
#         print("Password is week")
#     else :
#         print("change your password")


# check_password("ahya2026**")

# file = open("data.txt", "r+")
# print(file.tell())
# file.seek(10)
# print(file.tell())
# file.write(" welcome ")
# file.close()
# with open("data.txt", "r+") as file:
#     print(file.tell())
#     file.seek(10)
#     print(file.tell())
#     file.write(" welcome ")
# try :
#     # x = int(input("Enter your age :"))
#     # print(x)
#     print("your number is true")
#     print(5/0)
# except ValueError:
#     print("value error")
# except NameError :
#     print("variable not defind")
# except : 
#     print("Error an acuured")
# finally :
#     print("End execution")

# if x == 5 :
#      raise Exception("age must be bigger than 5")   
