
class Group:
  def __init__(self, shapes_list):
    self.shapes = shapes_list
  
  
  def move_by(self, x, y):
    for shape in self.shapes:
      shape.move_by(x, y)
  
  def is_point_on(self, x, y):
    return any(shape.is_point_on(x, y) for shape in self.shapes)
  
  def is_shape_in_region(self, x, y, length, width):
    return all(shape.is_shape_in_region(x, y, length, width) for shape in self.shapes)

