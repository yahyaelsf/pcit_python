class Person():
    # class attribute
    count = 0
    __salary = 0
    # is instance attribute (paramters)
    def __init__(self , name , age , gender):
        self.name = name
        self.age = age 
        self.gender = gender
        Person.count +=1 
    # instance function
    def info(self):
        return f"My name is {self.name} , age {self.age} and gender {self.gender}"
    # class function 
    @classmethod
    def showCounter(cls):
        return f"number of objects is {cls.count}"
    def get_salary(cls):
        return cls.__salary
    def set_salary(cls , new_value ) :
        cls.__salary = new_value
    @staticmethod
    def voice():
        return "sssss"

    

# class Person2():
#     pass
    

# p1 = Person("yahya" , 28 , "male")
# p1.set_salary(2500)
# print(p1.voice())
# Person.count = 20
# print(Person.count)

# name = "yahya"
# class Student(Person , Person2):
#     def __init__(self , name , age , gender , level ):
#         # Person.__init__(self , name , age , gender)
#         super().__init__(name , age , gender)
#         self.level = level

#     def info(self):
#         return f"level is {self.level}"

# p1 = Person("yahya" , 26 , "male" )
# s1 = Student("ali" , 26 , "male" , "11")
# print(p1.info())
# print(s1.info())

# print("a" + "b")
# print(5 + 6)
# print(True + True)