from math import sqrt

class Prime:
  def __init__(self):
    self.priSeq = [0, 1]

  def __call__(self,n):
    if (n <= 1):
        return False
    for i in range(2, int(sqrt(n))+1):
      if (n % i == 0):
        return False
      return True

def test_prime():
  pri_of = Prime() 
  print("Is 13 prime?", pri_of(13))
  print("Is 8 prime?", pri_of(8))