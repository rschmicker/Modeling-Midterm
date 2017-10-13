#!/usr/bin/env python
import math
import plotly
import plotly.graph_objs as go
from scipy import interpolate
from scipy import stats

ys = []
xs = []
with open("alife2.data", "r") as afile:
	for line in afile:
		xs.append(float(line.split("\t")[0]))
		ys.append(float(line.split("\t")[1]))

#slope, intercept, r_value, p_value, std_err = stats.linregress(xs,newys)

trace = go.Scatter(
	x = xs,
	y = ys,
	mode = 'markers',
)

newxs = []
for i in range(len(xs)):
	newxs.append(math.log(xs[i]))

slope2 = 3.16177460359
intercept2 = -16.9102542465
#slope = 3.29134212711
#intercept = -18.6099823031

newys = []
for i in range(len(xs)):
	newys.append(math.log(xs[i]) * slope2 + intercept2)

print(math.log(9700000) * slope2 + intercept2)
"""
newxs = []
for i in range(0, len(xs)):
	newxs.append(math.log(ys[i]))
"""
trace2 = go.Scatter(
	x = xs,
	y = newys,
	mode = 'markers'
)
"""
slope = 0.0747373531351
intercept = -140.731224923

newys = []
for i in range(len(ys)):
	newys.append(math.exp(xs[i] * slope + intercept))

print(math.exp(2030 * slope + intercept))

tck = interpolate.splrep(xs, ys, s=0)

xnew = []
for i in range(xs[0], xs[len(xs)-1]):
	xnew.append(i)
xnew.append(2006)

ynew = interpolate.splev(xnew, tck, der=0)

trace2 = go.Scatter(
	x = xnew,
	y = ynew,
)

newxs = []
for i in range(0,len(xs)):
	newxs.append(pow(xs[i], 2))

slope = 0.185831061656
intercept = -34.6288138355

newxs = []
for i in range(0,len(xs)):
	newxs.append(pow(xs[i], 2) * slope + intercept)
print(pow(5, 2) * slope)

data = [trace, trace2]
"""

data = [trace, trace2]
plot_url = plotly.offline.plot(data, filename='basic-line.html')
