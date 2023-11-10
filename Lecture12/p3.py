#!/usr/bin/python3
with open("remote_in.txt") as file :
   exon=file.read()
seq=exon.split("\n")[1]
windowsize=30
offset=3
starts=list(range(0,len(seq),offset))
segment=[]
for s in starts:
   ends=s+windowsize
   segment.append(seq[s:ends])
print('\n'.join(segment))
for se in segment :
   GC=100*((se.count("G")+se.count("C"))/len(se))
   print(se+"\t"+str(GC)+"%"+"\n")
#write to individual file
header=">segments_"
i=1
import os,subprocess,shutil

for se in segment :
   filename="./output_individuals/"+"segment_"+str(i)+".fasta"
   head=header+str(i)+"\n"
   with open(filename,'w') as file :
       file.write(head+se+"\n")
   i=i+1

#write in one file
with open("segments_all_in_one.fasta",'w') as file :
   i=1
   for se in segment:
     head=header+str(i)+"\n"
     file.write(head+se+"\n")
     i=i+1



