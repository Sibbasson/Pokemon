import i

start = input("1: From beginning, 2: Skip to your room, 3: Battle test\n")
if start == "1":
  i.introseq()
  import places #bryter mot PEP 8 jättehårt men det funkar
  places.m()

elif start == "2":
  import places
  places.m()

elif start == "3":
  import bd #bryter också mot PEP 8 men wth
  import bs
  bs.new_pkmn(bd.CHARIZARD, 1, "p")
  bs.new_pkmn(bd.GENGAR, 1, "p")
  bs.new_pkmn(bd.VENUSAUR, 1)
  bs.new_pkmn(bd.RAICHU, 1)
  bd.op = bd.temp_p
  bd.battle_func(1, "Blue")
else:
  print("Please restart and choose a valid input")







print("Hackerman")
