#!/bin/bash

#echo out a command that works, thene cho out the exit code

date
echo $?
echo "-----"

#echo out a command that will break
mv -jimmy 
echo $?
echo "----"


