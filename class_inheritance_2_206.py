class A: # parent class 
    attr1 = "item 1"
    attr2 = "item 2"
    
    def Test1(self):  
        print("test1() method from class A")


class B(A): # 1st Child Class ( inherits from class A )
    attr3 = "item 3"

    def Test1(self):  # child inherits the method from the parent ( has the same "name" as the method in the parent class ) 
        print("test1() method from class B") # we are modifying the method in this instance because it doesnt fit with the parent in this pretend mock up

class C(A): # 2nd Child Class ( inherits from class A )
    attr4 = "item 4"

    def Test1(self):   # child inherits the method from the parent ( has the same "name" as the method in the parent class )
        print("test1() method from class C")  # we are modifying the method in this instance because it doesnt fit with the parent in this pretend mock up


if __name__ == "__main__":
    A = A()
    B = B()
    C = C()
    A.Test1()
    B.Test1()
    C.Test1()
