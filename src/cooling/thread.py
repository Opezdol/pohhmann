import cadquery as cq

from cq_warehouse.thread import MetricTrapezoidalThread, IsoThread

MM = 1
""" MetricTrapezoidalThread example
metric_thread = MetricTrapezoidalThread(size="8x1.5", length=20 * MM)
metric_core = (
    cq.Workplane("XY").circle(metric_thread.root_radius).extrude(metric_thread.length)
)
metric = metric_thread.cq_object.fuse(metric_core.val())
print(f"{metric.isValid()=}")

show_object(metric)
"""

""" IsoThread Internal Example """
iso_internal_thread = IsoThread(
    major_diameter=6 * MM,
    pitch=1 * MM,
    length=4.35 * MM,
    external=False,
    end_finishes=("square", "chamfer"),
    hand="left",
)

iso_internal_core = (
    cq.Workplane("XY")
    .polygon(6, iso_internal_thread.major_diameter * 1.5)
    .circle(iso_internal_thread.major_diameter / 2)
    .extrude(iso_internal_thread.length)
)
iso_internal = iso_internal_thread.cq_object.fuse(iso_internal_core.val())

#show_object(iso_internal_thread, name='thread')
show_object(iso_internal_core, name = 'core')
show_object(iso_internal,name='thread')
