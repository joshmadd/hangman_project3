import random
import sys
import os

word_list = ["APPLE", "BANANA", "BLUEBERRY", "CHERRY", "GRAPE",
	"GRAPEFRUIT", "KIWI", "LEMON", "LIME", "MANGO",
	"NECTARINE", "ORANGE", "PEACH", "PINEAPPLE", "STRAWBERRY"]

rand_num = random.randrange(0, 15)
print(rand_num)

def create_disp_word(word):
	length = len(word)
	disp_word = list(word)
	i = 0
	while(i < length):
		disp_word[i] = '*'
		i = i + 1
	return disp_word;

def check_disp_word(secret, display, letter):
	i = 0
	while(i < len(secret)):
		if letter[0] == secret[i]:
			display[i] = secret[i]
		i = i + 1
	return display

sec_word = list(word_list[rand_num])
disp_word = create_disp_word(sec_word)
temp_disp = ''.join(disp_word)

print(sec_word)

print("\nWelcome to the game of Hangman!")
print("Please enter a capitalized letter to begin")
print("guessing the word displayed above.  Good luck!")

letter = sys.stdin.readline().upper()
print(letter)

disp_word = check_disp_word(sec_word, disp_word, letter)
print(disp_word)
