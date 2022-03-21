def fibonacci(n):
  if n == 0:
    return 0
  elif n == 1 or n == 2:
    return 1
  else:
    return fibonacci(n-1) + fibonacci(n-2)

def fibonacci_results():
  try:
    num = int(input("Enter a number for fibonacci: "))
    if num < 0:
      raise ValueError
      
    for n in range(num + 1):
      if n == num:
        print(fibonacci(n))
      else:
        print(fibonacci(n), end=", ")
  except ValueError:
    print("ERROR: Invalid input for Fibonacci sequence.")