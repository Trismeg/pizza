# -*- coding: utf-8 -*-
class PizzaPlace(object):
               hourOpens = ""
               hourCloses = ""
               foodMenu = ""
               parking = None

               def __init__(self,hourOpens, hourCloses, foodMenu, parking):
                               self.hourOpens = hourOpens
                               self.hourCloses = hourCloses
                               self.foodMenu = foodMenu
                               self.parking = parking

               def hoursOfOperation(self):
                               result = "We are open from "+self.hourOpens+" to "+self.hourCloses
                               return result

               def foodMenuN(self):
                               result = "We proudly serve "+self.foodMenu
                               return result


               def  haveParking(self):
                               if self.parking == False:
                                   return"Yes, we have sample parking!"
                               else:
                                   return "Sorry, no parking is available."  

myPizzaPlace = PizzaPlace("10am","10pm","Pizza Wings Burgers", True)

print myPizzaPlace.hoursOfOperation()
print myPizzaPlace.foodMenuN()
print myPizzaPlace.haveParking()
