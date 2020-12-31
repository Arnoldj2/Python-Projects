
from abc import abstractmethod, ABC

"""ABC is a class from the abc module in Python. If we extend any class
with ABC and include any abstraction methods,then the classes inherited
from this class will have to mandatorily implement those abstract methods. """

class Shape(ABC):   # Here, Shape is a parent inherited from ABC class. It has an abstraction method "area"
    
    @abstractmethod  #  method is annotated with an abstractmethod keyword
    def area(self): pass

    def perimeter(self): pass


class Square(Shape):  # Square is another class that is inherited from Shape , so it has to implement the drive method.
    def __init__(self, side):
        self.side = side
        
""" if i were to add in the following

 def area(self):
        return self.side * self.side

The code would run without any problems, because the asbstract class was inherited """


square = Square(5)  # Can't instantiate abstract class Square with abstract method area
