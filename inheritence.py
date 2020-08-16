class father:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
    
  def printname(self):
    print(self.firstname, self.lastname)



class child(father):
  def __init__(self, fname, lname):
    father.__init__(self, fname, lname)

x = child("deepak", "TM")
x.printname()