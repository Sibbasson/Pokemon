import random
import bs
from i import names

#Things to add: 
#trainer prize money
#ev yield
#pp
#Walk around in overworld (all exits in Viridian city are blocked)
#Meet wild pokemon
#catch pokemon

#Extra:
#Gör om pokemon "base stats" till tipplar?
#priority moves
#Natures

def dmgcalc(LVL, ATK, DEF, PWR, ATK_TYPE, DEF_TYPE1, DEF_TYPE2, ACC, ATK_SLOT, Attacker = ""):
  list1 = []
  if Attacker != "":
    print("Foe " + op[0][9] + " used " + op[0][ATK_SLOT + 9][0] + "!")
  else:
    print(p[0][9] + " used " + p[0][ATK_SLOT + 9][0] + "!")
  if random.randint(1, 100) > ACC:
    if Attacker != "":
      print("Enemy " + op[0][9] + "'s attack missed!")
    else:
      print(p[0][9] + "'s attack missed!")
  else:
    list1.append((((((2 * LVL) / 5 + 2) * PWR * ATK) / DEF) / 50 + 2) * random.randint(85, 100) / 100)
    if random.randint(1, 24) == 1:
      list1[0] *= 2
      print("A critical hit!")
    tm = DEF_TYPE1[ATK_TYPE] * DEF_TYPE2[ATK_TYPE] #tm = type matchup
    list1[0] *= tm
    if tm == 0:
      if Attacker != "":
        print("It doesn't affect " + p[0][9] + "...")
      else:
        print("It doesn't affect the foe " + op[0][9] + "...")
    elif tm > 1:
      print("It's super effective!")
    elif 0 < tm < 1:
      print("It's not very effective...")
    if Attacker != "":
      if op[0][7] == types[ATK_TYPE] or op[0][8] == types[ATK_TYPE]:
        list1[0] *= 1.5
      if p[0][1] - int(list1[0]) < 0:
        p[0][1] = 0
      else:
        p[0][1] -= int(list1[0])
    else:
      if p[0][7] == types[ATK_TYPE] or p[0][8] == types[ATK_TYPE]:
        list1[0] *= 1.5
      if op[0][1] - int(list1[0]) < 0:
        op[0][1] = 0
      else:
        op[0][1] -= int(list1[0])

def dmgtext(HP, Attacker = ""):
  if HP == 0:
    if Attacker != "":
      print(p[0][9], "fainted!")
    else:
      print("Enemy", op[0][9], "fainted!")
      exp_g = bs.expy(tExp, op[0][29][10], op[0][0])
      p[0][14] += exp_g
      print("\n" + p[0][9] + " gained " + str(exp_g) + " exp!")
      print("Current exp: " + str(p[0][14]))
      print("Exp needed for next level: " + str(bs.exp(p[0][0] + 1, 2)))
      for i in range(100 - p[0][0]):
        if p[0][14] >= bs.exp(p[0][0] + 1, p[0][29][9]):
          p[0][0] += 1
          print(str(p[0][9]) + " grew to lvl " + str(p[0][0]) + "!")
          print("Old stats:")
          print(p[0][31:36])
          bs.new_pkmn(p[0], 0, 1)
          print("New stats:")
          print(p[0][31:36])
      if tExp == 1:
        return 1
  else:
    if Attacker != "":
      print(p[0][9] + " has " + str(round(p[0][1] / p[0][31] * 100, 1)) + "% HP left.")
    else:
      print("Enemy " + op[0][9] + " has " + str(round(op[0][1] / op[0][31] * 100, 1)) + "% HP left.")
  print()

def print_attacks(slot = 0):
  no_error_attack = []
  ne = 0 #ne = not empty
  while ne <= 3 and p[slot][10 + ne] != 0:
    print(ne + 1, ": ", p[slot][10 + ne][0], " ", end ="", sep="")
    if ne == 1:
      print()
    ne += 1
    no_error_attack.append(str(ne))
  return no_error_attack

def choose_attack():
  faster = 0
  if p[0][6] > op[0][6]:
    faster = "you"
  elif p[0][6] < op[0][6]:
    faster = "opp_"
  else:
    rand_faster = random.randint(1,2)
    if rand_faster == 1:
      faster = "you"
    else:
      faster = "opp"
  nea = print_attacks() #nea = no error attack
  print("\n0: Go back\n")
  chosen_attack = input("Choose attack: ")
  print()
  if chosen_attack in nea:
    if p[0][int(chosen_attack) + 9][2] == 0:
      if faster == "you":
        physical(int(chosen_attack))
        opponent_attacks()
      else:
        opponent_attacks()
        if p[0][1] > 0:
          physical(int(chosen_attack))
    else:
      if faster == "you":
        special(int(chosen_attack))
        opponent_attacks()
      else:
        opponent_attacks()
        if p[0][1] > 0:
          special(int(chosen_attack))
  elif chosen_attack != "0":
    print("Please choose a valid input") 
    print()
    choose_attack()

def opponent_attacks():
  if op[0][1] > 0:
    atk_slots = 0
    for i in range(4):
      if op[0][i + 10] != 0:
        atk_slots += 1
    opp_chosen_attack = random.randint(1, atk_slots)
    if op[0][int(opp_chosen_attack) + 9][2] == 0:
      physical(opp_chosen_attack, "opp_")
    else:
      special(opp_chosen_attack, "opp_")

#LVL, ATK, DEF, PWR, ATK_TYPE, DEF_TYPE1, DEF_TYPE2, ACC, ATK_SLOT, Attacker = ""

def physical(slot, attacker = "you"):
  if attacker != "you":
    dmgcalc(op[0][0], op[0][2], p[0][3], op[0][slot + 9][3], op[0][slot + 9][1], p[0][7], p[0][8], op[0][slot + 9][5], slot, "opp_")
    dmgtext(p[0][1], "opp_")
  else:
    dmgcalc(p[0][0], p[0][2], op[0][3], p[0][slot + 9][3], p[0][slot + 9][1], op[0][7], op[0][8], p[0][slot + 9][5], slot)
    dmgtext(op[0][1])

def special(slot, attacker = "you"):
  if attacker != "you":
    dmgcalc(op[0][0], op[0][4], p[0][5], op[0][slot + 9][3], op[0][slot + 9][1], p[0][7], p[0][8], op[0][slot + 9][5], slot, "opp_")
    dmgtext(p[0][1], "opp_")
  else:
    dmgcalc(p[0][0], p[0][4], op[0][5], p[0][slot + 9][3], p[0][slot + 9][1], op[0][7], op[0][8], p[0][slot + 9][5], slot)
    dmgtext(op[0][1])

def choose_p():
  no_error_p = []
  print("0: Go back")
  for i in range(len(p)):
    print(str(i + 1) + ": " + p[i][9])
    no_error_p.append(str(i + 1))
  p_slot = input("Choose Pokémon: ") #Need to make temp_POKEMON first
  if p_slot not in no_error_p and p_slot != "0":
    print()
    print("Please choose a valid slot")
    choose_p()
  elif p_slot != "0":
    p_step2(p_slot)

def p_step2(p_slot1):
  print()
  print("0: Go back, 1: Shift, 2: Summary")
  send_out = input("Do what with " + p[int(p_slot1) - 1][9] + "? ")
  if send_out == "0":
    choose_p()
  elif send_out == "2":
    print()
    summary(int(p_slot1) - 1)
    p_step2(p_slot1)
  elif send_out == "1":
    if p_slot1 == "1":
      print()
      print(p[0][9], "is already sent out!")
      p_step2(p_slot1)
    else: 
      p.insert(0, p[int(p_slot1) - 1])
      p.pop(int(p_slot1))
      print()
      print(p[0][9] + " was sent out!")
      opponent_attacks()
  else:
    print()
    print("Please choose a valid input")
    p_step2(p_slot1)

def summary(slot):
  print("Name: " + p[slot][9] + "\nLevel: " + str(p[slot][0]) + "\nType: " + p[slot][7][17], end="")
  if p[slot][8][17] != 1:
    print("/" + p[slot][8][17])
  print("\nMoves:")
  print_attacks(slot)
  print()

def trainer_check(tr_b = 0):
  global tExp
  if tr_b == 0:
    tExp = 1
  elif tr_b == 1:
    tExp = 1.5

types = [
  [1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,"Normal"],
  [1,1,2,1,1,.5,.5,1,1,1,1,1,1,2,1,1,.5,"Fighting"],
  [1,.5,1,1,0,2,.5,1,1,1,1,.5,2,1,2,1,1,"Flying"],
  [1,.5,1,.5,2,1,.5,1,1,1,1,.5,1,2,1,1,1,"Poison"],
  [1,1,1,.5,1,.5,1,1,1,1,2,2,0,1,2,1,1,"Ground"],
  [.5,2,.5,.5,2,1,1,1,2,.5,2,2,1,1,1,1,1,"Rock"],
  [1,.5,2,1,.5,2,1,1,1,2,1,.5,1,1,1,1,1,"Bug"],
  [0,0,1,.5,1,1,.5,2,1,1,1,1,1,1,1,1,2,"Ghost"],
  [.5,2,.5,0,2,.5,.5,1,.5,2,1,.5,1,.5,.5,.5,1,"Steel"],
  [1,1,1,1,2,2,.5,1,.5,.5,2,.5,1,1,.5,1,1,"Fire"],
  [1,1,1,1,1,1,1,1,.5,.5,.5,2,2,1,.5,1,1,"Water"],
  [1,1,2,2,.5,1,2,1,1,2,.5,.5,.5,1,2,1,1,"Grass"],
  [1,1,.5,1,2,1,1,1,.5,1,1,1,.5,1,1,1,1,"Electric"],
  [1,.5,1,1,1,1,2,2,1,1,1,1,1,.5,1,1,2,"Psychic"],
  [1,2,1,1,1,2,1,1,2,2,1,1,1,1,.5,1,1,"Ice"],
  [1,1,1,1,1,1,1,1,1,.5,.5,.5,.5,1,2,2,1,"Dragon"],
  [1,2,1,1,1,1,2,.5,1,1,1,1,1,0,1,1,.5,"Dark"],
  [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]

#move stats are ordered [0] = name, [1] = type, [2] = physical/special (0,1), [3] = power, [4] = pp, [5] = accuracy
moves = [
  ["Tackle", 0, 0, 40, 35, 100],          #[0]
  ["Flamethrower", 9, 1, 95, 15, 100],    #[1]
  ["Headbutt", 0, 0, 70, 15, 100],        #[2]
  ["Fire Blast", 9, 1, 110, 5, 85],       #[3]
  ["Shadow Ball", 7, 1, 80, 15, 100],      #[4]
  ["Thunderbolt", 12, 1, 90, 15, 100],     #[5]
  ["Razor Leaf", 11, 0, 55, 25, 95],       #[6]
  ["Sludge Bomb", 3, 1, 90, 10, 100]      #[7]
  ]

#[0] = NORMAL, [1] = FIGHT, [2] = FLYING, [3] = POISON, [4] = GROUND, [5] = ROCK, [6] = BUG, [7] = GHOST, [8] = STEEL, [9] = FIRE, [10] = WATER, [11] = GRASS, [12] = ELECTR, [13] = PSYCHC, [14] = ICE, [15] = DRAGON, [16] = DARK, [17] = Name

#B, IV, EV, LVL

#stats are ordered [0] = LVL,
# current stats: [1] = HP, [2] = ATK, [3] = DEF, [4] = SP.ATK, [5] = SP.DEF, [6] = SPD, [7] = TYPE1, [8] = TYPE2, [9] = Name, [10] = Move 1, [11] = Move 2 [12] = Move 3, [13] = Move 4, [14] = EXP
#IVs: [15] = HP, [16] = ATK, [17] = DEF, [18] = SP.ATK, [19] = SP.DEF, [20] = SPD
#EVs: [21] = HP, [22] = ATK, [23] = DEF, [24] = SP.ATK, [25] = SP.DEF, [26] = SPD
# [27] = Nature, [28] = *available*, [29] = lookup id, [30] = *available*
#Fully healed stats: [31] = HP, [32] = ATK, [33] = DEF, [34] = SP.ATK, [35] = SP.DEF, [36] = SPD

BULBASAUR = [5, 0, 0, 0, 0, 0, 0, types[bs.pd001[7]], types[bs.pd001[8]], bs.pd001[0], moves[0], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, bs.pd001, 0, 0, 0, 0, 0, 0, 0]

VENUSAUR = [50, 0, 0, 0, 0, 0, 0, types[bs.pd003[7]], types[bs.pd003[8]], bs.pd003[0], moves[6], moves[7], moves[2], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, bs.pd003, 0, 0, 0, 0, 0, 0, 0]

CHARMANDER = [5, 0, 0, 0, 0, 0, 0, types[bs.pd004[7]], types[bs.pd004[8]], bs.pd004[0], moves[0], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, bs.pd004, 0, 0, 0, 0, 0, 0, 0]

CHARIZARD = [50, 0, 0, 0, 0, 0, 0, types[bs.pd006[7]], types[bs.pd006[8]], bs.pd006[0], moves[1], moves[3], moves[2], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, bs.pd006, 0, 0, 0, 0, 0, 0, 0]

SQUIRTLE = [5, 0, 0, 0, 0, 0, 0, types[bs.pd007[7]], types[bs.pd007[8]], bs.pd007[0], moves[0], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, bs.pd007, 0, 0, 0, 0, 0, 0, 0]

RAICHU = [50, 0, 0, 0, 0, 0, 0, types[bs.pd026[7]], types[bs.pd026[8]], bs.pd026[0], moves[5], moves[2], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, bs.pd026, 0, 0, 0, 0, 0, 0, 0]

GENGAR = [50, 0, 0, 0, 0, 0, 0, types[bs.pd094[7]], types[bs.pd094[8]], bs.pd094[0], moves[4], moves[7], moves[5], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, bs.pd094, 0, 0, 0, 0, 0, 0, 0]

# bs.hpcalc(bs.pd006[1], 31, 0, CHARIZARD[0])

p = [] #p = party
op = [] #op = opponents party
temp_p = [] #temporary party

#battle loop
def battle_func(trainer_battle, trainer_name = "[You didn't define the name dumbass]"): # 1 = true 
  trainer_check(trainer_battle)
  battle = 1
  num_opp_fainted = 0
  num_fainted = 0
  c = 0
  if trainer_battle == 1:
    print()
    print(trainer_name, "would like to battle! (Opponent has", len(op), "Pokémon)")
    print(trainer_name + " sent out " + op[0][9] + "!")
    print("Go! " + p[0][9] + "!")
  else:
    print()
    print("Wild " + op[0][9] + " appeared!")
    print("Go! " + p[0][9] + "!")
    num_opp_fainted = 0
    num_fainted = 0
  while battle == 1:
    print("What will", p[0][9], "do?")
    first = input("1: Attack, 2: Run, 3: View party ")
    if first == "1": 
      print()
      choose_attack() 
    elif first == "2":
      print()
      if trainer_battle == 1:
        print("You can't run from a trainer battle!")
      else:
        c += 1
        if (p[0][36] * 128 / op[0][36] + 30 * c) % 256 > random.randint(0, 255):
          print("Got away safely!")
          return 1
    elif first == "3":
      print()
      choose_p()
    else:
      print('Please choose a vaild input')
    if op[0][1] == 0:
      num_opp_fainted += 1
      if num_opp_fainted == len(op):
        if trainer_battle == 1:
          print(names[0] + " defeated " + trainer_name + "!")
          return 1
        battle = 0
      for i in range(len(op) - 1):
        if op[i + 1][1] != 0:
          op.insert(0, op[i + 1])
          op.pop(i + 2)
          print(op[0][9] + " was sent out!")
          break
    elif p[0][1] == 0:
      num_fainted += 1
      if num_fainted == len(p):
        return 0
      for i in range(len(p) - 1):
        if p[i + 1][1] != 0:
          p.insert(0, p[i + 1])
          p.pop(i + 2)
          print(p[0][9] + " was sent out!")
          break
