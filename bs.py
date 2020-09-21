import random
import math

#pdXXX (PokéDex#): [0] = Name, [1] = HP, [2] = ATK, [3] = DEF, [4] = SP.ATK, [5] = SP.DEF, [6] = SPD
# [7] = type 1, [8] = type 2, [9] = EXP group, [10] = EXP yield

#EV yield: [11] = HP, [12] = ATK, [13] = DEF, [14] = SP.ATK, [15] = SP.DEF, [16] = SPD

#[0] = NORMAL, [1] = FIGHT, [2] = FLYING, [3] = POISON, [4] = GROUND, [5] = ROCK, [6] = BUG, [7] = GHOST, [8] = STEEL, [9] = FIRE, [10] = WATER, [11] = GRASS, [12] = ELECTR, [13] = PSYCHC, [14] = ICE, [15] = DRAGON, [16] = DARK, [17] = Neutral
#make into tuples?
pd001 = ["Bulbasaur", 45, 49, 49, 65, 65, 45, 11, 3, 2, 64, 0, 0, 0, 1, 0, 0]
pd003 = ["Venusaur", 80, 82, 83, 100, 100, 80, 11, 3, 2, 236, 0, 0, 0, 2, 1, 0]

pd004 = ["Charmander", 39, 52, 43, 60, 50, 65, 9, 17, 2, 62, 0, 0, 0, 0, 0, 1]
pd006 = ["Charizard", 78, 84, 78, 109, 85, 100, 9, 2, 2, 240, 0, 0, 0, 3, 0, 0]

pd007 = ["Squirtle", 44, 48, 65, 50, 64, 43, 10, 17, 2, 63, 0, 0, 1, 0, 0, 0]

pd026 = ["Raichu", 60, 90, 55, 90, 80, 110, 12, 17, 1, 218, 0, 0, 0, 0, 0, 3]

pd094 = ["Gengar", 60, 65, 60, 130, 75, 110, 7, 3, 2, 190, 0, 0, 0, 3, 0, 0]

import bd

#B, IV, EV, LVL(, N)

def statcalc(B, IV, EV, LVL, N = 1):
  return math.floor((math.floor((2 * B + IV + math.floor(EV/4)) * LVL / 100) + 5) * N)


def hpcalc(B, IV, EV, LVL):
  return math.floor((2 * B + IV + math.floor(EV/4)) * LVL / 100) + LVL + 10 

#tr = trainer (1, 1.5), B = base exp yield, fLVL = LVL of fainted pkmn
def expy(tr, B, fLVL):
  return math.ceil((tr * B * fLVL) / 7)

def new_pkmn(name, IVs = 0, who = 0):
  if IVs != 0:
    name[14] = exp(name[0], name[29][9])
  for i in range(6):
    if IVs != 0:
      name[15 + i] = random.randint(0,31)
    if i > 0:
      name[31 + i] = statcalc(name[29][1 + i], name[15 + i], name[21 + i], name[0]) #"permanent" stats
      name[1 + i] = name[31 + i] # stats that change during battle
  name [31] = name[1] = hpcalc(name[29][1], name[15], name[21], name[0]) # hpcalc
  if who == "p":
    bd.p.append(name)
  elif who == 0:
    bd.temp_p.append(name)
  
def exp(n, group, check = 0): #lvl, exp group
  pkmn_exp = 0
  if group == 0:
    pkmn_exp = math.ceil((n ** 3) * 0.8) #fast
  elif group == 1:
    pkmn_exp = n ** 3 #medium fast
  elif group == 2:
    pkmn_exp = math.ceil((n ** 3) * 1.2 - 15 * (n ** 2) + 100 * n - 140) #medium slow
  elif group == 3:
    pkmn_exp = math.ceil((n ** 3) * 1.2) #slow
  else:
    print("EXP group error")
  if pkmn_exp != 0:
    return pkmn_exp
