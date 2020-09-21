names = ['Red', 'Blue']

def choose_name(a = 0, b = 0):
  while a == 0:
    if b == 0:
      pick_name = input("1: New name, 2: Red, 3: Ash, 4: John\n")
      if pick_name == "1":
        a = 1
        return (input("Please enter your name: "))
      elif pick_name == "2":
        a = 1
        return ("Red")
      elif pick_name == "3":
        a = 1
        return ("Ash")
      elif pick_name == "4":
        a = 1
        return ("John")
      else:
        print("Please choose a vaild input")
    elif b == 1:
      pick_name = input("1: New name, 2: Blue, 3: Gary, 4: Jack\n")
      if pick_name == "1":
        a = 1
        return (input("Please enter his name: "))
      elif pick_name == "2":
        a = 1
        return ("Blue")
      elif pick_name == "3":
        a = 1
        return ("Gary")
      elif pick_name == "4":
        a = 1
        return ("Jack")
      else:
        print("Please choose a vaild input")

def choose_rival():
    choose_rival()

def introseq():
  global names
  names = []
  input("Hello there! Welcome to the world of Pokémon!")
  input("My name is Oak! People call me the Pokémon professor!")
  input("This world is inhabited by creatures called Pokémon!")
  input("For some people, Pokémon are pets. Others use them for fights.")
  input("Myself...")
  input("I study Pokémon as a profession.")
  input("First, what is your name?") 
  names.append(choose_name(0, 0))
  input("Right! So your name is " + names[0] + "!")
  input("This is my grandson. He's been your rival since you were a baby.")
  input("...Erm, what is his name again?")
  names.append(choose_name(0, 1))
  input("That's right! I remember now! His name is " + names[1] + "!")
  input(names[0] + "!")
  input("Your very own Pokémon legend is about to unfold!")
  input("A world of dreams and adventures with Pokémon awaits! Let's go!")
  print()
  

