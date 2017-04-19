#~ /bin/bash

for file in /1lock/*
do
	xxd $file > $file.txt
done

