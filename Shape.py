class Shape:
    def __init__(self , width , heigth):
        self.width = width
        self.heigth = heigth

    def area(self):
        return self.width * self.heigth
    

x = Shape(10 , 20)
y = Shape(20 , 40)
print(x.area())
print(y.area())
