#!/usr/bin/env python
# trapfep.py - integrate compute fep results using the trapezoidal rule

import sys, math

if len(sys.argv) < 3:
    print "Integrate compute fep results using the trapezoidal rule"
    print "usage: trapfep.py temperature hderiv < fep.lmp"
    sys.exit()

rt = 0.008314 * float(sys.argv[1])
hderiv = float(sys.argv[2])

line = sys.stdin.readline()
while line.startswith("#"):
    line = sys.stdin.readline()

v = 1.0
tok = line.split()
if len(tok) == 4:
    v = float(tok[3])
lo = -rt * math.log(float(tok[2]) / v)
    
i = 0
sum = 0.0
for line in sys.stdin:
    tok = line.split()
    if len(tok) == 4:
        v = float(tok[3])
    hi = - rt * math.log(float(tok[2]) / v)
    sum += (hi + lo) / (2 * hderiv)
    lo = hi
    i += 1

print sum / i      # int_0^1: divide by i == multiply by delta
