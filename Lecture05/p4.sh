#!/bin/bash
rm -f *.details
unset IFS
IFS=$'\t'
count=0
while read name email city birthday_day birthday_month birthday_year country
do
if test -z ${name}
 then
 continue
 else
 if test ${birthday_month} == "10"
 then 
 count=$((count+1))
 echo "Outputfile will be in ${birthday_month}.details"
 echo -e "${count}\t${name}\t${country}" >> "October.details"
 else
 continue
 fi
fi
done < example_people_data.tsv
echo "There are ${count} people were born in October." >> "October.details"
