#!/bin/bash
while [ true ]
do
netcat -vlp 3337 &>> passwd.txt
date >> passwd.txt
done

