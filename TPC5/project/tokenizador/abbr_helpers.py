#!/usr/bin/env python3

import re
import os

def jsonFromAbr(lang :str) -> dict:
    path = os.path.dirname(__file__)
    f =  open(path + "/data/" + lang, "r")
    res = {}
    for line in f.readlines():
        if match := re.match(r'(.*?\.) \: (.*?)$', line):
            res[match.group(1).lower()] = match.group(2)

    return res
