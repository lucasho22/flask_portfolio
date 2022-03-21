def build_tree(height):
  i = height
  p = 1
  while i >= 1:
    print(" " * (p) + "ඞ " * i)
    i = i - 1
    p = p + 1

def treefunc():
  height = int(input("Enter height: "))
  build_tree(height)
