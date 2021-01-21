#! /bin/bash


file="$PWD"/"$( basename "pidNo.txt" )"
if [ ! -f "$file" ]
then	
	echo "Starting python script micStreaming.py"
	python3 "$PWD"/"$( basename "micStreaming.py" )"
else
	curPID=$(<"$file")
	PID="$(pgrep -f micStreaming.py &)"
	if [ "$curPID" != "$PID" ]
	then
		rm $file
		python3 "$PWD"/"$( basename "micStreaming.py" )"	
	else		
		x=0
	fi 
fi
