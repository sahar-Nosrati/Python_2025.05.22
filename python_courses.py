import sys
import numpy as np

# class Red_fruit:
#   def __init__(self, name, location):
#     self.name = name
#     self.location = location

#   def color (self):
#     return ("Red")

# class Green_fruit:
#   def __init__(self, name, location):
#     self.name = name
#     self.location = location

#   def color (self):
#     return ("Green")
  

# class Yellow_fruit:
#   def __init__(self, name, location):
#     self.name = name
#     self.location = location

#   def color (self):
#     return ("Yello")
  

# pomegranate = Red_fruit("pomegranate", "Iran")
# kiwi = Green_fruit("Kiwi", "Poland")
# pineapple = Yellow_fruit("Pineapple", "Spain")


# for fruit in (pomegranate, kiwi, pineapple):
#   print(fruit.color())


class Fruit:
  def __init__(self, name, location):
    self.name = name
    self.location = location

  def color (self):
    return ("Red")

class Green_fruit(Fruit):
  def color (self):
    return ("Green")
  
class Yellow_fruit(Fruit):
  def color (self):
    return ("Yello")
  

pomegranate = Fruit("pomegranate", "Iran")
kiwi = Green_fruit("Kiwi", "Poland")
pineapple = Yellow_fruit("Pineapple", "Spain")

for fruit in (pomegranate, kiwi, pineapple):
  print(fruit.color())