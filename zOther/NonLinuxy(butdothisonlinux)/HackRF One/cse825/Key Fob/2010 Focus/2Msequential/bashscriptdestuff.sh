#!/bin/bash

#########CANNOT APPEND VARNAME W/ _modname, but can use .modname #################
for file in *.txt; do python3 messageBuilderV2.1.py -sig $file -out $file.destuff.txt; done		#echo $file


#for f in *.txt; do python3 messageBuilder.py -sig $f -out $f.convtxt; done
