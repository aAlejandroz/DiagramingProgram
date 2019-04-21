import unittest
from src.rectangle import Rectangle

class RectangleTest(unittest.TestCase):

  def setUp(self):
    self.rectangle = Rectangle(0, 0, 8, 4)

  def test_create_rectangle(self):

    self.assertEqual(self.rectangle.width, 4)
    
  def test_get_location(self):
    self.rectangle.set_location(3, 3)
    
    self.assertEqual((3, 3), self.rectangle.get_location())

  def test_move_rectangle(self):
    self.rectangle.set_location(2, 2)

    self.assertEqual((2, 2), (self.rectangle.x_coordinate, self.rectangle.y_coordinate))

  def test_point_outside_square(self):

    self.assertFalse(self.rectangle.is_point_on(6, 6))

  def test_point_inside_square(self):

    self.assertTrue(self.rectangle.is_point_on(0, 0))

  def test_point_on_left_edge_square(self):

    self.assertTrue(self.rectangle.is_point_on(-2, 0))

  def test_point_on_top_edge_square(self):

    self.assertTrue(self.rectangle.is_point_on(0, 1))

  def test_point_on_right_edge_square(self):

    self.assertTrue(self.rectangle.is_point_on(2, 0))

  def test_point_on_bottom_edge_square(self):

    self.assertTrue(self.rectangle.is_point_on(0, -1))

  def test_if_rectangle_in_selection_region(self):

    self.assertTrue(self.rectangle.is_shape_in_region(0, 0, 10, 10))
    
  def test_move_by(self):
    
    self.rectangle.set_location(5, 5)
    self.rectangle.move_by(5, -5)
    
    self.assertEqual([10, 0], [self.rectangle.x_coordinate, self.rectangle.y_coordinate])

if __name__ == '__main__':
  unittest.main()
