﻿#!/usr/bin/env python
# file: kill-group.py
# author: Artur Skonecki
# website: http://adb.cba.pl
# description: kill recursively all windows in a group

import sys
import tools

session=sys.argv[1]
min=int(sys.argv[3])
max=int(sys.argv[2])
groupids=sys.argv[4:]
tools.kill_group(session,min,max,groupids)
