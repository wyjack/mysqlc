#!/bin/sh
a=433
b=890
if test $a -ne $b
then
	echo " ok "
else
	echo " filse "
fi

echo  " input a file path "
read path
if test -e $pash  
then
   echo " $path is exist "
   cat $path
else
	echo " $path is not exist "
fi
