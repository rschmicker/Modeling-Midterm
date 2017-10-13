#!/usr/bin/env python
import math
import random

ymin = 0
ymax = 2
xmin = 1
xmax = 10
n = xmax
insidepoints = 0

rectange_area = (xmax - xmin) * (ymax - ymin)

for i in range(n):
	randy = random.uniform(ymin, ymax)
	randx = random.uniform(xmin, xmax)
	if randy <=  2 * math.exp(1 - (randx ** 2)):
		insidepoints += 1
fnArea = float(rectange_area) * float(insidepoints) / float(n)
print(fnArea)
