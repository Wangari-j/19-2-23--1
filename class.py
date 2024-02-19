class Triangle:
    base = 0
    height = 0

    def __init__(self,base, height):
      self.base = base
      self.height = height

    def getArea(self):
      result = self.base * self.height/2
      return result

t1 = Triangle(4,12)
print(t1.getArea())

t2 = Triangle(8,10)
print(t2.getArea())

t3 = Triangle(4,10)
print(t3.getArea())

