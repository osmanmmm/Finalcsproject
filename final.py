from graphics import * 
import math 

class Planet: 
    def __init__(self, x, y, color, radius):
        self.x = x
        self.y = y
        self.color = color 
        self.radius = radius
        self.circle = Circle(Point(self.x, self.y), self.radius)
        self.circle.setFill(self.color)
    
    def draw(self, window): 
        self.circle.draw(window)
    
class Orbit: 
    def __init__(self, x, y, xradius, yradius):
        self.x = x
        self.y = y
        self.xradius = xradius
        self.yradius = yradius
        self.oval = Oval(Point(self.x - self.xradius, self.y - self.yradius), 
                         Point(self.x + self.xradius, self.y + self.yradius))
        self.oval.setOutline("white")
    
    def draw(self, window): 
        self.oval.draw(window)

window = GraphWin("Solar system", 1000, 1000)
window.setBackground("Black")

sun = Planet(500, 500, color_rgb(253, 184, 19), 50)
sun.draw(window)

mercury = Planet(400, 500, color_rgb(151, 151, 159), 20)
mercury.draw(window)

venus = Planet(300, 500, color_rgb(139, 125, 130), 30)
venus.draw(window)

earth = Planet(200, 500, color_rgb(13, 152, 186), 50)
earth.draw(window)

mercury_orbit = Orbit(500, 500, 100, 80)
mercury_orbit.draw(window)

venus_orbit = Orbit(450, 500, 250, 200)
venus_orbit.draw(window)

earth_orbit = Orbit(225, 500, 200, 150)
earth_orbit.draw(window)

window.getMouse()
window.close()