class A: # parent class 1
    attr1 = "item 1"
    attr2 = "item 2"
    
    def classAinfo(self):  
        msg = "\nAttribute 1: {}\nAttribute 2: {}".format(self.attr1,self.attr2)
        return msg

class B: # Parent class 2
    attr3 = "item 3"
    attr4 = "item 4"
    
    def classBinfo(self):  
        msg = "\nAttribute 3: {}\nAttribute 4: {}".format(self.attr3,self.attr4)
        return msg

class C:  # Parent class 3
    attr5 = "item 5"
    attr6 = "item 6"
    
    def classCinfo(self):  
        msg = "\nAttribute 5: {}\nAttribute 6: {}".format(self.attr5,self.attr6)
        return msg

class D(A, B, C): # Child Class ( derived from parent 1 2 and 3 )
    attr7 = "item 7"

    def classDinfo(self):  
        msg = "\nAttribute 7: {}".format(self.attr7)
        return msg

class E(A, B, C): # 2nd Child Class ( derived from parent 1 2 and 3 )
    attr8 = "item 8"

    def classEinfo(self):  
        msg = "\nAttribute 8: {}".format(self.attr8)
        return msg


if __name__ == "__main__":
    Combine = D()
    print(Combine.classAinfo()) # Calls Class A Method from class D
    print(Combine.classBinfo()) # Calls Class B Method from class D
    print(Combine.classCinfo()) # Calls Class C Method from class D
    Combine1 = E()
    print(Combine1.classEinfo()) # Calls Class A Method from class E
  
