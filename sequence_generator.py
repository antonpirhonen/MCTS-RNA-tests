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
	
# f = open("performance-test-sequences.txt", "a")
# i = 0
# while i < 20:
# 	i += 1
# 	f.write("#Sequences of length: " + str(10*i) + "\n")
# 	j = 0
# 	while j < 10:
# 		seq = createSequence(10*i)
# 		f.write(seq + "\n")
# 		j+=1
	
# f.close()

