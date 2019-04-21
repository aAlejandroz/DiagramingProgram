import unittest
from src.diagram import *

class GroupTest(unittest.TestCase):
  
  def test_move_group_make_sure_shapes_in_group_move_too(self):
    circle1 = Circle(0, 5, 3)
    rectangle1 = Rectangle(0, -5, 8, 2)
    square1 = Square(0, 0, 4)
    
    shapes = [circle1, rectangle1, square1]
    
    self.group = Group(shapes)
    
    self.group.move_by(2, -2)
    
    self.assertEqual((2, 3), self.group.shapes[0].center)
    self.assertEqual([2, -7], [self.group.shapes[1].x_coordinate, self.group.shapes[1].y_coordinate])
    self.assertEqual([2, -2], [self.group.shapes[2].x_coordinate, self.group.shapes[2].y_coordinate])

  def test_if_point_is_in_group(self):
    circle1 = Circle(5, 5, 3)
    rectangle1 = Rectangle(4, 4, 8, 2)
    square1 = Square(6, 6, 4)

    shapes = [circle1, rectangle1, square1]

    self.group = Group(shapes)

    self.assertTrue(self.group.is_point_on(5, 5))
    
  def test_is_point_not_in_group(self):
    circle1 = Circle(5, 5, 3)
    rectangle1 = Rectangle(4, 4, 8, 2)
    square1 = Square(6, 6, 4)

    shapes = [circle1, rectangle1, square1]

    self.group = Group(shapes)

    self.assertFalse(self.group.is_point_on(70, 7))




if __name__ == '__main__':
  unittest.main()

