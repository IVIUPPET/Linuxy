#!/bin/bash

#########CANNOT APPEND VARNAME W/ _modname, but can use .modname #################
for file in *.txt; do python3 messageBuilder.py -sig $file -out $file.hex.txt; done		#echo $file


#for f in *.txt; do python3 messageBuilder.py -sig $f -out $f.convtxt; done
