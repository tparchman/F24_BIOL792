#!/usr/bin/env python3

import re
import sys
from collections import defaultdict

IN = open("sample_passerina.fastq", 'r')
OUT = open("seq_count.txt", 'w')
# ID_ctr={}
ID_Ctr = defaultdict(int)


for Line in IN:
	Line.strip('\n')
	if re.search("^@(\w+)", Line):
		M=re.search("^@(\w+)", Line)
		ID = M.group(1)
		ID_Ctr[ID] += 1
		

for thing in ID_Ctr.keys():
	print(thing, ID_Ctr[thing]) 

#	OUT.write("ID: %s, No of seqs: %s \n" % (thing, ID_ctr[thing]))
	