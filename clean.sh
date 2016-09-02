#!/bin/bash
#bash script to clean up executables and other mess

if [ $# -ne 0 ]
then
	files_to_clean=$(find $1 -type f -executable)
	#echo $files_to_clean
else
	echo "CAUTION: Please Provide Directory Path As Parameter"
fi

echo "FILES TO BE DELETED: "

for file in $files_to_clean
do
	del_file=$( echo $file | grep -v ".sh" )
	
	if [ -n $del_file ]
	then		
		echo $del_file
		rm $del_file
	fi
done









