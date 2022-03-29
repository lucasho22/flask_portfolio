def buildTree2(height):
  i = 1
  while(i<=height):
    amongInRow = "ඞ " * i
    n = 3 * height - i
    sp = " " * n
    print(sp + amongInRow + "\n")
    i = i + 1
  print(" " * 3 * (height-1) + "* * *\n" + " " * 3 * (height-1) + "* * *")
    
def tester2():
  height = int(input("Enter how tall you want the tree to be: "))
  buildTree2(height)