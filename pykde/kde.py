from statistics import stdev
from numbers import Real

__all__ = ['fromdata']

def fromdata(data, bandwidth="*1", resolution=1000):
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
        plotpointsy.append( (1/(len(data)*h)) * sum([(3/4)*(1-(((x-val)/h)**2)) if abs((x-val)/h)<=1 else 0 for val in data]) )
        x += pointsep
    return [plotpointsx, plotpointsy]