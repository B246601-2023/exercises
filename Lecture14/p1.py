#!/usr/bin/python3
def animo_count_v1(seq,acid,sig=2):
    length=len(seq)
    counts=seq.upper().count(acid.upper())
    precentage=counts*100/length
    return round(precentage,sig)

def animo_count_v2(seq,acid=['A','I','L','M','F','W','Y','V'],sig=2):
    length=len(seq)
    la=len(acid)
    seq=seq.upper()
    counts=0
    for a in acid:
       a=a.upper()
       counta=seq.count(a)
       counts=counts+counta
    precentage=counts*100/length
    return round(precentage,sig)

def base_counter(seq,threshold=50):
    seq=seq.upper()
    length=len(seq)
    g=["A","G","C","T"]
    count=0
    for base in seq :
      if base in g :
         continue
      else :
        count=count+1
    precentage=count*100/length
    if round(precentage,1) < threshold:
       return(False)
    else :
       return(True)

