from tkinter import *
from src.circle import Circle


class DrawCircle:
	
	def __init__(self, canvas, diagram):
		self.canvas = canvas
		self.diagram = diagram
		self.create_circle_button()

	def create_circle_button(self):
		circle_button = Button(master = None, text="Circle", command = self.create_shape, height = 3, width = 7)
		circle_button.place(x = 0, y = 45)

	def create_shape(self):
		circle = Circle(100, 100, 25)
		self.diagram.add_shape(circle)
		self.canvas.create_oval(circle.center[0] - 25, circle.center[1] - 25, circle.center[0] + 25, circle.center[1] + 25,
														outline = 'black', fill = 'white', tags = "shape")


	def load_shape(self, shape):
		self.canvas.create_oval(shape.center[0] - 25, shape.center[1] - 25, shape.center[0] + 25, shape.center[1] + 25,
														outline = 'black', fill = 'white', tags = "shape")
	
	def is_instance(self, shape):
		if isinstance(shape, Circle):
			self.load_shape(shape)
