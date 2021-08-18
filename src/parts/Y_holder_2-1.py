import cadquery as cq

PROFILE = cq.importers.importDXF('./ref_dxfs/3mm/2-1-3mm.DXF').wires()

res = PROFILE.toPending().extrude(3)
show_object(res)
