class Main:
      def func1(self):
          print("This is main parent class")
class derieved(Main):
      def func2(self):
          print("This is dereived function of parent class")
class Child(Main):
      def func3(self):
          print("this is 2nd derieved from parent class")
 
ob = derieved()
ob1 = Child()
ob.func1()
ob.func2()
ob1.func3()