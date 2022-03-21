def swap(a, b):
  if a < b:
    temp = a
    a = b
    b = temp
  else:
    temp = a
    a = b
    b = temp
  return (a,b)
    
def test_swap():
  a = int(input("Enter first age: "))
  b = int(input("Enter second age: "))
  x, y = swap(a, b)
  print(x, y)
