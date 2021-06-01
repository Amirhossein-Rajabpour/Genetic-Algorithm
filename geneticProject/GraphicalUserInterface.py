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


# test = create_game_plate_arr("__G__")


def get_first_state(game_plate_arr):
    game_plate_arr_copy = copy.deepcopy(game_plate_arr)
    game_plate_arr_copy[1][0] = "SM"  # super mario
    return game_plate_arr_copy


def get_super_mario_index(arr, string):
    row_number = len(arr)
    column_number = len(arr[0])
    for i in range(row_number):
        if string in arr[i]:
            index_j = arr[i].index(string)
            return i, index_j


def get_sequence_movement(win_path, game_plate_arr):
    sequence_movement_arr = []
    super_mario_index = 0

    first_state = get_first_state(game_plate_arr)
    sequence_movement_arr.append(first_state)

    i = 0
    while i < len(win_path):
        if win_path[i] == "0":
            current_super_mario_index = get_super_mario_index(sequence_movement_arr[-1], "SM")
            next_state = copy.deepcopy(sequence_movement_arr[-1])
            next_state[current_super_mario_index[0]][current_super_mario_index[1]] = "_"
            next_state[1][current_super_mario_index[1] + 1] = "SM"
            sequence_movement_arr.append(next_state)
            i += 1

        elif win_path[i] == "1":
            current_super_mario_index = get_super_mario_index(sequence_movement_arr[-1], "SM")
            next_state = copy.deepcopy(sequence_movement_arr[-1])
            next_state[current_super_mario_index[0]][current_super_mario_index[1]] = "_"
            next_state[0][current_super_mario_index[1] + 1] = "SM"
            sequence_movement_arr.append(next_state)
            two_next_state = copy.deepcopy(sequence_movement_arr[-1])
            two_next_state[0][current_super_mario_index[1] + 1] = "_"
            two_next_state[1][current_super_mario_index[1] + 2] = "SM"
            sequence_movement_arr.append(two_next_state)
            i += 2

        elif win_path[i] == "2":
            current_super_mario_index = get_super_mario_index(sequence_movement_arr[-1], "SM")
            next_state = copy.deepcopy(sequence_movement_arr[-1])
            next_state[current_super_mario_index[0]][current_super_mario_index[1]] = "_"
            next_state[1][current_super_mario_index[1] + 1] = "SM"
            sequence_movement_arr.append(next_state)
            i += 1

    return sequence_movement_arr


# print(get_sequence_movement("0000", test))



class GraphicalUserInterface():

    def __init__(self, path):
        self.path = path
        self.step = 0
        # self.game_plate = game_plate
        self.Visualize()



    def Visualize(self, e=1):
        num_rows, num_cols = 2, 6

        WIDTH = (num_cols * 100) + 10
        HEIGHT = (num_rows * 100) + 10
        root.geometry(f"{WIDTH}x{HEIGHT}")
        root.title("goal chromosome!")
        root.config(bg="white")

        root.columnconfigure(0, weight=num_cols)
        root.columnconfigure(1, weight=num_rows)

        super_mario_image = ImageTk.PhotoImage(
            Image.open('./picture_for_gui/superMario.jpg').resize((100, 100), Image.ANTIALIAS))
        half_super_mario_image = ImageTk.PhotoImage(
            Image.open('./picture_for_gui/superMario.jpg').resize((50, 100), Image.ANTIALIAS))
        mushroom_image = ImageTk.PhotoImage(
            Image.open('./picture_for_gui/mushrooms.jpg').resize((100, 100), Image.ANTIALIAS))
        ghost_image = ImageTk.PhotoImage(Image.open('./picture_for_gui/ghost.jpg').resize((100, 100), Image.ANTIALIAS))
        gumpa_image = ImageTk.PhotoImage(Image.open('./picture_for_gui/gumpa.jpg').resize((100, 100), Image.ANTIALIAS))
        cell_image = ImageTk.PhotoImage(Image.open('./picture_for_gui/cell.png').resize((100, 100), Image.ANTIALIAS))

        if self.step < len(self.path):
            root.geometry(f"{WIDTH}x{HEIGHT}")
            root.title("goal chromosome!")
            root.config(bg="white")

            root.columnconfigure(0, weight=num_cols)
            root.columnconfigure(1, weight=num_rows)
            super_mario_index = get_super_mario_index(self.path[self.step], "SM")
            print(super_mario_index)
            super_mario_index_i, super_mario_index_j = super_mario_index[0], super_mario_index[1] - 1
            print(self.path[self.step])
            for r in range(num_rows):
                for c in range(num_cols):
                    if self.path[self.step][r][c + super_mario_index_j] == "_":
                        cell_label = ttk.Label(root, image=cell_image)
                        cell_label.grid(column=c, row=r)


                    elif self.path[self.step][r][c + super_mario_index_j] == "G":
                        gumpa_label = ttk.Label(root, image=gumpa_image)
                        gumpa_label.grid(column=c, row=r)

                    elif self.path[self.step][r][c + super_mario_index_j] == "L":
                        ghost_label = ttk.Label(root, image=ghost_image)
                        ghost_label.grid(column=c, row=r)

                    elif self.path[self.step][r][c + super_mario_index_j] == "SM":
                        super_mario_label = ttk.Label(root, image=super_mario_image)
                        super_mario_label.grid(column=c, row=r)

                    elif self.path[self.step][r][c + super_mario_index_j] == "M":
                        mushroom_label = ttk.Label(root, image=mushroom_image)
                        mushroom_label.grid(column=c, row=r)



            self.step += 1
            root.after(800, self.Visualize)
            root.mainloop()
        # super_mario_label = ttk.Label(root, image=super_mario_image)
        # super_mario_label.grid(column=0, row=1)

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

        # root.mainloop()

game_plate_arr = create_game_plate_arr("__G___L_" + "______")
print(game_plate_arr)
movement = get_sequence_movement("01010200", game_plate_arr)
print(movement)
g = GraphicalUserInterface(movement)
g.Visualize()
# g = GraphicalUserInterface("001100", "_G_ML_")
