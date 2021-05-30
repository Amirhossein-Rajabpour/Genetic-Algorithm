import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

root = tk.Tk()


class GraphicalUserInterface():

    def __init__(self, path_string):
        self.path_string = path_string
        self.step = 0
        self.Visualize()

    def Visualize(self, e=1):
        num_rows = 2
        num_cols = len(self.path_string)

        WIDTH = (num_cols * 100) + 10
        HEIGHT = (num_rows * 100) + 10
        root.geometry(f"{WIDTH}x{HEIGHT}")
        root.title("goal chromosome!")
        root.config(bg="white")

        root.columnconfigure(0, weight=num_cols)
        root.columnconfigure(1, weight=num_rows)

