#!/bin/bash

source /home/frafau/Documents/Bibliography/venv/bin/activate

for file in *.txt
do
	python xml_to_json.py $file
done

