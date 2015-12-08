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
	disp_word = word
	i = 0
	while(i < length):
		disp_word[i] = '*'
		i = i + 1

	return disp_word;

disp_word = list(word_list[rand_num])

print(create_disp_word(disp_word))
