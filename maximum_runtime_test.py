import sequence_generator as sg
import GCcount
import sys
sys.path.append('/usr/local/lib/python2.7/site-packages/')
import RNA
import os
i = 1
while i < 11:
    seq = sg.createSequence(i*100)
    gc = GCcount.GCcount(seq)
    seq = RNA.fold(seq)[0]
    os.system("python2 MCTS-RNA.py -s \"" + seq + "\" -GC " + str(gc) + " -d 0.02 -pk 0")
    i += 1