#!/bin/bash

echo "initialized"
sleep 5
echo "script initialized"
SEG_LEN=30
N_SEG=10
path_prefix="/home/pi/HW_Project/HW_project_template"

echo "removing old data"
rm -r $path_prefix/data_*

echo "begin collection"

#record segment
for i in $(seq 0 $N_SEG); do
	echo "recording "$i
	python3 /home/pi/HW_Project/HW_project_template/CaptureMotion.py $path_prefix"/data_"$i  $SEG_LEN -fps 30
	sleep 0.5
	if [ $i -ne 0 ]; then
		python3 /home/pi/HW_Project/HW_project_template/CountMotion.py $path_prefix"/data_"$((i-1))"/motion.h5" "dy" > $path_prefix"/data_"$((i-1))"/dy.txt" &
		python3 /home/pi/HW_Project/HW_project_template/CountMotion.py $path_prefix"/data_"$((i-1))"/motion.h5" "dx" > $path_prefix"/data_"$((i-1))"/dx.txt" &
	fi
done

#wrapup
python3 /home/pi/HW_Project/HW_project_template/CountMotion.py $path_prefix"/data_"$((N_SEG))"/motion.h5" "dy" > $path_prefix"/data_"$((N_SEG))"/dy.txt" &
python3 /home/pi/HW_Project/HW_project_template/CountMotion.py $path_prefix"/data_"$((N_SEG))"/motion.h5" "dx" > $path_prefix"/data_"$((N_SEG))"/dx.txt" &
