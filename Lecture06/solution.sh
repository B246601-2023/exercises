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

IFS=$'\t'
count1=0
count2=0
group1cut=150
group2cut=250
group3cut=350
while read wholeline
do
if test ${wholeline:0:1} != "#";
then
 echo "${wholeline}" >> "sortlines.out"
 read Q_acc S_acc Identity A_length mismatch Gap_opens Q_start Q_end S_start S_end Evalue bit_score <<< ${wholeline}
 if [[ ${S_acc} == *"AEI"* ]]
 then
 echo -e "${S_acc}\t${S_start}" >> "string_AEI.exercise.out"
 fi
 if ((A_length < 100))
 then
 count1=$((count1+1))
 fi
 if ((mismatch < 20)) && ((count2 < 20))
  then
  count2=$((count2+1))
  echo -e "lessthan 20 mismatches: ${Q_acc}\t${S_acc}\t${mismatch}" >> "lessthan_20.exercise.out"
 fi
 percent=$((100*${mismatch}/${A_length}))
 echo -e "${A_length}\t${mismatch}\t${percent}%" >> "percent.exercise.out"
 scorebin=1
 if [ ${bit_score} -gt  ${group3cut} ]
 then 
     scorebin=4
 fi
 if [ ${bit_score} -le ${group3cut} ] && [ ${bit_score} -gt ${group2cut} ]
 then
     scorebin=3
 fi
 if [ ${bit_score} -le ${group2cut} ] && [ ${bit_score} -gt ${group1cut} ]
 then 
     scorebin=2
 fi

scoregroupdetails=$(echo -e "${Q_acc}\t${S_acc}\t${bit_score}")
case $scorebin in
  4) 
    echo -e "${scoregroupdetails}" >> "group4.exercise.out"
    ;;
  3) 
    echo -e "${scoregroupdetails}" >> "group3.exercise.out"
    ;;
  2) 
    echo -e "${scoregroupdetails}" >> "group2.exercise.out"
    ;;
  1) 
    echo -e "${scoregroupdetails}" >> "group1.exercise.out"
    ;;
esac
 fi
done < blastoutput2.out
echo "There are ${count1} HSPs less than 100 amino acids."
count3=$(cut -d $'\t' -f2 sortlines.out | uniq -d | wc -l)
cat sortlines.out | sort -t$'\t' -k12,12nr | head -10 > "top10_best.exercise.out"

echo "There are ${count3} subject sequences have more than one HSP."
rm -f sortlines.out
