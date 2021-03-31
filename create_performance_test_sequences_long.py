import sequence_generator as sg

f = open("performance_test_sequences_long.txt", "w")
l = 100
while l <= 300:
    f.write("#Sequences of length: " + str(l) + "\n")
    j = 0
    while j < 15:
        seq = sg.createSequence(l)
        f.write(seq + "\n")
        j+=1
    l += 25

f.close()