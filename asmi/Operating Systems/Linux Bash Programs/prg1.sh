#!/bin/bash

if [ "$1" != "$2" ] && cmp -s -- "$1" "$2";
then
	echo "File contents are same"
	echo "Removed $2"
	rm -- "$2"
else
	echo "File contents are different"
fi
