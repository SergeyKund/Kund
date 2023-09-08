class Point:
    x = 0
    y = 0
    z = 0
    def __init__(self, x, y, z):
        if (type(x) in (int, float)) and (type(y) in (int, float)) and (type(z) in (int, float)):
            self.x = x
            self.y = y
            self.z = z
        else:
            raise ValueError('Invalid input for x and y coordinates')


    def __str__(self):
        return f'Point [{self.x}:{self.y}]'

class Triangle(Point):
    def pir(self):
        s = (self.x + self.y + self.z) / 2
        plo = (s * (s - self.x) * (s - self.y) * (s - self.z)) ** 0.5
        return f'{plo}'







x = 12
y = 12
z = 12

triangle = Triangle (x, y, z)
triangle = triangle.pir()
print(triangle)



