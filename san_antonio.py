# -*- coding: utf8 -*-

import random

quotes = [
    "Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes !", 
    "On doit pouvoir choisir entre s'écouter parler et se faire entendre."
]

characters = [
    "alvin et les Chipmunks", 
    "Babar", 
    "betty boop", 
    "calimero", 
    "casper", 
    "le chat potté", 
    "Kirikou"
]

def show_random_quote(my_list):
  rand_namb = random.randint(0, len(my_list) - 1)
  item = my_list[rand_namb]
  return(item)

user_answer = input("Tapez entrée pour connaître une autre citation ou B pour quiter le programme.")


#	if user_answer == "B":
#	  pass
#	elif user_answer == "C":
#	  print("C pas la bonne réponse ! Et G pas d'humour, je C... ")
#	else :
#	  pass
#	  # Show another quote


while user_answer != "B":
	print(show_random_quote(quotes))
	user_answer = input("Tapez entrée pour connaître une autre citation ou B pour quiter le programme.")

for character in characters:
	n_character = character.capitalize()
	print(n_character)

print(show_random_quote(quotes))