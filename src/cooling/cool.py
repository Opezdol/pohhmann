import cadquery as cq
##ToDO
# Box enclosure with 
# Height = 245mm
# Width = 200mm
# Lenght = 50 mm
# fixes 
# lower  - center 5 mm offset
# 190 mm from lower, 60 mm offset
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

tm = (
        # base box with thick offset of offset
        cq.Workplane()
        .box(length+offset,width+offset,offset)
        # estetic fillets to box
        .edges('|Z').fillet(fillet)
        .faces('<Z').edges().fillet(fillet)
        # top face for sketch
        #_______
        # SKETCH
        .faces('>Z')
        .sketch()
        .rect(width+offset,length+offset,tag='base')
        .rect(width,length, mode='s',tag='base1')
        .select('base','base1')
        .vertices()
        .fillet(fillet)
        .finalize()
        #______SKETCH_END______

        .extrude(50)
        )

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
result = (
        cq.Workplane()
        .placeSketch(test_hull)
        .extrude(2)
        )
show_object(result)
