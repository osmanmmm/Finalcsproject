from graphics import *
import math 
from random import randint
from time import sleep


class Planet:
   def __init__(self, x, y, color, radius):
       self.x = x
       self.y = y
       self.color = color
       self.radius = radius
       self.Circle = Circle(Point(self.x, self.y), self.radius)
       self.Circle.setFill(self.color)


   def draw(self, window):
       self.Circle.draw(window)


class Orbit:
   def __init__(self, x, y, oradius):
       self.x = x
       self.y = y
       self.oradius = oradius
       self.Circle = Circle(Point(self.x, self.y), self.oradius)
       self.Circle.setOutline("white")


   def draw(self, window):
       self.Circle.draw(window)


window = GraphWin("Solar system", 1000, 1000)
window.setBackground("black")


sun = Planet(500, 500, color_rgb(253, 184, 19), 50)
sun.draw(window)


mercury = Planet(500 + 100, 500, color_rgb(219, 206, 202), 20)
mercury.draw(window)


venus = Planet(500 + 250, 500, color_rgb(255, 198, 73), 30)
venus.draw(window)


earth = Planet(500 - 350, 500, color_rgb(52, 165, 111), 50)
earth.draw(window)


mercury_orbit = Orbit(500, 500, 100)
mercury_orbit.draw(window)
venus_orbit = Orbit(500, 500, 250)
venus_orbit.draw(window)
earth_orbit = Orbit(500, 500, 350)
earth_orbit.draw(window)

for i in range(300):
   x = randint(0, 1000)
   y = randint(0, 1000)
   message = Text(Point(x, y), "*")
   message.setSize(10)
   message.setTextColor("white")
   message.draw(window)
   sleep(0.1)
   message.move(randint(-200, 200), randint(-200, 200))




window.getMouse()
window.close()
