#!/bin/bash

# ----SOLVED----
# https://code.google.com/codejam/contest/32016/dashboard#s=p2
# loop and read input from user



#functions
DIGIT[0]=0
DIGIT[1]=0
DIGIT[2]=0

function getDigit(){
	rem=$(echo "$1%10" | bc)
	div=$(echo "$1/10" | bc)
	echo %rem
}



read TEST_CASE
for((t=1;t<=TEST_CASE;t++)){
	DIGIT[0]=0
	DIGIT[1]=0
	DIGIT[2]=0
	
	#---take input--- 
	read indice
	answer=$(bc <<< "scale=30;(3+sqrt(5))^$indice")
	
	#---truncate decimal---
	scale=0
	res=$(echo "scale=0;$answer/1" | bc)
	#echo $res
	
	#---take last 3 digits---
	DIGIT[0]=$(echo "$res%10" | bc)
	res=$(echo "$res/10" | bc)
	
	DIGIT[1]=$(echo "$res%10" | bc)
	res=$(echo "$res/10" | bc)
	
	DIGIT[2]=$(echo "$res%10" | bc)
	res=$(echo "$res/10" | bc)
	#---show output---
	printf "Case #%d: " $t		 
	for((i=2;i>=0;i--)){
		printf "%d" ${DIGIT[i]}
	}
	printf "\n"	
}	

		
