
from abc import abstractmethod, ABC

"""ABC is a class from the abc module in Python. If we extend any class
with ABC and include any abstraction methods,then the classes inherited
from this class will have to mandatorily implement those abstract methods. """

class Shape(ABC):   # Here, Shape is a parent inherited from ABC class. It has an abstraction method "area" and "perimeter"
    
    
    @abstractmethod  #  method is annotated with an abstractmethod keyword
    def area(self): pass

    @abstractmethod
    def perimeter(self): pass

    def attribute(self):  # method without abstractmethod keyword
        msg = "unknown attribute"
        return msg


class Square(Shape): # Square is another class that is inherited from Shape , so it has to implement the area and perimeter method.
    
    def __init__(self, side):
        self.side = side
        
    def area(self):  # here we define the implimentation of the abstract methods
        return self.side * self.side
    
    def perimeter(self): # here we define the implimentation of the abstract methods
        return 4 * self.side



if __name__ == "__main__":
    
    square = Square(5)
    print(square.area()) 
    print(square.perimeter())
    print(square.attribute())

    


    
 
