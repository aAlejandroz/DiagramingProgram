import unittest
from src.circle import Circle

class CircleTest(unittest.TestCase):

  def setUp(self):
    self.circle = Circle(0, 0, 5)

  def test_canary_test(self):
    self.assertTrue(True)

  def test_create_circle(self):
    
    self.assertEqual(self.circle.radius, 5)

  def test_center_of_circle(self):
    
    self.assertEqual((0, 0), self.circle.center)
    
  def test_move_circle(self):
    self.circle.set_location(3, 3)
    
    self.assertEqual((3, 3), self.circle.center)

  def test_point_outside_circle(self):

    self.assertFalse(self.circle.is_point_on(6, 6))

  def test_point_outside_top_of_circle(self):

    self.assertFalse(self.circle.is_point_on(0, 6))

  def test_point_outside_right_of_circle(self):

    self.assertFalse(self.circle.is_point_on(6, 0))

  def test_point_outside_left_of_circle(self):

    self.assertFalse(self.circle.is_point_on(-6, 0))

  def test_point_outside_bottom_of_circle(self):

    self.assertFalse(self.circle.is_point_on(0, -6))
  
  def test_get_location(self):
    self.circle.set_location(3, 3)
    
    self.assertEqual((3, 3), self.circle.get_location())

  def test_point_inside_circle(self):

    self.assertTrue(self.circle.is_point_on(-3, 0))

  def test_point_on_circle(self):

    self.assertTrue(self.circle.is_point_on(4, 3))

  def test_move_circle_and_check_if_point_inside_circle(self):
    
    self.circle.set_location(5, 5)

    self.assertTrue(self.circle.is_point_on(6, 5))

  def test_check_if_circle_in_selection_region(self):

    self.circle.set_location(1, 1)

    self.assertTrue(self.circle.is_shape_in_region(0, 0, 15, 15))
  
  def test_move_by(self):
    self.circle.set_location(6, 9)
    self.circle.move_by(0, -3)
    
    self.assertEqual((6, 6), (self.circle.center[0], self.circle.center[1]))
   
if __name__ == '__main__':
  unittest.main()
