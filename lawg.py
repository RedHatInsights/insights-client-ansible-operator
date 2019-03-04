#!/usr/bin/env python3.6
import sys
import json

for line in sys.stdin:
    try:
        json.loads(line)
        sys.stdout.write(line)
    except:
        sys.stdout.write(json.dumps({"msg": line.strip()}))
        sys.stdout.write("\n")
    finally:
        sys.stdout.flush()
