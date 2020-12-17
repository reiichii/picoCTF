#!/bin/sh
file="./1000.tar"
echo "Hello, World!"

for i in {3..998}
do
    rm "$i.tar"
done