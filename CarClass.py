class Car:   
    wheels = 4

    def __init__(self, colour, style):
        self.colour = colour
        self.style = style

  
    def showDescription(self):
        print("This car is a", self.colour, self.style)

    
    def changeColour(self, colour):
        self.colour = colour

c = Car('Black', 'Sedan')


c.showDescription()

c.changeColour('White')

c.showDescription()