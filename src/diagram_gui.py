from tkinter import *
from tkinter import messagebox
from random import randint
from src.diagram import Diagram, pickle
from src.draw_circle import DrawCircle
from src.draw_rectangle import DrawRectangle
from src.draw_square import DrawSquare


class DiagramGUI(Frame):
  
  def __init__(self, master = None):
    self.master = master
    Frame.__init__(self, self.master)
    
    self.delete_pressed = False
    self.group_pressed = False
    self.ungroup_pressed = False
    self.group_list = ['1']

    self.rect = None
    self.start_x = self.start_y = 0
    
    self.diagram = Diagram()
    self.glob_in = 0
    
    self.canvas = Canvas(width = 1050, height = 578, bg = 'gray67', borderwidth = 5, relief = RAISED)
    self.canvas.pack(side = RIGHT)
    self._drag_data = {"x" : 0, "y" : 0, "item" : None}
    
    self.click_drag_shapes()
    self.create_save_load_buttons()
    self.create_delete_button()
    self.create_group_ungroup_buttons()
    self.draw_shapes = [DrawCircle(self.canvas, self.diagram), DrawRectangle(self.canvas, self.diagram), DrawSquare(self.canvas, self.diagram)]
  
  def click_drag_shapes(self):
    self.canvas.tag_bind("shape", "<ButtonPress-1>", self.shape_press)
    self.canvas.tag_bind("shape", "<B1-Motion>", self.shape_movement)
    self.canvas.tag_bind("shape", "<ButtonRelease-1>", self.shape_release)
    
  def shape_press(self, event):
    if self.delete_pressed:
      self.canvas.delete(self.canvas.find_closest(event.x, event.y)[0])
      self.diagram.delete_shape_at(event.x, event.y)
      self.activate_delete()
    elif self.ungroup_pressed:
      self.glob_in = 0
      if len(self.canvas.gettags(self.canvas.find_closest(event.x, event.y)[0])) >= 2 :
        group = self.diagram.select_at(event.x, event.y)
        self.diagram.ungroup(group)
        self.ungroup_drawings(self.canvas.gettags(self.canvas.find_closest(event.x, event.y)[0]))
        self.ungroup_shapes()
      else:
        self.ungroup_shapes()
    else:
      shape = self.diagram.select_at(event.x, event.y)
      self.glob_in = self.diagram.shapes.index(shape)
      self._drag_data["item"] = self.canvas.find_closest(event.x, event.y)[0]
      self._drag_data["x"] = self.diagram.shapes[self.glob_in].get_location()[0]
      self._drag_data["y"] = self.diagram.shapes[self.glob_in].get_location()[1]
  
  def shape_movement(self, event):
    delta_x = event.x - self._drag_data["x"]
    delta_y = event.y - self._drag_data["y"]
    self.canvas.move(self._drag_data["item"], delta_x, delta_y)
    
    self._drag_data["x"] = event.x
    self._drag_data["y"] = event.y
  
  def shape_release(self, event):
    self.diagram.shapes[self.glob_in].set_location(event.x, event.y)
    self._drag_data['item'] = None
    self._drag_data['x'] = 0
    self._drag_data['y'] = 0
  



  def group_items(self, starting, ending):
    rect_measurements = self.calculate_rectangle(starting, ending)
    self.diagram.group_shapes(rect_measurements[0][0], rect_measurements[0][1], rect_measurements[1], rect_measurements[2])
    self.get_enclosed_items(rect_measurements)
    

  def get_enclosed_items(self, measu):
    all_items = self.canvas.find_withtag('shape')
    for shape in all_items:
      if (self.canvas.coords(shape)[0] > measu[0][0] - (measu[1] / 2)) \
        and (self.canvas.coords(shape)[1] > measu[0][1] - (measu[2] / 2)) \
        and (self.canvas.coords(shape)[2] < measu[0][0] + (measu[1] / 2)) \
        and (self.canvas.coords(shape)[3] < measu[0][1] + (measu[2] / 2) ):
        self.canvas.itemconfig(shape, fill = 'green', tag=('shape', 'Group'))
    self.increment_group_id()
    
  def ungroup_drawings(self, tags):
    grouped_drw = self.canvas.find_withtag('Group')
    for shape in grouped_drw:
      self.canvas.itemconfig(shape, tag='shape', fill= 'white')
    
  def activate_delete(self):
    self.delete_pressed = not self.delete_pressed
    if self.delete_pressed:
      self.delete_button.config(bg = 'red', text = "click object")
    else:
      self.delete_button.config(bg = self.defaultbg, text = "Delete")

  def ungroup_shapes(self):
    self.ungroup_pressed = not self.ungroup_pressed
    if self.ungroup_pressed:
      self.ungroup_button.config(bg = 'red', text = "click group")
      self.canvas.config(cursor='tcross')
    else:
      self.ungroup_button.config(bg = self.defaultbg, text = "Ungroup")
      self.click_drag_shapes()
      self.canvas.config(cursor='arrow')
  
  def create_save_load_buttons(self):
    self.save_button = Button(master = None, text = "Save", command = self.save_diagram)
    self.save_button.place(x = 0, y = 0)
    
    self.load_button = Button(master = None, text = 'Load', command = self.load_diagram)
    self.load_button.place(x = 35, y = 0)
 
  def create_delete_button(self):
    self.delete_button = Button(master = None, text = "Delete", command = self.activate_delete, width=7)
    self.defaultbg = self.delete_button['bg']
    self.delete_button.place(x = 73, y = 0)
    
  def create_group_ungroup_buttons(self):
    self.group_button = Button(master = None, text = 'Group', command = self.activate_group, width=7)
    self.group_button.place(x = 73, y = 25)
    
    self.ungroup_button = Button(master = None, text = 'Ungroup', command = self.ungroup_shapes, width=7)
    self.ungroup_button.place(x = 73, y = 50)
 
  def activate_group(self):
    self.group_pressed = not self.group_pressed
    if self.group_pressed:
      self.group_button.config(bg = 'blue', text = "Group shapes")
      self.canvas.config(cursor='cross')
      self.canvas.bind("<ButtonPress-1>", self.on_button_press)
      self.canvas.bind("<B1-Motion>", self.on_move_press)
      self.canvas.bind("<ButtonRelease-1>", self.on_button_release)
    else:
      self.group_button.config(bg = self.defaultbg, text = "Group")
      self.canvas.config(cursor='arrow')
      self.click_drag_shapes()

  def on_button_press(self, event):
    if self.group_pressed:
      self.start_x = event.x
      self.start_y = event.y
      self.rect = self.canvas.create_rectangle(self.start_x, self.start_y, 1, 1)

  def on_move_press(self, event):
    if self.group_pressed:
      curX, curY = (event.x, event.y)
      self.canvas.coords(self.rect, self.start_x, self.start_y, curX, curY)
  
  def on_button_release(self, event):
    if self.group_pressed:
      self.group_items((self.start_x, self.start_y), event)
      self.canvas.delete(self.rect)
      self.start_x = None
      self.start_y = None
      self.rect = None
      self.activate_group()
  
  def calculate_rectangle(self, starting, ending):
    leng = abs(starting[0] - ending.x)
    wid = abs(starting[1] - ending.y)
    center = ((starting[0] + ending.x)/2 ,(starting[1] + ending.y)/2)
    return [center, leng, wid]
 
  def save_diagram(self):
    pickle_out = open('save_diagram', 'wb')
    pickle.dump(self.diagram.shapes, pickle_out)
    pickle_out.close()
    messagebox.showinfo("Save", "Diagram Saved!")
  
  def load_diagram(self):
    self.canvas.delete(ALL)
    self.load_button.config(state = 'disabled')
    pickle_in = open('save_diagram', 'rb')
    self.diagram.shapes = pickle.load(pickle_in)
    self.load_canvas()
  
  def load_canvas(self):
    for shape in self.diagram.shapes:
      any(drawing.is_instance(shape) for drawing in self.draw_shapes)
    
  def increment_group_id(self):
    ran = randint(0,1000)
    group_id = str(ran)
    self.group_list.insert(0,group_id)

class Main(DiagramGUI):
  def __init__(self):
    master = Tk()
    
    master.title("Draw.io 2")
    master.geometry("1200x500")
    master.resizable(width = True, height = True)
    
    app = DiagramGUI(master)
    app.mainloop()


