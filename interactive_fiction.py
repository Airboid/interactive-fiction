from collections import defaultdict
import os

def choice_check (inp): # Checks whether the player input is valid
	global a, b # Uses global choice variables for reference
	inp = str(inp)
	a = str(a)
	b = str(b)
	if inp.lower() == a.lower() or inp.lower() == b.lower():
		return inp.lower()
	else:
	 	return choice_check(input('Invalid or incorrect input. Try again: '))
	
def game_reset (inp): # Resets or ends the game depending on the input. Clears the prompt screen if the former.
	if inp == 'x' or inp == 'X':
		return inp
	else:
		 os.system('cls' if os.name == 'nt' else 'clear')
		 return inp
	
line = 1
a = ''
b = ''
while line != 'x' and line != 'X': #Loops the game if chosen to reset
	playerinfo = defaultdict(list) #Storages player info that will be used in the 				playthrough
	name = input('Welcome to this project. What is your name? ')
	playerinfo['name'].append(name)
	age = input('Hello %s, how old are you? ' %(name))
	try:
		int(age)
		if int(age) in (range(8, 130)):
			playerinfo['age'].append(age)
		else:
			print("You weren't truthful on your age. This will have consequences...")
			playerinfo['age'].append('null')
	except:
		print("You weren't truthful on your age. This will have consequences...")
		playerinfo['age'].append('null')
	a = 'left'
	b = 'right'
	taken = False
	choice = choice_check(input('You are in a dark room of a castle. Opening the door out leads to a hallway. Are you going left or right? (Left/Right) '))
	if choice == a:
		a = 'yes'
		b = 'no'
		choice = choice_check(input('You find a room with a casket at the center. Opening the casket, you find a strange red ore that says "I open to the truthful". Will you take it? (Yes/No) '))
		if choice == a:
			taken = True
		else:
			pass
	print ('You then return and decide to go back and choose the right.')		
	print ('You find the king of the castle. He offers you food and requests a red ore.')
	if taken == False:
		print ("You don't seem to have any, so the king loses his interest on you. Game over.")
		line = game_reset(input('Press any key to restart, or X to exit the game '))
		continue
	else:
		a = 'dungeons'
		b = 'tower'
		choice = choice_check(input('The king tells you that the castle is actually a prison, and to escape it, one has to open the red ore with a unique password. The first half of the password is either on the dungeons or on the main tower. Which one do you choose? (Dungeons/Tower) '))
		if choice == a:
			print ('You die in the dungeons after falling into a trapdoor')
			line = game_reset(input('Press any key to restart, or X to exit the game '))
			continue
		else:
			a = int(len(playerinfo['name'][0])**2 * (9/3))
			b = a
			choice = choice_check(input ('After exploring the tower, you find a piece of paper containing the following formula: x = the number of characters on your name ** 2 . (9/3). What is the password? '))
			if choice == str(a):
				password = int(a)
				print('Correct! Now, the last part of the password the product of that number with your age... ')
				if playerinfo['age'][0] == 'null':
					line = game_reset(input("...which you didn't insert correctly. Remember to always be truthful. Game over. Press any key to restart, or X to exit the game "))
				else:
					a = password * int(playerinfo['age'][0])
					b = a
					answer = choice_check(input('...what is the password? '))
					if answer == a:
						print ('Congratulations, you opened the ore and got out of the castle. The king thanks you. Game over.')
						break