#!/bin/bash
unset IFS
IFS=$'\t'
count=0
while read name email city birthday_day birthday_month birthday_year country
do
 if test -z ${name} || test ${country} == "country"
 then
 continue
 else 
 count=$((count+1))
 echo "outputfile will be ${country// /}.details"
 echo -e "${count}\t${name}\t${email}\t${city}\t${country}" >> "${country// /}.details"
 fi
done < example_people_data.tsv
