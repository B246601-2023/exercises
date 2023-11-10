#!/usr/bin/python3
import sys,os,numpy
import pandas as pd
df=pd.read_csv("eukaryotes.txt")
df=pd.read_csv("eukaryotes.txt",sep="\t",na_values=['-'])
len(df[df.apply(lambda x : x['Group']=='Fungi' and x['Size (Mb)']>100,axis=1)])
big_fungi=df.loc[(df['Group']=='Fungi') & (df['Size (Mb)']>100),['#Organism/Name']]
sorted(list(big_fungi['#Organism/Name']))
Groups=list(df['Group'].drop_duplicates())
for g in Groups:
   count=len(df[df['Group']==g])
   count_uniq=len(df[df['Group']==g].drop_duplicates('#Organism/Name'))
   print(str(count)+" genomes for "+g+"("+str(count_uniq)+" unique)")
hel=df[df.apply(lambda x : x['#Organism/Name'].startswith('Heliconius'),axis=1)]
hel[['#Organism/Name','Heliconius']]
cendf=df[df['Group']=='Plants'][['Group','Center']]
cendf['Center'].value_counts()

df[['#Organism/Name','Genes','Proteins','P/G']].apply(lambda x : x['P/G']>=1.1,axis=1).value_counts()
