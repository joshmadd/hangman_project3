import random
import sys
import os

word_list = ["APPLE", "BANANA", "BLUEBERRY", "CHERRY", "GRAPE",
	"GRAPEFRUIT", "KIWI", "LEMON", "LIME", "MANGO",
	"NECTARINE", "ORANGE", "PEACH", "PINEAPPLE", "STRAWBERRY"]

def create_disp_word(word):
	length = len(word)
	disp_word = list(word)
	i = 0
	while(i < length):
		disp_word[i] = '*'
		i = i + 1
	return disp_word;

def check_sec_word(secret, display, letter):
	i = 0
	while(i < len(secret)):
		if letter[0] == secret[i]:
			display[i] = secret[i]
		i = i + 1
	return display

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
	rand_num = random.randrange(0, 15)
	turns = 6
	
	sec_word = list(word_list[rand_num])
	disp_word = create_disp_word(sec_word)
	
	print(''.join(sec_word))
	print(''.join(disp_word))
	
	print("\nWelcome to the game of Hangman!")
	print("Please enter a letter to begin guessing")
	print("the word displayed above to try and save")
	print("your man from the gallows.  Good luck!")
	
	while((turns > 0) and (first_isnt_sec(sec_word, disp_word))):
		letter = sys.stdin.readline().upper()
		temp_word = list(disp_word)	
		disp_word = check_sec_word(sec_word, disp_word, letter)
		print("\n")
		if(not first_isnt_sec(temp_word, disp_word)):
			turns = turns - 1
			if(turns > 0):
				print("Oh, no! Your letter wasn't in the word!")
				print "Try again you only have", turns, "turns left!\n"
		elif(first_isnt_sec(sec_word, disp_word) and turns > 0):
			print("Good job!  Now try for the other letters.\n")
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
	if(turns == 0):
		print("Sorry, you lost your man to the gallows!")
	else:
		print("Congratulations, you saved the man from the gallows!")
	print("Well, that's game over.  Would you like to try and save someone else? (Y/N)")
	play = sys.stdin.readline().upper()

print("Come play again!\n")
