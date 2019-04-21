from src.rectangle import Rectangle
from src.square import Square
from src.circle import Circle

from src.group import Group
import pickle

class Diagram:
  def __init__(self):
    self.shapes = []
    
  def add_shape(self, shape):
    self.shapes.append(shape)
    
  def delete_shape_at(self, x, y):
    shape = self.select_at(x, y)
    
    if shape:
      self.shapes.remove(shape)

  def select_at(self, x, y):
    shapes = []
    if self.shapes:
      shapes = list(filter(lambda shape: shape.is_point_on(x, y), self.shapes))

    if shapes:
      return shapes[-1]
  
  def group_shapes(self, x, y, length, width):
    group_list = []
    bool_check = False
    for shape in reversed(self.shapes):
      if shape.is_shape_in_region(x, y, length, width):
        bool_check = True
        group_list.append(shape)
        self.shapes.remove(shape)

    if bool_check:
      self.shapes.append(Group(list(reversed(group_list))))

  def ungroup(self, group):
    if isinstance(group, Group):
      if group in self.shapes:
        self.shapes.remove(group)
        for shape in group.shapes:
         self.shapes.append(shape)

  def convert_data(self):
    return pickle.dumps(self.shapes)
    
  @staticmethod
  def load_diagram(shapes_bytes):
    return pickle.loads(shapes_bytes)
