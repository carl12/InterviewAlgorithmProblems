'''
Problem: given an array of characters, reverse the order of the words in the array

'''
import random
import string
import f_timer
import copy

def reverseWords(arr):
	reverseSubarr(arr, 0, len(arr))
	start = 0
	for i in range(len(arr)):
		if arr[i] == ' ':
			reverseSubarr(arr, start, i)
			start = i+1
	reverseSubarr(arr, start, len(arr))
	return arr

def reverseSubarr(arr, low, high):
	while low < high:
		tmp = arr[low]
		arr[low] = arr[high - 1]
		arr[high - 1] = tmp
		low += 1
		high -= 1
	return arr

def reverseWords2(arr):
	newArr = []
	endOfWord = len(arr) - 1

	for i in reversed(range(len(arr))):
		if arr[i] == ' ':
			j = i+1
			while j <= endOfWord:
				newArr.append(arr[j])
				j += 1
			endOfWord = i-1
			newArr.append(' ')

	j = 0
	while j <= endOfWord:
		newArr.append(arr[j])
		j += 1
	return newArr


def genRandomSentence(maxNumWords, maxWordLength):
	numWords = random.randint(0,maxNumWords)
	output = []
	for i in range(numWords):
		wordLength = random.randint(0,maxWordLength)
		for _ in range(wordLength):
			output.append(random.choice(string.ascii_letters))
		output.append(' ')
	if(numWords > 0):
		output.pop()
	return [output]



print(f_timer.time_funcs([reverseWords, reverseWords2], genRandomSentence, [100,100], 1000))


