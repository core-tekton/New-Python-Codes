class MyClass:
    x = 0
    name = ""
    print(type(name))

    def __init__(self,z):
        self.name = z
        print(self.name,'I am Constructed')

    def party(self):
        self.x = self.x + 1
        print(self.name,"So Far", self.x)

    ##def __del__(self):
        ##print('I am Destructed',self.x)

class YourClass(MyClass):
    points = 0
    def touchdown(self):
        self.points = self.points+7

        print(self.name,"points",self.points)



var1 = MyClass("Jeevan")
var1.party()

var2 = YourClass("Jyoti")
var2.party()
var2.touchdown()

#var1.party()



##var=42
##print('var contains',var)

