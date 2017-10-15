#!/bin/bash

mkdir -p $HOME/bin

for i in $(ls *.py)
do

  if [ ! -f $HOME/bin/$i ]; then
    echo "Installing $i..."
    install $i $HOME/bin
  else
    echo "Skipping $i..."
  fi
done







