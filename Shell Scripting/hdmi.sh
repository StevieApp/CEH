#!/bin/bash
if [ -e hdmi.txt ]
	then 
	rm hdmi.txt
fi
locate usr | grep 'hdmi' | cut -d '/' -f 10 | sed -r '/^\s*$/d' | tr -d '.' >> hdmi.txt

findings=`cat hdmi.txt`


for hd in $findings
do
echo $hd
done
