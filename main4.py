#from sys import executable

#import sys

#print(sys.executable)  # розташування інтерпретатора Python
#print(sys.version)     # його версія
#print(sys.platform)    # дані щодо операційної системи
# дізнатися назви всіх імпортованих модулів та їх шляхи
#for name, path in sys.modules.items():
 #   print(name, path)




#import tkinter
#import sys


#print(type(tkinter))
#print(type(sys))

#print(tkinter.__file__)
#print(sys.executable)
#print(sys.version)
#print(sys.platform)

#for name, path in sys.modules.items():
 #   print(name, path)




#class Car:
 #   def __init__(self, brand, year, color):
  #      self.brand = brand
   #     self.year = year
    #    self.color = color

 #   def drive(self):
  #      print(f"{self.brand} їде вперед!")
#print(dir(Car))



# Створення винятків
class BuildingError(Exception):
    def __str__(self):
        return f"With so much material the house cannot be built!"

def check_material(amount, limit):
    if amount > limit:
        return "enough material"
    else:
        # Увага: BuildingError приймає 'amount' як аргумент,
        # але __str__ його не використовує
        raise BuildingError(amount)

material = 123
check_material(material, limit=100)