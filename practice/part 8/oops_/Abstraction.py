# Abstraction
# hiding the implementation details of a class and only showing the esential features to the user.


class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.cluch = False
        
    def start(self):
        self.cluch = True
        self.acc = True
        print("car started..")        
        
car1 = Car()        
car1.start()