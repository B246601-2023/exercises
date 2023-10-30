#!/usr/bin/python3
import os,shutil,subprocess
with open("plain_genomic_seq.txt") as file:
	local=file.read()

with open("AJ223353_nohead.fasta") as file:
	remote=file.read()

local=local.upper().replace("X","").replace("K","").replace("L","").replace("S","")
remote=remote.replace("\n","")
lcode1=local[0:63]
lcode2=local[63:90]
lcode3=local[90:]
rcode1=remote[0:28]
rcode2=remote[28:409]
rcode3=remote[409:]
with open("local_in.txt",'w') as file :
	file.write(">senuqence1_"+str(len(lcode2))+"\n"+lcode2)

with open("local_ex.txt",'w') as file :
	file.write(">sequence1_"+str(len(lcode1))+"\n"+lcode1+"\n"+">sequence2_"+str(len(lcode3))+"\n"+lcode3)

with open("remote_in.txt",'w') as file :
	file.write(">sequence1_"+str(len(rcode2))+"\n"+rcode2)

with open("remote_ex.txt",'w') as file :
	file.write(">sequence_1"+str(len(rcode1))+"\n"+rcode1+"\n"+">sequence2_"+str(len(rcode3))+"\n"+rcode3)




