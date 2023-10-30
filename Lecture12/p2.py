#!/usr/bin/python3
with open("exons.txt") as file :
   location=file.read().split("\n")
del location[4]
with open("genomic_dna2.txt") as file :
  dna2=file.read()
#generate exons
exons=[]
for l in location:
   l=l.split(",")
   s=int(l[0])-1
   e=int(l[1])
   exons.append(dna2[s:e])
with open("joined_exons.txt",'w') as file :
  file.write(">Lecture12_exercise2_codingseq"+"\n"+''.join(exons))

