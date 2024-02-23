#!/bin/zsh

for pickle in $(ls *.pkl);
do
  # make the config file
  pkl eval -f json $pickle > config.json
  #find the folder with the same name and put it there
  start=$(pwd)
  cd ../../plugins
  found=1
  for plugin in */;
  do
    cd $plugin
    for skill in */;
    do
      if [ "$(echo $pickle | cut -d '.' -f 1)" = "${skill%/}" ] ;
      then
        cd $skill
        mv $start/config.json .
        found=0
        break
      fi
    done
    if [ $found -eq 0 ];
    then
      break
    fi
  done
done  