#!/bin/python3

import sys as sy #importing library with alias
import datetime #importing whole library
from datetime import datetime as datewithtime #importing specific from library then giving an alias


print(sy.version)
def newline():
	print("\n")
print('Better way to show version: ' + sy.version[0:int(sy.version.find(')'))+1])
print(datewithtime.now())
print(datetime.datetime.now())

def argument (num, string, boolean):
	#this is gonna crush too
	print(bool('900'))
	print(int(num)*4)
	nibbi = string + '! what is going on niccur'
	print(nibbi.split())
	print(' '.join(nibbi.split()))
	print('"Chibi", they all said.')
	print("\'Chibi\', they all said.")#use of an escape
	print('\'Chibi\', they all said.')#use of an escape
	print("\"Chibi\", they all said.")#use of an escape
	#find letter in the string which returns a boolean
	print("in there C in chibbi?? " + str("C" in nibbi))
	#concatenation using wild cards
	print('Who does that {}{}'.format('??', 'niccur really??'))
	print('                           ' + nibbi + '    too much space 😖           ')
	print(('                           (' + nibbi + '    too much space 😖)           ').strip() 
	+ ' now stripped out... Big space is little now')
	#probably this too
	#coding huh 😫🙄
	if (boolean == 'True'):
		print('Yaay!!😃😃😃😃😃😃😃')
	elif (boolean == 'False'):
		print('Howdy biiii...😫')
	else:
		print('Are you even there??😂😂...😫')

#this is gonna crash alot,,, out of range stuff
argument(sy.argv[1], sy.argv[2], sy.argv[3])

#dictionaries work like hashmaps in java with a key value pair {key: value}
distance = {400: 'Short', 600: 'Average', 800: 'Quite long', 1000: 'Really long'} #distance is the key & description is the value

#a key may have several values
shows = {'Anime': ["Naruto", "Bleach", "Fate:Zero"], 
'Netflix': ["Punisher", "Stranger Things", "Witcher", "Disenchantment"], 
'Animations':["Rick and Morty", "Archer", "All Hail King Julien"]}
print(shows)


#adding a new key-value pair
shows["CW"] = ['Arrow', 'The Flash', 'iZombie', 'Originals']
print(shows)
newline()
#changing the value of a key
shows["CW"] = ['Arrow', 'The Flash', 'iZombie', 'Originals', 'Vampire Diaries']
distance[800] = 'Very long'
distance[1000] = 'Too long'
print(shows)
print(distance)

newline()
#updating fields which is basically as what is above
#~Be careful since adding a string in the place of an array or list in this case will make the section to hold a singular value~ 
shows.update({"CW": ["Legacies"], "Netflix": ["Defenders"]})
print(shows)

newline()

netflix_shows = ["Punisher", "Stranger Things", "Witcher", "Disenchantment"]
cw_shows = ['Arrow', 'The Flash', 'iZombie', 'Originals', 'Vampire Diaries']
for g in netflix_shows:
	shows['Netflix'].append(g)

for g in cw_shows:
	shows["CW"].append(g)
print('The final list of shows is: \n' + str(shows))




