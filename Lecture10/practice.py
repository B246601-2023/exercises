#!/usr/bin/python3
DNAseq="ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
A_num=DNAseq.count('A')
T_num=DNAseq.count('B')
Q=(A_num+T_num)/len(DNAseq)
print("the number of A nucleotides:"+str(A_num))
print("the number of T nucleotides:"+str(T_num))
print(str(Q))

#p2
DNA_A=DNAseq.replace("A","t").replace("T","a").replace("C","g").replace("G","c")
print(DNA_A.upper())

#p3
DNAseq="ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
print(DNAseq.find('AATTC'))
print("length of seq2:"+str(len(DNAseq[22:])))

#p4
DNAseq="ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
firstbase=DNAseq[0:63]
secondbase=DNAseq[90:]
code=firstbase+secondbase
print(code)
print(len(code)/len(DNAseq)*100)
intron=DNAseq[63:90]
print(firstbase+intron.lower()+secondbase)
