import cadquery as cq

def make_holder():
    base = cq.Workplane().rect(171,82).extrude(17)
    mid = cq.Workplane().rect(171-30,82).extrude(92)
    cylinder = base.faces('>Y').edges('<Z').workplane().center(0,60).tag('center').circle(60).extrude(-82)
    base = base.union(mid).union(cylinder)
    base = base.workplaneFromTagged('center').circle(50).cutThruAll()

    return base



holder = make_holder()
show_object(holder)
