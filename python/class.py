# class vehicle:
#     wheel=4
#     door=4
#     def start(self,a,b):
#         # print("engine start")
#         print(a*b)         
# car=vehicle()
# car.start(4,4)



        
# class vehicle:
#     wheel=4
#     door=4
#     def start(self,type):
#         print(type,"engine start")           
# car=vehicle()
# car.start("engine stop")
        
        
        
# class vehicle:
#     color="red"
#     def start(self):
#         print("color is",self.color)
# car=vehicle()
# car.start()



# class vehicle:
#     def setColor(self,color):
#         self.color=color
#     def show(self):
#         print("color is",self.color)
# car=vehicle()
# car.setColor("violet")
# car.show()

"""constructor"""

# class vehicle:
#     def __init__(self,color,tyre):
#         self.color=color
#         self.tyre=tyre
#     def show(self):
#         print("color is",self.color,"tyre is",self.tyre)
# car=vehicle("green",4)
# car.show()
       
       
class animal:
    def __init__(self,leg,tail,eye):
        self.leg=leg
        self.tail=tail
        self.eye=eye
    def show(self):
        print("leg is",self.leg)
    def show(self):    
        print( "tail is",self.tail)
    def show(self):
        print(      "eye is", self.eye) 
wildanimal=animal(4,1,2)
wildanimal.show()
petanimal=animal(4,1,2)
petanimal.show()




# class animal:
#     def __init__(self,leg,tail,eye):
#         self.leg=leg
#         self.tail=tail
#         self.eye=eye
#     def show(self):
#         print("leg is",self.leg,"tail is",self.tail,"eye is", self.eye) 
# wildanimal=animal(4,1,2)
# petanimal=animal(4,1,2)
# wildanimal.show()
# petanimal.show()