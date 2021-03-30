import sequence_generator as sg

f = open("performance_test_sequences.txt", "w")
i = 0
while i < 20:
	i += 1
	f.write("#Sequences of length: " + str(10*i) + "\n")
	j = 0
	while j < 20: # number of sequences of len 10*i in the test
		seq = sg.createSequence(10*i)
		f.write(seq + "\n")
		j+=1

i = 225
while i <= 500:
    f.write("#Sequences of length: " + str(i) + "\n")
    j = 0
    while j < 10:
        seq = sg.createSequence(i)
        f.write(seq + "\n")
        j+=1
    i += 25

f.close()
