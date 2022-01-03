import cadquery as cq
##ToDO
# Box enclosure with 
# Height = 245mm
# Width = 200mm
# Lenght = 50 mm
# fixes 
# lower  - center 5 mm offset
# 190 mm from lower, 60 mm offset

## PARAMS
width = 201
length = 53
offset = 12
fillet = 3 # actually 5
fixOffset = 5 # mm offset from rect wire
fixOffsetY = 16.5 # mm offset from top of rect
fixPnts = (
        (0, -(width/2+fixOffset)),
        (-(length/2+fixOffset), width/2-fixOffsetY),
        ( length/2+5, width/2-fixOffsetY),
        )
#############
# Sketch Zone!
test_hull = (
        cq.Sketch()
        # Define main geometry
        .rect(width+offset,length+offset,mode='a', tag='outerBase')
        #.wires().offset(-offset,mode='s', tag='innerBase')
        #.vertices().fillet(fillet)
        .push(fixPnts)
        .rect(15,15,mode='a',tag='fix')
        .wires()
        .hull()
        .reset()
        # Cut from main form
        .select('outerBase').wires()
            # offset test print Error  corrected!! Dimentions!!
        .offset(-offset/2,mode='s',tag='innerBase')
        .select('innerBase').vertices().fillet(fillet)
        .push(fixPnts).circle(1,mode='s')
        )

tubeCut = (
        cq.Sketch()
        .rect(4*2,45) # depth of cut *2
        .vertices(">Y")
        .chamfer(2) #.segment((0,0),(-21,0))
        #.arc((-21,0),(0,5),(21,0))
        )

## Sketcj zone End
####################
result = ( cq.Workplane()
        .placeSketch(test_hull)
        .extrude(10)
        .faces('>Y')
        .workplane()
        .placeSketch(tubeCut)
        .cutBlind(-10)
        )
# test tubeCut
#result = result.faces("<Y").workplane().rect(80,80).cutBlind(-190) 

##############

