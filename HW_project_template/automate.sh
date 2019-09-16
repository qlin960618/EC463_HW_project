#!/bin/bash

SEG_LEN=30
N_SEG=10

#record segment
for i in $(seq 0 $N_SEG); do
	echo "recording "$i
	python3 CaptureMotion.py "./data_"$i  $SEG_LEN -fps 30
	if [ $i -ne 0 ]; then
		python3 CountMotion.py "./data_"$((i-1))"/motion.h5" "dy" > "./data_"$((i-1))"/dy.txt" &
		python3 CountMotion.py "./data_"$((i-1))"/motion.h5" "dx" > "./data_"$((i-1))"/dx.txt" &
	fi
done

#wrapup
python3 CountMotion.py "./data_"$((N_SEG-1))"/motion.h5" "dy" > "./data_"$((N_SEG-1))"/dy.txt" &
python3 CountMotion.py "./data_"$((N_SEG-1))"/motion.h5" "dx" > "./data_"$((N_SEG-1))"/dx.txt" &
