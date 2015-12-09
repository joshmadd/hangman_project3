import random
import sys
import os

# creates the list of words to choose from
word_list = ["APPLE", "BANANA", "BLUEBERRY", "CHERRY", "GRAPE",
	"GRAPEFRUIT", "KIWI", "LEMON", "LIME", "MANGO",
	"NECTARINE", "ORANGE", "PEACH", "PINEAPPLE", "STRAWBERRY"]

# uses the secret word to create the display word
# it does this by setting the contents of the secret word
# to a new list and changing all the contents to *
def create_disp_word(word):
	length = len(word)
	disp_word = list(word)
	i = 0
	while(i < length):
		disp_word[i] = '*'
		i = i + 1
	return disp_word;

# checks to see if the entered letter is in the secret word
# and updates the displayed word if the entered letter is there
# otherwise, it makes no changes
def check_sec_word(secret, display, letter):
	i = 0
	while(i < len(secret)):
		if letter[0] == secret[i]:
			display[i] = secret[i]
		i = i + 1
	return display

# checks to see if the lists entered as parameters to the
# function are equal.  returns 0 if they are and 1 if they aren't
def first_isnt_sec(first, second):
	i = 0
	while(i < len(first)):
		if first[i] != second[i]:
			return 1
		else: 
			i = i + 1
	return 0

play = 'Y'

while(play[0] == 'Y'):
	# picks a random number to be used in selecting a random word
	# and sets values to begin and maintain the game
	rand_num = random.randrange(0, 15)
	turns = 6
	sec_word = list(word_list[rand_num])
	disp_word = create_disp_word(sec_word)
	
	print("\n")
	print(''.join(disp_word))
	
	# welcome message to the game
	print("\nWelcome to the game of Hangman!")
	print("Please enter a letter to begin guessing")
	print("the word displayed above to try and save")
	print("your man from the gallows.  Good luck!")
	
	# the game runs until the user wins by guessing all the letters
	# or until the user loses by running out of turns
	while((turns > 0) and (first_isnt_sec(sec_word, disp_word))):
		
		# gets a letter from the user
		letter = sys.stdin.readline().upper()
		print("\n")
		temp_word = list(disp_word)	
		disp_word = check_sec_word(sec_word, disp_word, letter)
		
		# checks to see if the letter entered was in the secret word and then
		# displays the appropriate message based on the letter's existence
		if(not first_isnt_sec(temp_word, disp_word)):
			turns = turns - 1
			print("Oh, no! Your letter wasn't in the word!")
			if(turns > 1):
				print "Try again, you only have", turns, "mistakes left!"
			elif(turns == 1):
				print "Try again, you only have", turns, "mistake left!"
		elif(first_isnt_sec(sec_word, disp_word) and turns > 0):
			print("Good job!  Now try for the other letters.")
		
		# the visual display of the hangman based on how many turns are left
		print("_______")
		print("      |")
		print("      |")
		print("      |")
		if(turns < 6):
			print("     000")
			print("    0   0")
			print("    0   0")
			print("     000")
		if(turns == 4):
			print("      0")
			print("      0")
			print("      0")
			print("      0")
		elif(turns == 3):
			print("      0")
			print("     00")
			print("    0 0")
			print("   0  0")
		elif(turns <= 2):
			print("      0")
			print("     000")
			print("    0 0 0")
			print("   0  0  0")
		if(turns == 1):
			print("     0")
			print("    0")
			print("   0")
			print("  0")
		if(turns == 0):
			print("     0 0")
			print("    0   0")
			print("   0     0")
			print("  0       0")
		print("\n")
		print(''.join(disp_word))
	
	# gives output based on if the user won or lost
	# and asks if they want to play again
	if(turns == 0):
		print("Sorry, you lost your man to the gallows!")
	else:
		print("Congratulations, you saved the man from the gallows!")
	print("Well, that's game over.  Would you like to try and save someone else? (Y/N)")
	play = sys.stdin.readline().upper()

print("\nCome play again!\n")
