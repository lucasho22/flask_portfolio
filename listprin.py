InfoDb = []
InfoDb.append({  
  "FirstName": "Lucas",  
  "LastName": "Ho",    
  "Favorite_Movies":["Star Wars","Dumb and Dumber","Spider Man","Avengers"]  
})  

InfoDb.append({  
  "FirstName": "Joe",  
  "LastName": "Rob",    
  "Favorite_Movies":["Cars","Super Idol","Wonder Pets"]  
})

InfoDb.append({  
  "FirstName": "Bob",  
  "LastName": "Bob",    
  "Favorite_Movies":["Bob bb","moooo","movE"]  
})

def print_data(n):
    print(InfoDb[n]["FirstName"], InfoDb[n]["LastName"])
    print("\t", "Favorite Movies: ", end="")
    print(", ".join(InfoDb[n]["Favorite_Movies"])) 
    print() 

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