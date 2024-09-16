#!/bin/bash
## cut_column3.sh
## description: cuts 3rd column from any number of input files
## usage: bash cut_column3.sh STDIN

echo $@

for myfile in $@; do
cut -f 3 -d "," $myfile &> column3_$myfile
done

