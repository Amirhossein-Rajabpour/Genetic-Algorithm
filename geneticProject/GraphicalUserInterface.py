import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

root = tk.Tk()


class GraphicalUserInterface():

    def __init__(self, path_string, game_plate):
        self.path_string = path_string
        self.step = 0
        self.game_plate = game_plate
        self.Visualize()


    def print_10_next_state(self, index):
        pass

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

        super_mario_image = ImageTk.PhotoImage(
            Image.open('./picture_for_gui/superMario.jpg').resize((100, 100), Image.ANTIALIAS))
        mushroom_image = ImageTk.PhotoImage(
            Image.open('./picture_for_gui/mushrooms.jpg').resize((100, 100), Image.ANTIALIAS))
        ghost_image = ImageTk.PhotoImage(Image.open('./picture_for_gui/ghost.jpg').resize((100, 100), Image.ANTIALIAS))
        gumpa_image = ImageTk.PhotoImage(Image.open('./picture_for_gui/gumpa.jpg').resize((100, 100), Image.ANTIALIAS))
        cell_image = ImageTk.PhotoImage(Image.open('./picture_for_gui/cell.png').resize((100, 100), Image.ANTIALIAS))

        super_mario_label = ttk.Label(root, image=super_mario_image)
        super_mario_label.grid(column=0, row=1)

        # for i in range(len(self.game_plate)):
        #     print(self.game_plate[i])
        #
        #
        #
        #
        #     if self.game_plate[i] == "_":
        #         cell_label1 = ttk.Label(root, image=cell_image)
        #         cell_label2 = ttk.Label(root, image=cell_image)
        #         cell_label1.grid(column=i, row=0)
        #         cell_label2.grid(column=i, row=1)
        #
        #     if self.game_plate[i] == "M":
        #         cell_label = ttk.Label(root, image=cell_image)
        #         mushroom_label = ttk.Label(root, image=mushroom_image)
        #         cell_label.grid(column=i, row=0)
        #         mushroom_label.grid(column=i, row=1)
        #
        #     if self.game_plate[i] == "G":
        #         gumpa_label = ttk.Label(root, image=gumpa_image)
        #         cell_label = ttk.Label(root, image=cell_image)
        #         cell_label.grid(column=i, row=0)
        #         gumpa_label.grid(column=i, row=1)
        #
        #     if self.game_plate[i] == "L":
        #         ghost_label = ttk.Label(root, image=ghost_image)
        #         cell_label = ttk.Label(root, image=cell_image)
        #         ghost_label.grid(column=i, row=0)
        #         cell_label.grid(column=i, row=1)

        root.mainloop()


g = GraphicalUserInterface("001100", "_G_ML_")
