from statistics import stdev
from numbers import Real
import math

gaussian_coeff = 1/(math.sqrt(2*math.pi))

__all__ = ['fromdata']

def fromdata(data, bandwidth="*1", kernal='uniform', resolution=1000):
    try:
        h = float(bandwidth[1:]) * 1.06*stdev(data)*(len(data)**(-1/5))
    except:
        try:
            h = float(bandwidth)
        except:
            h = 1.06*stdev(data)*(len(data)**(-1/5))
    
    plotstart = min(data)-h
    plotstop = max(data)+h
    pointsep = (plotstop-plotstart) / resolution
    
    plotpointsx = []
    plotpointsy = []
    x = plotstart
    while x < plotstop:
        plotpointsx.append(x)
        plotpointsy.append( (1/(len(data)*h)) * sum([kernal_fucnt(kernal, (x-val)/h) for val in data]) )
        x += pointsep
    return [plotpointsx, plotpointsy]
    
def gaussian_bandwidth_estimation(data):
    return 1.06 * stdev(data) * (len(data)**(-1/5))
    
def kernal_fucnt(kernal, u):
    if kernal == 'epanechnikov':
        if abs(u) <= 1:
            return (3/4)*(1-(u**2))
        else:
            return 0
    elif kernal == 'uniform':
        if abs(u) <= 1:
            return 1/2
        else:
            return 0
    elif kernal == 'gaussian':
        return gaussian_coeff * (math.e**((u**2)*(-1/2)))
    elif kernal == 'triangular':
        if abs(u) <= 1:
            return 1 - abs(u)
        else:
            return 0
            