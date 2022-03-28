{% include navigation.html %}

# Data Structures

<iframe frameborder="0" width="100%" height="500px" src="https://replit.com/@lucasho22/flaskportfolio-2?embed=true"> </iframe>

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
```python
InfoDb = []
InfoDb.append({  
  "FirstName": "Lucas",  
  "LastName": "Ho",    
  "Favorite_Movies":["Star Wars","Dumb and Dumber","Spider Man","Avengers"]  
})  
# adds to the end of InfoDb

InfoDb.append({  
  "FirstName": "Joe",  
  "LastName": "Rob",    
  "Favorite_Movies":["Cars","Super Idol","Wonder Pets"] 
})
# adds to the end of InfoDb

InfoDb.append({  
  "FirstName": "Bob",  
  "LastName": "Bob",    
  "Favorite_Movies":["Bob bb","moooo","movE"]  
})
# adds to the end of InfoDb

InfoDb.append({  
  "FirstName": "Steve",  
  "LastName": "Jobs",    
  "Favorite_Movies":["Wreck It Ralph","Bugs Life","Up"] 
})
# adds to the end of InfoDb

def print_data(n):
    print(InfoDb[n]["FirstName"], InfoDb[n]["LastName"])
    print("\t", "Favorite Movies: ", end="")
    print(", ".join(InfoDb[n]["Favorite_Movies"])) 
    print() 
# prints the list. This is how it will appear for each loop. Shows first name, last name, and favorite movies.

def for_loop():
  for n in range(len(InfoDb)):
    print_data(n)

def while_loop(n):
    while n < len(InfoDb):
        print_data(n)
        n += 1
    return

def recursive_loop(n):
  if n < len(InfoDb):
      print_data(n)
      recursive_loop(n + 1)
  return

def tester():
  print("For loop")
  for_loop()
  print("While loop")
  while_loop(0)  
  print("Recursive loop")
  recursive_loop(0)  
# Code for replit that actually prints list 
```

### Fibonacci with try/except
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

## Week 2

### Factorial
```python
class Factorial:
  def __call__(self,n):
    if n == 1 or n == 0:
      return 1
      # Factorial of 0 and 1 is 1
    else:
      return n * self(n-1) 
      # Goes through factorial code for any n values greater than 1.

def testee():
  facto_of = Factorial() 
  print("The factorial of four is", facto_of(4))
  print("The factorial of six is", facto_of(6))
  ```
### Math Function: Prime Numbers
```python
from math import sqrt

class Prime:
  def isPrime(self, n):
    if (n <= 1):
      return "No"
      #0 and 1 are not prime bumers
      
    for i in range(2, int(sqrt(n))+1):
      if (n % i == 0):
        return "No"
        # Finds in the range, sees if there is any divisible number
    return "Yes"
    # Returns yes if it can't find a divisibile  number

def test_prime():
  prime = Prime()
  print("Is 13 prime?", prime.isPrime(13))
  print("Is 8 prime?", prime.isPrime(8))
  print("Is 65 prime?", prime.isPrime(65))
  # Puts in these numbers to run the function
  ```
  
#### Github Links
[Github Commits and Links](https://github.com/lucasho22/flask_portfolio/issues/7)

#### Replit Links
[Replit](https://replit.com/@lucasho22/flaskportfolio-2#week2/factorial.py)
