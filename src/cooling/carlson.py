import cadquery as cq
import csv 
plateRadius = 15
plateCenterHole = 4
pinRadius = 3.5/2
pinInter = 18

plate = (
        cq.Workplane()
        .circle(plateRadius)
        .circle(plateCenterHole)
        .rect(pinInter,pinInter,forConstruction=True)
        .vertices()
        .circle(pinRadius)
        )
res  = plate.extrude(10)

