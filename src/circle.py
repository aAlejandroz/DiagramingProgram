class Circle:
  def __init__(self, x, y, radius):
    self.center = (x, y)
    self.radius = radius
  
  def set_location(self, x, y):
    self.center = (x, y)
    
  def move_by(self, x, y):
    self.set_location(self.center[0] + x, self.center[1] + y)
  
  def is_point_on(self, x, y):
    return (x - self.center[0])**2 + (y - self.center[1])**2 <= self.radius**2
  
  def is_shape_in_region(self, x, y, length, width):
    return (self.center[0] + self.radius < x + length / 2) \
           and (self.center[0] - self.radius > x - length / 2) \
           and (self.center[1] + self.radius < y + width / 2) \
           and (self.center[1] - self.radius > y - width / 2)

  def get_location(self):
    return self.center[0], self.center[1]
