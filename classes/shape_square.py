class shape:
    def __init__(self):
        pass

    def area(self):
        return 0
    

class square(shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length
    
s = shape()
print("Shape area:", s.area())

sq = square(5)
print("Square area:", sq.area())