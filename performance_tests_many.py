import os
import GCcount
import sys
sys.path.append('/usr/local/lib/python2.7/site-packages/')
import RNA
fwrite = open("performance_test_results_many.csv", "a")
fread  = open("performance_test_sequences_many.txt", "r")
seq = fread.readline()
fwrite.write("Sequence,SecondaryStructure,Length,Runtime,GCcontent,GCdistance,StructureDistance\n")
while len(seq) != 0:
	seq = seq.replace("\n", "")
	if (seq[0] == "#"):
		seq = fread.readline()
		continue
	fwrite.write(seq + ",")
	gc = GCcount.GCcount(seq)
	seq = RNA.fold(seq)[0]
	fwrite.write(seq + ",")
	fwrite.write(str(len(seq)) + ",")
	fwrite.flush()
	os.system("python2 MCTS-RNA.py -s \"" + seq + "\" -GC " + str(gc) + " -d 0.02 -pk 0")
	seq = fread.readline()

fread.close()
fwrite.close()