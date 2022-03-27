class Factorial:
  def __init__(self):
    self.facSeq = [0, 1]
  
  def __call__(self,n):
    if n == 1 or n == 0:
      return 1
    else:
      return n * self(n-1) 

def testee():
  facto_of = Factorial() 
  print("The factorial of four is", facto_of(4))
  print("The factorial of six is", facto_of(6))