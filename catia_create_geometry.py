from pycatia import catia
caa = catia()
document = caa.active_document
part = document.part
parameters = part.parameters
sketches = part.main_body.sketches

plane_xy = part.origin_elements.plane_xy
target_name = "MyCircleSketch"
found = False

for sketch in sketches:
    if target_name == sketch.name:
        found = True

if not found:
    new_sketch = sketches.add(plane_xy)
    new_sketch.name = target_name
    sketch_editor = new_sketch.open_edition()
    factory2d = new_sketch.factory_2d
    circle = factory2d.create_closed_circle(0, 0, 30)
    new_sketch.close_edition()
    part.update()
    part.in_work_object = new_sketch
    print("Created new sketch:", new_sketch.name)
    shape_factory = part.shape_factory
    pad = shape_factory.add_new_pad(new_sketch,50)
    part.update()