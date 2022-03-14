def build_tree(height):
  i = 1
  while i <= height:
    print(" " * (height - i) + "* " * i)
    i = i + 1
  print(" " * (height - 2) + "***")
  print(" " * (height - 2) + "***")

def treefunc():
  height = int(input("Enter height: "))
  build_tree(height)