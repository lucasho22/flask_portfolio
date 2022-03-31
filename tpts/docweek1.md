{% include navigation.html %}

<iframe frameborder="0" width="100%" height="500px" src="https://replit.com/@lucasho22/flaskportfolio-2?embed=true"> </iframe>

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
