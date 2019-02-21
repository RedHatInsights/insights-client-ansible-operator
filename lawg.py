#!/usr/bin/env python3.6
import sys
import json

for line in sys.stdin:
    try:
        print(json.loads(line)["msg"])
    except:
        print(line.strip())
