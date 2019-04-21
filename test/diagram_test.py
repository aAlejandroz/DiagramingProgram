import unittest
from src.diagram import Diagram
from src.square import Square
from src.rectangle import Rectangle
from src.circle import Circle
from src.group import Group

class DiagramTest(unittest.TestCase):
  
  def setUp(self):
    self.diagram = Diagram()
  
  def test_for_no_shape_in_diagram(self):
    
    self.assertEqual(0, len(self.diagram.shapes))
    
  def test_add_circle_to_diagram(self):
    circle1 = Circle(0, 0, 3)
    
    self.diagram.add_shape(circle1)
    
    self.assertEqual([circle1], self.diagram.shapes)
    
  def test_add_two_circles_to_diagram(self):
    circle1 = Circle(0, 0, 3)
    circle2 = Circle(0, 10, 3)
    
    self.diagram.add_shape(circle1)
    self.diagram.add_shape(circle2)
    
    self.assertEqual(circle1, self.diagram.shapes[0])
    self.assertEqual(circle2, self.diagram.shapes[1])
  
  def test_add_circle_and_rectangle_to_diagram(self):
    circle1 = Circle(0, 0, 3)
    rectangle1 = Rectangle(0, 0, 4, 2)
    
    self.diagram.add_shape(circle1)
    self.diagram.add_shape(rectangle1)

    self.assertEqual([circle1, rectangle1], self.diagram.shapes)
  
  def test_add_circle_square_rectangle_to_diagram(self):
    circle1 = Circle(0, 0, 3)
    rectangle1 = Rectangle(0, 0, 4, 2)
    square1 = Square(0, 0, 4)
    
    self.diagram.add_shape(circle1)
    self.diagram.add_shape(rectangle1)
    self.diagram.add_shape(square1)
    
    self.assertEqual([circle1, rectangle1, square1], self.diagram.shapes)
    
  def test_diagram_with_no_shapes_ignores_delete_shape_at_method(self):
    
    self.assertFalse(self.diagram.delete_shape_at(4, 3))
  
  def test_diagram_with_two_circles_deletes_nothing_if_point_isnt_inside_circle(self):
    circle1 = Circle(0, 0, 3)
    circle2 = Circle(0, 0, 3)
    
    self.diagram.add_shape(circle1)
    self.diagram.add_shape(circle2)
    
    self.diagram.delete_shape_at(10, 10)
    
    self.assertEqual([circle1, circle2], self.diagram.shapes)
  
  def test_diagram_with_two_overlapping_circles_deletes_only_first(self):
    circle1 = Circle(0, 0, 3)
    circle2 = Circle(0, 10, 3)
    
    self.diagram.add_shape(circle1)
    self.diagram.add_shape(circle2)
    
    self.diagram.delete_shape_at(0, 0)
    
    self.assertEqual([circle2], self.diagram.shapes)
  
  def test_diagram_with_two_circles_at_different_locations_deletes_second_circle(self):
    circle1 = Circle(0, 0, 3)
    circle2 = Circle(10, 10, 3)
    
    self.diagram.add_shape(circle1)
    self.diagram.add_shape(circle2)
    
    self.diagram.delete_shape_at(9, 9)
    self.assertEqual([circle1], self.diagram.shapes)
  
  def test_diagram_has_circle_on_top_of_rectangle_delete_circle_check_for_a_property_of_rectangle_being_there(self):
    rectangle1 = Rectangle(0, 0, 8, 4)
    circle1 = Circle(0, 0, 3)

    self.diagram.add_shape(rectangle1)
    self.diagram.add_shape(circle1)

    self.diagram.delete_shape_at(0, 0)
    self.assertEqual([rectangle1], self.diagram.shapes)
  
  def test_diagram_has_circle_on_top_of_rectangle_delete_rectangle_check_for_a_property_of_circle_being_there(self):
    rectangle1 = Rectangle(0, 0, 8, 4)
    circle1 = Circle(0, 0, 3)
    
    self.diagram.add_shape(rectangle1)
    self.diagram.add_shape(circle1)
    
    self.diagram.delete_shape_at(-3, 1)
    
    self.assertEqual([circle1], self.diagram.shapes)
  
  def test_SELECT_AT_returns_nothing_when_diagram_has_no_shapes(self):

    self.assertFalse(self.diagram.select_at(0, 0))
  
  def test_diagram_with_two_circles_returns_nothing_when_location_of_selection_isnt_in_either_circle(self):
    circle1 = Circle(0, 0, 3)
    circle2 = Circle(0, 0, 3)
    
    self.diagram.add_shape(circle1)
    self.diagram.add_shape(circle2)

    self.assertEqual(None, self.diagram.select_at(10, 0))
  
  def test_diagram_with_two_circles_at_same_location_returns_first_circle(self):
    circle1 = Circle(0, 0, 3)
    circle2 = Circle(0, 0, 3)
    
    self.diagram.add_shape(circle1)
    self.diagram.add_shape(circle2)

    self.assertEqual(circle2, self.diagram.select_at(0, 0))
  
  def test_diagram_with_two_circles_at_different_location_returns_second_circle_at_selected_location(self):
    circle1 = Circle(10, 10, 3)
    circle2 = Circle(0, 0, 3)
    
    self.diagram.add_shape(circle1)
    self.diagram.add_shape(circle2)

    self.assertEqual(circle1, self.diagram.select_at(7, 10))
    
  def test_diagram_has_circle_on_top_of_rectangle_selects_circle_when_point_is_on_circle(self):
    rectangle1 = Rectangle(0, 0, 8, 4)
    circle1 = Circle(0, 0, 3)
    
    self.diagram.add_shape(rectangle1)
    self.diagram.add_shape(circle1)
    
    self.assertEqual(circle1, self.diagram.select_at(0, 0))
  
  def test_diagram_has_circle_on_top_of_rectangle_selects_rectangle_when_point_is_on_rectangle(self):
    rectangle1 = Rectangle(0, 0, 8, 4)
    circle1 = Circle(0, 0, 3)
    
    self.diagram.add_shape(rectangle1)
    self.diagram.add_shape(circle1)
    
    self.assertEqual(rectangle1, self.diagram.select_at(4, 2))
    
  def test_draw_a_rectangle_area_any_shape_within_it_will_be_grouped(self):
    rectangle1 = Rectangle(-1, 7, 8, 4)
    circle1 = Circle(0, 0, 3)
    square1 = Square(-5, 0, 8)

    self.diagram.add_shape(rectangle1)
    self.diagram.add_shape(circle1)
    self.diagram.add_shape(square1)
    
    self.diagram.group_shapes(0, 0, 25, 25)
  
    self.assertEqual([rectangle1, circle1, square1], self.diagram.shapes[0].shapes)
   
  def test_diagram_has_only_a_group_no_ungrouped_shapes(self):
    rectangle1 = Rectangle(-1, 7, 8, 4)
    circle1 = Circle(3, 6, 3)
    square1 = Square(-5, 0, 8)
    
    self.diagram.add_shape(rectangle1)
    self.diagram.add_shape(circle1)
    self.diagram.add_shape(square1)
    
    self.diagram.group_shapes(0, 0, 21, 20)
    
    self.assertEqual([rectangle1, circle1, square1], self.diagram.shapes[0].shapes)
    self.assertEqual(1, len(self.diagram.shapes))
  
  def test_diagram_has_a_group_and_two_ungrouped_shapes(self):
    rectangle1 = Rectangle(-1, 7, 8, 4)
    circle1 = Circle(3, 6, 3)
    square1 = Square(-5, 0, 8)

    circle2 = Circle(9, 6, 3)
    square2 = Square(8, 0, 8)

    self.diagram.add_shape(rectangle1)
    self.diagram.add_shape(circle1)
    self.diagram.add_shape(square1)

    self.diagram.add_shape(circle2)
    self.diagram.add_shape(square2)
    
    self.diagram.group_shapes(0, 0, 21, 20)
    
    self.assertEqual([rectangle1, circle1, square1], self.diagram.shapes[2].shapes)
    self.assertEqual([circle2, square2], self.diagram.shapes[0:2])

  def test_ungroup_a_group(self):
    rectangle1 = Rectangle(-1, 7, 8, 4)
    circle1 = Circle(20, 2, 3)
    square1 = Square(-5, 0, 8)

    self.diagram.add_shape(rectangle1)
    self.diagram.add_shape(circle1)
    self.diagram.add_shape(square1)

    self.diagram.group_shapes(0, 0, 21, 20)
    
    self.diagram.ungroup(self.diagram.shapes[1])

    self.assertEqual([circle1, rectangle1, square1], self.diagram.shapes)

  def test_delete_group_and_all_its_shapes(self):
    rectangle1 = Rectangle(-1, 7, 8, 4)
    circle1 = Circle(1, 3, 3)
    square1 = Square(-5, 0, 8)

    self.diagram.add_shape(rectangle1)
    self.diagram.add_shape(circle1)
    self.diagram.add_shape(square1)

    self.diagram.group_shapes(0, 0, 21, 20)

    self.diagram.delete_shape_at(3, 6)

    self.assertEqual([], self.diagram.shapes)

  def test_delete_group_and_its_shapes(self):
    rectangle1 = Rectangle(-1, 7, 8, 4)
    circle1 = Circle(20, 6, 3)
    square1 = Square(-5, 0, 8)

    self.diagram.add_shape(rectangle1)
    self.diagram.add_shape(circle1)
    self.diagram.add_shape(square1)

    self.diagram.group_shapes(0, 0, 21, 20)
    
    self.diagram.delete_shape_at(3, 6)
    
    self.assertEqual([circle1], self.diagram.shapes)
    
  def test_group_a_group_and_a_circle(self):
    rectangle1 = Rectangle(-2, -1, 4, 1)
    rectangle2 = Rectangle(-1, 2, 4, 2)
    
    square1 = Square(7, 3, 2)
    square2 = Square(10, 3, 2)
    
    circle1 = Circle(2, 6, 3)

    self.diagram.add_shape(rectangle1)
    self.diagram.add_shape(rectangle2)
    
    self.diagram.add_shape(square1)
    self.diagram.add_shape(square2)
    
    self.diagram.add_shape(circle1)
    
    self.diagram.group_shapes(-1, 1, 8, 6)
    
    self.diagram.group_shapes(9, 3, 8, 4)
    
    self.diagram.group_shapes(3, 6, 20, 20)
    
    self.assertEqual(circle1, self.diagram.shapes[0].shapes[0])
    self.assertEqual([rectangle1, rectangle2], self.diagram.shapes[0].shapes[1].shapes)
    self.assertEqual([square1, square2], self.diagram.shapes[0].shapes[2].shapes)
    
  def test_save_diagram_with_nothing_in_it(self):
    
    self.assertEqual(bytes, type(self.diagram.convert_data()))
    
  def test_save_diagram_with_one_circle(self):
    self.diagram.add_shape(Circle(0, 0, 3))
    
    self.assertEqual(bytes, type(self.diagram.convert_data()))
    
  def test_save_diagram_with_one_circle_and_one_rectangle(self):
    self.diagram.add_shape(Circle(0, 0, 3))
    self.diagram.add_shape(Rectangle(0, 0, 4, 2))
    
    self.assertEqual(bytes, type(self.diagram.convert_data()))
    
  def test_load_diagram_with_nothing_in_it(self):
    self.diagram.load_diagram(self.diagram.convert_data())
    
    self.assertEqual(0, len(self.diagram.shapes))
  
  def test_load_diagram_with_one_circle(self):
    circle1 = Circle(0, 3, 3)
    self.diagram.add_shape(circle1)
    data_bytes = self.diagram.convert_data()
    
    self.diagram.shapes = []
    
    self.diagram.shapes = self.diagram.load_diagram(data_bytes)
    
    self.assertEqual(1, len(self.diagram.shapes))
    
  def test_load_diagram_with_one_circle_and_one_rectangle(self):
    circle1 = Circle(0, 3, 3)
    rectangle1 = Rectangle(0, 0, 4, 2)
    self.diagram.add_shape(circle1)
    self.diagram.add_shape(rectangle1)
    data_bytes = self.diagram.convert_data()
    
    self.diagram.shapes = []
    
    self.diagram.shapes = self.diagram.load_diagram(data_bytes)
    
    self.assertEqual(2, len(self.diagram.shapes))
    
  def test_ungroup_a_nonexistent_group_from_a_diagram(self):
    group = Group([Circle(10, 10, 5), Circle(20, 20, 5)])
    self.diagram.ungroup(group)
    
    self.assertEqual(0, len(self.diagram.shapes))
    
  def test_ungroup_a_nonexistent_group_from_a_di(self):
    circle1 = Circle(0, 3, 3)
    rectangle1 = Rectangle(0, 0, 4, 2)
    self.diagram.add_shape(circle1)
    self.diagram.add_shape(rectangle1)
    
    self.diagram.group_shapes(100,100, 4, 2)
    
    self.assertEqual(2, len(self.diagram.shapes))


  def test_ungroup_something_thats_not_a_group(self):
    circle1 = Circle(0, 0, 2)
    self.diagram.ungroup(circle1)

    self.assertEqual(0, len(self.diagram.shapes))
    
if __name__ == '__main__':
  unittest.main()
