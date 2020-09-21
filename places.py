from i import names
import bd
import bs

def starter(a = 0):
  if a != 0:
    starter_cutscene = ["You step into the tall grass.", "Oak: Hey! Wait! Don't go out", "The professor approaches from the town.", "Oak: It's unsafe! Wild Pokémon live in tall grass!", "You need your own Pokémon for your protection. I know!", "Here, come with me!", "You follow the professor back to his lab.", "You go to the back of the lab, where the professor is waiting with " + names[1] + " and the Poké Balls.", names[1] + ": Gramps! I'm fed up with waiting!", "Oak: " + names[1] + "? Let me think...", "Oh, that's right, I told you to come! Just wait!", "Here, " + names[0] + "!", "There are 3 Pokémon here!", "Haha!", "They are inside the Poké Balls.", "When I was young, I was a serious Pokémon trainer!", "In my old age, I have only 3 left, but you can have one! Choose!", names[1] + ": Hey! Gramps! What about me?", "Oak: Be patient! " + names[1] + ", you can have one too!"]
    for i in range(len(starter_cutscene)):
      input(starter_cutscene[i])
    print("Which Pokémon will you choose?")
  p_starter = input("1: Charmander, 2: Squirtle, 3: Bulbasaur\n")
  print()
  if p_starter == "1":
    your_starter = bd.CHARMANDER
    rival_starter = bd.SQUIRTLE
  elif p_starter == "2":
    your_starter = bd.SQUIRTLE
    rival_starter = bd.BULBASAUR
  elif p_starter == "3":
    your_starter = bd.BULBASAUR
    rival_starter = bd.CHARMANDER
  else:
    print("Please choose a valid input")
    starter()
  if p_starter == "1" or p_starter == "2" or p_starter== "3":
    bs.new_pkmn(your_starter, 1, "p")
    input(names[0] + " recieved a " + bd.p[0][9] + "!")
    bs.new_pkmn(rival_starter, 1)
    input(names[1] + ": I'll take this one then!")
    input(names[1] + " recieved a " + bd.temp_p[0][9] + "!")
    input("You start walking out of Oak's lab.")
    input(names[1] + ": Wait " + names[0] + "! Let's check out our Pokémon!")
    input("Come on, I'll take you on!")
    bd.op = bd.temp_p
    win(bd.battle_func(1, names[1]), 1, 1)
    bd.p[0][1:6] = bd.p[0][31:36]
    if win == 1:
      input(names[1] + ": WHAT? Unbelievable! I picked the wrong Pokémon!")
    elif win == 0:
      input(names[1] + ": Yeah! Am I great or what!")
    input(names[1] + ": Okay, I'll make my Pokémon fight to toughen it up!")
    input(names[0] + "! Gramps! Smell you later!")

    #What happens next?

def win(w, t = 0, s = 0): #s = special
  global win
  win = w
  if s == 0 and t == 1:
    if w == 0:
      print("[Name] is out of usable pokemon...")
      print("[Name] blacked out!")



def menu(func = 0):
  if len(bd.p) > 0:
    print("Pokémon")
  print(names[0] + "\n")

rs = [
  #0
  ["You're in your room in your house in Pallet Town.", 3, "Go downstairs", "Play with SNES", "Check PC", 1, 2, 3, ],
  #1
  ["You're on the bottom floor of your house.", 3, "Go outside", "Go upstairs", "Talk to mom", 4, 0, 5],
  #2
  [names[0] + " is playing the SNES! ...Okay! It's time to go!", 0, 0],
  #3
  ["[PC placeholder]", 0, 0],
  #4
  ["You're in Pallet Town.", 4, "Go to Route 1", "Go inside Oak's lab", "Go inside your house", "Go inside " + names[1] + "'s house", 6, 7, 1, 9],
  #5
  ["Mom: Right. All boys leave home some day. It said so on TV.\nProfessor Oak, next door, is looking for you.", 0, 1],
  #6
  ["You're on Route 1.", -1, "Go to Viridian City", "Go to Pallet Town", 12, 4, starter, 7],
  #7
  ["You're in professor Oak's lab.", 2, "Go outside", "Look at Poké Balls", 4, 8, ],
  #8
  ["These are the professor's Pokémon.", 0, 7],
  #9
  ["You're in " + names[1] + "'s house.", 3, "Go outside", "Go upstairs", "Talk to Daisy", 4, 10, 11],
  #10
  ["You're in " + names[1] + "'s room.", 1, "Go downstairs", 9],
  #11
  ["Daisy: idk what she says lol", 0, 9],
  #12
  ["You're in Viridian City.", 4, "Go to Route 2", "Go to Route 1", "Go to Route 22", "Enter Pokémon Center", 13, 6, 14, 15],
  #13
  ["You're on Route 2 (dead end for now)", 1, "Go to Viridian City", 12],
  #14
  ["You're on Route 22 (dead end for now", 1, "Go to Viridian City", 12],
  #15
  ["You're in the Pokémon Center.", 3, "Talk to the nurse", "Go outside", "Check PC", 16, 12, 3],
  #16
  ["Hello, and welcome to the Pokémon Center. We restore your tired Pokémon to full health. Would you like to rest your Pokémon?", -2, "Yes/No\n", "OK, I'll take your Pokémon for a few seconds.", "...", "Thank you for waiting.", "We've restored your Pokémon to full health.", 15, "We hope to see you again!"]
]
# [0] = your_roomm, [1] = your_house, [2] = SNES, [3] = PC, [4] = pallet_town, [5] = mom, [6] = route 1, [7] = oak's lab, [8] = professor's pokemon, [9] = rival's house, [10] = rival's room, [11] = daisy, [12] = viridian city, [13] = route 2, [14] = route 22, [15] = poke center


def m(k = 0): #m = master, rs = rooms
  room = rs[k]
  overworld = 1
  while overworld == 1:
    no_error = []
    print("\n" + room[0])
    if room[1] > 0:
      print("0: Menu, ", end="")
      for i in range(room[1]):
        print(str(i + 1) + ": " + room[2 + i], end="")
        if i < room[1] - 1:
          print(", ", end="")
      inp = input("\n")
      if inp == "0":
        print()
        menu()
        no_error.append("0")
      else:
        for i in range(room[1]):
          no_error.append(str(i + 1))
          if inp == str(i + 1):
            room = rs[room[room[1] + 2 + i]]
            break
      if inp not in no_error:
        print("Please choose a valid input")
    elif room[1] == -1:
      room[len(room) - 2](1)
      room[1] = 2
      room = rs[room[len(room) - 1]]
    elif room[1] == -2:
      yn = input(room[2])
      if yn == "Yes" or yn == "yes":
        for i in range (6):
          if i < len(bd.p):
            bd.p[i][1:6] = bd.p[i][31:36]
          if i < 4:
            input(room[i + 3])
      input(room[len(room) - 1])
      room = rs[room[len(room) - 2]]
    elif room[1] == 0:
      room = rs[room[2]]
