import os
import GCcount
import sys
sys.path.append('/usr/local/lib/python2.7/site-packages/')
import RNA
import time
fwrite = open("performance-test-results.txt", "a")
fread  = open("performance-test-sequences.txt", "r")
seq = fread.readline()
fwrite("Runtime,GCcontent,GCdistance,StructureDistance")
fwrite.flush()
while len(seq) != 0:
	seq = seq.replace("\n", "")
	if (seq[0] == "#"):
		seq = fread.readline()
		continue
	fwrite.write(seq + ",")
	fwrite.flush()
	time.sleep(.5)
	gc = GCcount.GCcount(seq)
	seq = RNA.fold(seq)[0]
	os.system("python2 MCTS-RNA.py -s \"" + seq + "\" -GC " + str(gc) + " -d 0.02 -pk 0")
	seq = fread.readline()

fread.close()
fwrite.close()