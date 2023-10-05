#!/usr/bin/python3
import hidden_4
import re
namelist = dir(hidden_4)
for name in namelist:
    if not name.startswith("_"):
        print('{}'.format(name))
