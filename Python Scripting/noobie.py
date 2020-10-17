#!/bin/python3

name = 'Noobie'
rating = 9.5
hacks = 9600
good = True
mini:int = [7, 'mimo']

print (mini)

def redo(name, rating, hacks, true):
	best = 'affirmative'
	print(name + ' has done ' + str(hacks) 
	+ ' and has had a rating of ' + str(rating) + '.')
	print('Hacks divided by rating is ' + str(hacks/rating) + '.')
	print('Hacks modulus ratings is ' + str(hacks%rating) + '.')
	print('Hacks divided by rating without a remainder is ' 
	+ str(hacks//rating) + '.')
	if true != True :
		best = 'negative'
		print('Is he a bad hacker?? ' + best)
	else :
		print('Is he a good hacker?? ' + best)
	print ('Ratings raised to the power of two ' + str(rating**2) + '.')

redo(name, rating, hacks, good)

def newline():
	print('\n')

newline()

list_of_items = ['lilo&stitch' ,6, "sigis", True, 'ssup']
print(list_of_items)

listnum:int = [6, "sigis", True]
listing = []
listing.extend(listnum)
listing.extend(list_of_items)
#listing.pop() - remove the last item
#listing.pop(1) - remove the second item in the list
print('extend works to add a whole list for example this listing instead of doing as below \n' + str(listing) + '\n')

for num in list_of_items:
	listnum.append(num)
	print (listnum)

print (listnum)
newline()

def sqrt(x):
	return (x ** .5)

redo(name, sqrt(90.25), hacks, False)

ipaddresslist = []

ipaddresses = open('dot100.txt')
for ipaddress in ipaddresses:
	print (ipaddress)
	ipaddresslist.append(ipaddress.strip())

print ('Here is a list of ip addresses in a list' + str(ipaddresslist) + ' with ' 
+ str(ipaddresslist[2:3]) + ' as the third ip address and ' + str(ipaddresslist[len(ipaddresslist)-1:len(ipaddresslist)]) 
+ ' as the last ipaddress in the list')
	
#tuples unlike lists cannot be changes once created so no appending, popping or extending,,, immutable
family = ('Mum', 2, 'Dad', 'Siz')
#family.pop(0) will not work
print (family[1:len(family)])

#for int i=0 i<listlength i++
for n in range(0, len(listnum)):
	hacks+=1
	print (listnum[n])

newline()
#or it may be done as
i=0
while i<len(listnum):
	print (listnum[i])
	i+=1
