class Rectangle:

    def __init__(self,length,breadth,cost=1):
        self.length = length
        self.breadth = breadth
        self.cost= cost

    def perimeter(self):
        return 2* (self.length + self.breadth)

    def area(self):
        return self.length * self.breadth

    def price_unit(self):
        area = self.area()
        return area*self.cost


r1= Rectangle(100,100,2)

print(r1.perimeter())
print(r1.area())
print(r1.price_unit())
