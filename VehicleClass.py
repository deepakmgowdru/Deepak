class Vehicle:   
  
  def __init__(self, price):
    self.price = price
  def display(self):
    print ('Price = Rs',self.price)

class Category(Vehicle):   
   
   def __init__(self, price, name):
     Vehicle.__init__(self, price)
     self.name = name

   def disp_name(self):
     print ('Vehicle = ',self.name)

obj = Category(120000, 'Maruthi Ciaz')
obj.disp_name()
obj.display()