#!/bin/bash
str=$(ps aux | egrep proxyserver.py | sed -e  's\....[ ]*\\' | sed 's:\(.....\).*$:\1:')
for word in $str
do
  echo -e 'kill ' $word
  sudo kill -9 $word
done

