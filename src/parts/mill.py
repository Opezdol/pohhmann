import cadquery as cq

def make_mill():
    return (
            cq.Workplane()
            .circle(50)
            .extrude(227)
            .faces('>Z').workplane()
            .circle(40)
            .extrude(25)
            .faces('>Z').workplane()
            .circle(25)
            .extrude(7)
            .faces('>Z').workplane()
            .circle(10)
            .extrude(23)
            .faces('>Z').workplane()
            .polygon(6,30)
            .extrude(23)
            .faces('>Z').workplane()
            .circle(10)
            .cutBlind(-5)
            )

mill = make_mill()
show_object(mill)
