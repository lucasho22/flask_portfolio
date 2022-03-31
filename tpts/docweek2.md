{% include navigation.html %}

<iframe frameborder="0" width="100%" height="500px" src="https://replit.com/@lucasho22/flaskportfolio-2?embed=true"> </iframe>

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
