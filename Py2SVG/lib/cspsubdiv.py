#!/usr/bin/env python  
from bezmisc import *  
from ffgeom import *  
  
def maxdist(p0x,p0y,p1x,p1y,p2x,p2y,p3x,p3y):  
    p0 = Point(p0x,p0y)  
    p1 = Point(p1x,p1y)  
    p2 = Point(p2x,p2y)  
    p3 = Point(p3x,p3y)  
  
    s1 = Segment(p0,p3)  
    return max(s1.distanceToPoint(p1),s1.distanceToPoint(p2))  
      
  
def cspsubdiv(csp,flat):  
    for sp in csp:  
        subdiv(sp,flat)  
  
def subdiv(sp,flat,i=1):  
    p0 = sp[i-1][1]  
    p1 = sp[i-1][2]  
    p2 = sp[i][0]  
    p3 = sp[i][1]
    
    m = maxdist(p0[0], p0[1], p1[0], p1[1], p2[0], p2[1], p3[0], p3[1])  
    if m <= flat:  
        try:  
            subdiv(sp,flat,i+1)  
        except IndexError:  
            pass  
    else:  
        one, two = beziersplitatt(p0[0], p0[1], p1[0], p1[1], p2[0], p2[1], p3[0], p3[1],0.5)  
        sp[i-1][2] = one[1]  
        sp[i][0] = two[2]  
        p = [one[2],one[3],two[1]]  
        sp[i:1] = [p]      
        subdiv(sp,flat,i)  
