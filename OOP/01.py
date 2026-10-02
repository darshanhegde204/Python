class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __add__(self,other):
        return self.x+other.x

obj1=Point(10,20)
obj2=Point(30,40)
print(obj1.__add__(obj2))