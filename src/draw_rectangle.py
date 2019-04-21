from tkinter import *
from src.rectangle import Rectangle


class DrawRectangle():

	def __init__(self, canvas, diagram):
		self.canvas = canvas
		self.diagram = diagram
		self.create_rectangle_button()

	def create_rectangle_button(self):
		rectangle_button = Button(master = None, text="Rectangle", command = self.create_shape, height = 3, width = 7)
		rectangle_button.place(x = 0, y = 100)

	def create_shape(self):
		self.diagram.add_shape(Rectangle(140, 120, 80, 40))
		self.canvas.create_rectangle(100, 100, 180, 140, outline='black', fill='white', tags="shape")
		
	def load_shape(self, shape):
		self.canvas.create_rectangle(shape.x_coordinate - 40, shape.y_coordinate - 20, shape.x_coordinate + 40, shape.y_coordinate + 20,
														outline = 'black', fill = 'white', tags = "shape")
	
	def is_instance(self, shape): #Feedback: should not need this
		if isinstance(shape, Rectangle):
			self.load_shape(shape)
