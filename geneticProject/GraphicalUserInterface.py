import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import copy

root = tk.Tk()


def create_game_plate_arr(game_plate_str):
    first_row, second_row = "", ""
    for char in game_plate_str:
        if char == "_":
            first_row += "_"
            second_row += "_"
        elif char == "G":
            first_row += "_"
            second_row += "G"
        elif char == "L":
            first_row += "L"
            second_row += "_"
        elif char == "M":
            first_row += "_"
            second_row += "M"
    first_row_split = [char for char in first_row]
    second_row_split = [char for char in second_row]
    game_plate_arr = [first_row_split, second_row_split]
    return game_plate_arr


test = create_game_plate_arr("__GMG__L")
print(test)


def get_first_state(game_plate_arr):
    game_plate_arr_copy = copy.deepcopy(game_plate_arr)
    game_plate_arr_copy[1][0] = "SM"  # super mario
    return game_plate_arr_copy


print(get_first_state(test))


def get_sequence_movement(win_path, game_plate_arr):
    sequence_movement_arr = []
    super_mario_index = 0

    first_state = get_first_state(win_path, game_plate_arr)
    sequence_movement_arr.append(first_state)

    for i in len(win_path):



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
