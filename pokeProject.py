from pokemon.master import *
import time

poke_data = catch_em_all()

i = 1
my_poke = {}
for key,value in poke_data.items():
    my_poke[value["name"].lower()] = value["ascii"]
    i += 1
    if(i > 386):
        break

print(my_poke["pikachu"])