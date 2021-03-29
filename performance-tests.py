MCTS = __import__("MCTS-RNA")
fwrite = open("performance-test-results.txt", "w")
fread  = open("performance-test-sequences.txt", "r")
seq = fread.readline()
while len(seq) != 0:
	if (seq[0] == "#"):
		seq = fread.readline()
		continue
	res = MCTS.MCTS(seq)
	print(res)
	fwrite.write(res)
	seq = fread.readline()

fread.close()
fwrite.close()
