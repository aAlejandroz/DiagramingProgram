import unittest
from src.square import Square

class SquareTest(unittest.TestCase):
  
  def setUp(self):
    self.square = Square(0, 0, 4)
  
  def test_create_square(self):
    
    self.assertEqual(self.square.side, 4)

  def test_move_square(self):
    self.square.set_location(3, 3)
    
    self.assertEqual((3, 3), (self.square.x_coordinate, self.square.y_coordinate))
    
  def test_get_location(self):
    self.square.set_location(3, 3)
    
    self.assertEqual((3, 3), self.square.get_location())
    
  def test_point_outside_square(self):

    self.assertFalse(self.square.is_point_on(6, 6))

  def test_point_inside_square(self):
    
    self.assertTrue(self.square.is_point_on(0, 0))
    
  def test_point_on_left_edge_square(self):

    self.assertTrue(self.square.is_point_on(-2, 0))
  
  def test_point_on_top_edge_square(self):
    
    self.assertTrue(self.square.is_point_on(0, 2))
  
  def test_point_on_right_edge_square(self):

    self.assertTrue(self.square.is_point_on(2, 0))

  def test_point_on_bottom_edge_square(self):
    
    self.assertTrue(self.square.is_point_on(0, -2))

  def test_if_square_in_selection_region(self):

    self.square.set_location(0, 0)

    self.assertTrue(self.square.is_shape_in_region(0, 0, 5, 5))
    
  def test_move_by(self):
    self.square.move_by(5, -5)
    
    self.assertEqual([5, -5], [self.square.x_coordinate, self.square.y_coordinate])
    

if __name__ == '__main__':
  unittest.main()
