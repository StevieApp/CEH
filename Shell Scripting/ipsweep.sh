#!/bin/bash
if [ "$1" != "" ] && [ "$2" != "" ] && [ "$3" != "" ] && [ "$4" != "" ]
then
if [ -e $3 ]
then
rm $3
fi
if [ -e $4 ]
then
rm $4
fi	
for ip in `seq 254` 
do
ping -c 1 $1.$ip | grep "64 bytes" | cut -d " " -f 4 | tr -d ":" >> $3&
ping -c 1 $2.$ip | grep "64 bytes" | cut -d " " -f 4 | tr -d ":" >> $4&
done
else
	if [ "$1" == "" ] 
	then 
	echo "Enter the first IP address scope with syntax 'n.n.n' eg 192.168.1"
	elif [ "$2" == "" ]
	then
	echo "Enter the second IP address scope with syntax 'n.n.n' eg 192.168.1"
	elif [ "$3" == "" ]
	then 
	echo "Enter the destination for the first IP address scope"
	elif [ "$4" == "" ]
	then
	echo "Enter the destination for the second IP address scope"
	else
	echo "good"
	fi
fi
