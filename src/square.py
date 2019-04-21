class Square:
  def __init__(self, x, y, side):
    self.x_coordinate = x
    self.y_coordinate = y
    self.side = side
  
  def set_location(self, x, y):
    self.x_coordinate = x
    self.y_coordinate = y
    
  def move_by(self, x, y):
    self.set_location(self.x_coordinate + x, self.y_coordinate + y)

  def is_point_on(self, x, y):
    return ((self.x_coordinate - self.side / 2) <= x <= (self.x_coordinate + self.side / 2)) \
           and ((self.y_coordinate - self.side / 2) <= y <= (self.y_coordinate + self.side / 2))

  def is_shape_in_region(self, x, y, length, width):
    return (self.x_coordinate + (self.side / 2) < x + (length / 2) ) \
           and (self.x_coordinate - (self.side / 2) > x - (length / 2)) \
           and (self.y_coordinate + (self.side / 2) < y + (width / 2)) \
           and (self.y_coordinate - (self.side / 2) > y - (width /2))

  def get_location(self): #Feedback: no need for this one
    return self.x_coordinate, self.y_coordinate
