from tkinter import *

from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import numpy as np
import time
class GUI:
	def __init__(self, master=None):
		self.master = master
		self.master.wm_title("ECG")
		self.main_frame = Frame(self.master)
		self.main_frame.pack()
		plot_fig = Figure(figsize=(5, 4), dpi=100)
		self.axis = plot_fig.add_subplot(111) 
		self.canvas = FigureCanvasTkAgg(plot_fig, master=self.master)
		self.canvas.draw()
		self.canvas.get_tk_widget().pack(side= TOP, fill= BOTH, expand=True)
		quit_btn = Button(master=root, text="Quit", command=self._quit)
		quit_btn.pack(side = BOTTOM)
		self.refresh()

	def plot_signal(self, x, y):
		self.axis.clear()
		self.axis.plot(x, y)
		self.canvas.draw()
		self.refresh()

	def refresh(self):
		self.master.update_idletasks()
		self.master.update()	

	def _quit(self):
		self.master.quit()		# stops mainloop
		self.master.destroy()	# this is necessary on Windows to prevent
								# Fatal Python Error: PyEval_RestoreThread: NULL tstate


root = Tk()
gui = GUI(root)
#Example to plot a signal and update GUI to show the plot
t_start = 0
t_end = 3
while(True):
	t = np.arange(t_start, t_end, .01)
	base_sin = 20 * np.sin(2 * np.pi *10* t)
	random_noise = np.random.randn()* np.sin(2 * np.pi *np.random.randn()* t)
	gui.plot_signal(t, np.add(base_sin, random_noise) )
	t_start = t_end + 0.1
	t_end = t_start + 3
