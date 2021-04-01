import sequence_generator as sg

f = open("performance_test_sequences_many.txt", "w")
l = 10
while l <= 150:
    f.write("#Sequences of length: " + str(l) + "\n")
    j = 0
    while j < 150:
        seq = sg.createSequence(l)
        f.write(seq + "\n")
        j+=1
    l += 10

f.close()