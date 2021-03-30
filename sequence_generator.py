import sys
import random
def randomNucleotide():
	r = random.randrange(4)
	if r == 0:
		return "A"
	if r == 1:
		return "C"
	if r == 2:
		return "G"
	if r == 3:
		return "U"
	raise Exception("Choosing a random nucleotide failed.")
	
def createSequence(length):
	array = [0] * length
	i = 0
	while i < length:
		array[i] = randomNucleotide()
		i += 1
	return "".join(array)
