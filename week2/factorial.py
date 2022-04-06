class Factorial:
  def __call__(self,n): #calls self, for an integer n
    if n == 1 or n == 0:
      return 1
      # Factorial of 0 and 1 is 1
    else:
      return n * self(n-1) 
      # Goes through factorial code for any n values greater than 1.

def testee():
  facto_of = Factorial() #facto_of is the class "Factorial"
  print("The factorial of four is", facto_of(4))
  print("The factorial of six is", facto_of(6))