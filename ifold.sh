#!/bin/bash
echo "Starting RNA folding tests"

while read line;
do
# Finding primary structures
echo; echo;
echo "Finding primary structure for $line"
python2 MCTS-RNA.py -s $line -GC 0.75 -d 0.02 -pk 0
done < testiRnat.txt

echo "Tests have been completed"
