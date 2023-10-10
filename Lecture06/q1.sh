#!/bin/bash 
unset IFS
rm -f *.exercise.out
count=0
while read wholeline
do
if test ${wholeline:0:1} != "#"
then
 count=$((count+1))
 read Q_acc S_acc Identity A_length mismatch Gap_opens Q_start Q_end S_start S_end Evalue bit_score <<< ${wholeline}
 echo -e "${Q_acc}\t${S_acc}" >> "subject.exercise.out"
 echo -e "${Identity}\t${A_length}" >> "lenth_percent_ID.exercise.out"
 if ((mismatch > 20))
 then
 echo -e "morethan 20 mismatches: ${Q_acc}\t${S_acc}\t${mismatch}" >> "morethan_20.exercise.out"
  if ((A_length <= 100))
  then
  echo -e "more than 20 mismatches less than 100 amino acids: ${Q_acc}\t${S_acc}\t${mismatch}\t${A_length}" >> "more20less100.exercise.out"
  fi
 else
 continue
 fi
fi
done < blastoutput2.out
echo "There are ${count} lines."

