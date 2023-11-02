"""single inheritance"""

# class vehicle:
#     color="green"
#     def engine(self):
#         print("all vehicles have engine")
# class car(vehicle):
#     def fourwheel(self):
#         print("car have 4 wheel",self.color)
# c=car()
# c.fourwheel()
# c.engine()


"""multi levevl"""

# class granpa:
#     def farmer(self):
#         print("farmer")
#     def kashandi(self):
#         print("kashandi")
# class father:
#     def driver(self):
#         print("driver")
#     def reader(self):
#         print("reader")
# class me:
#     def engineer(self):
#         print("engineer")
#     def swimming(self):
#         print("swimming")
# class mechild:
#     def gamer(self):
#         print("gamer")
# ab=me()
# ab.engineer()
# ab.swimming()

"""multiple inheritance"""

class father:
    def driver(self):
        print("driver")
   
class mother:
    def cook(self):
        print("cook")
   
class girl(father,mother):
    def gamer(self):
        print("gamer")
ab=girl()
ab.cook()
ab.driver()
ab.gamer()


