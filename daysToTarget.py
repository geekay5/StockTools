#!/usr/bin/env python3

import sys

def daysToTgt(base, circuitLimit, target):
    days = 0
    while base < target:
        base = base + (base * circuitLimit / 100)
        days += 1
    return days

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: ./daysToTarget.py <base> <circuitLimit> <target>")
        exit(1)
    base = int(sys.argv[1])
    circuitLimit = int(sys.argv[2])
    target = int(sys.argv[3])
    print("Target will be achieved in {0} days".format(daysToTgt(base, circuitLimit, target)))