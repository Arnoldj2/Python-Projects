
class protected: #created a class to demonstrate protected variables
    def __init__(self): 
        self._protectedVar  = 10 #Protected is prefixed with a single underscore. it acts as a warning but doesnt change behavior 

obj = protected()
print(obj._protectedVar)  #called variable
obj._protectedVar = 20     # updated variable
print(obj._protectedVar)    # called variable again and it returned the updated values

class Private:  #created a class to demonstrate private variables
  def __init__(self): 
    self.name = 'Jeffrey' 
    self.__lastname = 'Arnold'  #private variable, denoted by 2 underscores
    
  def PrintName(self):
    return self.name +' ' + self.__lastname
    
    
P = Private()
print(P.name)
print(P.PrintName())
print(P.__lastname)  # variable is hidden when accessed outside of the class
#AttributeError: 'Person' object has no attribute '__lastname'








