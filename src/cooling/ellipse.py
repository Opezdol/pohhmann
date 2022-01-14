import cadquery as cq
x = 100
y = 80
ell = (
        cq.Workplane()
        .ellipse(x,y)
        .twistExtrude(50,360)
        )

if 'show_object' in locals():
    show_object(ell)
