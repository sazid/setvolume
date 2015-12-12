#!/usr/bin/python

# Bismillahir Rahmanir Rahim, ALLAHU AKBAR
# @author: sazid
# MIT License

import sys
from subprocess import call

if len(sys.argv) <= 1 or len(sys.argv) > 2:
    print "Bad argument(s)"
    print "Usage: \"setvolume.py 70\" to set the volume to 70%"
    print "You can also increase the volume above 100% like 150% or 200%"
else:
    volume_percent = sys.argv[1] + "%"
    call(["pactl", "set-sink-volume", "0", volume_percent])
