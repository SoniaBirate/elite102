class ClassA(): 
    def __init__(self): 
        self.var1 = 1
        self.var2 = 2
  
    def methodA(self): 
        self.var1 = self.var1 + self.var2 
        return self.var1 
  
class ClassB(ClassA): 
    def __init__(self, class_a): 
        self.var1 = class_a.var1 
        self.var2 = class_a.var2 
  
object1 = ClassA() 
# updates the value of var1 
summ = object1.methodA() 
  
# return the value of var1 
print (summ) 
  
# passes object of classA 
object2 = ClassB(object1) 
  
# return the values carried by var1,var2 
print( object2.var1)
print (object2.var2) 