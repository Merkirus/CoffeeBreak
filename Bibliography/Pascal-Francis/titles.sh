#!/bin/bash

for file in *.txt
do
	grep 'title' $file >> titles
done
