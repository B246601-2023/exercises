#!/bin/bash
unset IFS
IFS=$'\t'
count=0
while read name email city birthday_day birthday_month birthday_year country
do
  count=$((count+1))
  echo -e "${count}\t${country}"
done 
