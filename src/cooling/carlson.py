import cadquery as cq
from math import sin, pi
import numpy as np
plateRadius = 15
plateCenterHole = 4
pinRadius = 3.5/2
pinInter = 18
SCALE= 100 # scale profile dimentions

# input data from csv file of wing profile 
data = np.genfromtxt('data/s7075-il.csv',delimiter=',')
pts = data[9:89]
# if we can normalize vectors< then we can scale it
def normalize(data: np.array) -> np.array:
    '''
    Input numpy 2D array, that describes wing profile
    Putput as list of vector Tuples
    cq.Sketch doent accepts any other format, even list of lists
    ''' 

    res = data/np.linalg.norm(data)
    res = res*SCALE
    res = [tuple(item) for item in res.tolist()]
    return res

pts2 = normalize(pts)

################
# Sketch zone
prof = (
        cq.Sketch()
        .spline(pts2)
        .close()
        .assemble()
        )
# Sketch Zone end


plate = (
        cq.Workplane()
        .circle(plateRadius)
        .circle(plateCenterHole)
        .rect(pinInter,pinInter,forConstruction=True)
        .vertices()
        .circle(pinRadius)
        .extrude(5)
        )

###########
#sweep test
path = (
        (10,-1,10),
        (50,15,-15),
        (100,0,0)
        )
pathWire = cq.Workplane().spline(path)
"""
res = (
        cq.Workplane('YZ')
        .placeSketch(prof)
        .sweep(pathWire)
        )
        """
###########
def makeIt(pts):

    wp = cq.Workplane("XY").polyline(pts).close().workplane()
    result = None
    for i in range(0,20):
        wp2 = (
                wp.transformed(offset=cq.Vector(0, -20, 5),
                    rotate=cq.Vector(1, 0, 0))
                .polyline(pts).close()
                .workplane()
                )
        if result == None:
            result = wp2.loft(combine=True)
        else:
            nextpart = wp2.loft(combine=True)
            result = result.union(nextpart)
        wp = wp.transformed(offset=cq.Vector(0, -5, 5),
            rotate=cq.Vector(18, 0, 0)).polyline(pts).close().workplane()

    show_object(result, options=dict(alpha=0.8,color='blue'))

def makeSweep(pts):
    path = (
            cq.Workplane()

            .parametricCurve(lambda t:(100*sin(t*pi/180),t,0),
                                start=0, stop = 10, N = 1000)
            )
    debug(path)
    res = (
            cq.Workplane('YZ')
            .polyline(pts)
            .close()
            .sweep(path)
            )
    show_object(res, options=dict(aplha=0.7, color='magenta'))


makeSweep(pts2)

