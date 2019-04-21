from tkinter import *
from src.square import Square


class DrawSquare:
	def __init__(self, canvas, diagram):
		self.canvas = canvas
		self.diagram = diagram
		self.create_square_button()

	def create_square_button(self):
		square_button = Button(master = None, text='Square', command = self.create_shape, height = 3, width = 7)
		square_button.place(x = 0, y = 155)

	def create_shape(self):
		self.diagram.add_shape(Square(125, 125, 50))
		self.canvas.create_rectangle(100, 100, 150, 150, outline='black', fill='white', tags="shape")
		
	def load_shape(self, shape):
		self.canvas.create_rectangle(shape.x_coordinate - 25, shape.y_coordinate - 25, shape.x_coordinate + 25, shape.y_coordinate + 25,
														outline = 'black', fill = 'white', tags = "shape")
		
	def is_instance(self, shape):
		if isinstance(shape, Square):
			self.load_shape(shape)
