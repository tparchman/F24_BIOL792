#!/bin/bash
## mac2unix.sh
## description: converts mac (\r) to unix (\n) line endings, writes new file.
## usage: bash mac2unix.sh STDIN

#echo $@
echo $1
echo $2
echo $8


for myfile in $@; do
cat $myfile | tr '\r' '\n' &> unixendings_$myfile
done

