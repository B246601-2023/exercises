#!/usr/bin/python3
import os,shutil,subprocess
#print out species Drosophila melanogaster or Drosophila simulans
with open("data.csv") as file :
    print("gene names from the species Drosophila melanogaster or Drosophila simulans")
    for line in file :
       line=line.rstrip('\n')
       if (
           line.startswith("Drosophila melanogaster") or line.startswith("Drosophila simulans")
          ):
           gene_name=line.split(',')[2]
           print(gene_name)

#print genes that are between 90 and 110 bases long
with open("data.csv") as file :
    print("all genes that are between 90 and 110 bases long")
    for line in file :
       line=line.rstrip('\n')
       gene_name=line.split(',')[2]
       gene_seq=line.split(',')[1]
       gene_l=len(gene_seq)
       if(
         gene_l>=90 and gene_l<=110
        ):
         print(gene_name)

#Print out the gene names for all genes whose AT content is less than 0.5 and whose expression level is greater than 200
with open("data.csv") as file :
    print("AT content is less than 0.5 and expression level is greater than 200")
    for line in file :
       line=line.rstrip('\n')
       gene_name=line.split(',')[2]
       gene_seq=line.split(',')[1]
       gene_l=len(gene_seq)
       A=gene_seq.count('a')
       T=gene_seq.count('t')
       AT_level=(A+T)/gene_l
       gene_exp=int(line.split(',')[3])
       if(
          AT_level<=0.5 and gene_exp>=200
         ):
          print(gene_name)
#For each gene, print out a message giving the gene name and saying whether its AT content is high (greater than 0.65), low (less than 0.45) or medium (between 0.45 and 0.65).
with open("data.csv") as file :
    print("AT content level")
    for line in file :
       line=line.rstrip('\n')
       gene_name=line.split(',')[2]
       gene_seq=line.split(',')[1]
       gene_l=len(gene_seq)
       A=gene_seq.count('a')
       T=gene_seq.count('t')
       AT_level=(A+T)/gene_l
       if(AT_level<0.45):
          print(gene_name+'\t'+"low")
       elif(AT_level>=0.45 and AT_level<=0.65):
          print(gene_name+'\t'+"medium")
       elif(AT_level>0.65):
          print(gene_name+'\t'+"high")
