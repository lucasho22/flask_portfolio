{% include navigation.html %}

# Data Structures

## Week 0

### Menu Challenge Code
![image](https://user-images.githubusercontent.com/77864093/158083190-d192270d-fe05-4420-88c2-058bc518e944.png)

### Swap Code
![image](https://user-images.githubusercontent.com/77864093/158109129-05dccdf8-d80c-4d1a-a2b4-06b83953150b.png)

### Keypad Code
![image](https://user-images.githubusercontent.com/77864093/158101274-571247ee-4399-49e5-b320-7f8fedd72f9c.png)

### Tree Code
![image](https://user-images.githubusercontent.com/77864093/158115651-155910f6-d924-4c5a-b68f-928926ae8332.png)

#### Github Links
[GitHub Commits](https://github.com/lucasho22/flask_portfolio/issues/2)

#### Replit Links
[Replit](https://replit.com/@lucasho22/flaskportfolio-2#swap.py)


## Week 1

### Lists with loops
<iframe frameborder="0" width="100%" height="500px" src="https://replit.com/@lucasho22/flaskportfolio-2?embed=true"> </iframe>

### Fibonacci with try/except
![image](https://user-images.githubusercontent.com/77864093/159205789-076389f5-8635-4c3a-9328-315d53b41750.png)
```python
def fibonacci(n):
  if n == 0:
    return 0
    # return 0 for n == 0
  elif n == 1 or n == 2:
    return 1
    # return 1 for n == 1 or n == 2
  else:
    return fibonacci(n-1) + fibonacci(n-2)
    # Goes through fibonacci. Loop. Adds. This is the original code for fibonacci.

def fibonacci_results():
  try:
    num = int(input("Enter a number for fibonacci: "))
    if num < 0:
      raise ValueError
      # If the number is negative, the code won't work, so we need to show the user there is an error.
      
    for n in range(num + 1):
      if n == num:
        print(fibonacci(n))
        # Prints fibonacci sequence for whatever n is
      else:
        print(fibonacci(n), end=", ")
  except ValueError:
    print("ERROR: Invalid input for Fibonacci sequence.")
```

#### Github Links
[GitHub Commits and Links](https://github.com/lucasho22/flask_portfolio/issues/5)

#### Replit Links
[Replit](https://replit.com/@lucasho22/flaskportfolio-2#main.py)
