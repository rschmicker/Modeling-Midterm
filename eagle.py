#!/usr/bin/env python
import math
import plotly
import plotly.graph_objs as go
from scipy import interpolate
from scipy import stats

ys = []
xs = []
with open("eagle.data", "r") as efile:
	for line in efile:
		xs.append(int(line.split("\t")[0]))
		ys.append(int(line.split("\t")[1]))

#slope, intercept, r_value, p_value, std_err = stats.linregress(xs,newys)

trace = go.Scatter(
	x = xs,
	y = ys,
	mode = 'markers',
)

newxs = []
for i in range(0, len(xs)):
	newxs.append(math.log(ys[i]))

trace2 = go.Scatter(
	x = xs,
	y = newxs,
)

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

"""
newxs = []
for i in range(0,len(xs)):
	newxs.append(pow(xs[i], 2))

slope = 0.185831061656
intercept = -34.6288138355

newxs = []
for i in range(0,len(xs)):
	newxs.append(pow(xs[i], 2) * slope + intercept)
"""
"""
print(pow(5, 2) * slope)

data = [trace, trace2]
"""

data = [trace, trace2]
plot_url = plotly.offline.plot(data, filename='basic-line.html')
