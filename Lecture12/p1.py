#!/usr/bin/python3
with open("input.txt") as file :
  input=file.read()
code=input.split("\n")
del code[5]
i=0
for c in code:
   code[i]=c[14:]
   i+=1
#save file
file=open("noadaptor.txt",'w')
for clean in code :
   file.write(clean+'\n')
   clean
file.close()
