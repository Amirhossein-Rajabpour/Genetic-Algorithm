import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import copy

root = tk.Tk()


def create_game_plate_arr(game_plate_str):
    end_string = "_F______"
    game_plate_str += end_string
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
        elif char == "F":
            first_row += "_"
            second_row += "F"

    first_row_split = [char for char in first_row]
    second_row_split = [char for char in second_row]
    game_plate_arr = [first_row_split, second_row_split]
    return game_plate_arr


def get_first_state(game_plate_arr):
    game_plate_arr_copy = copy.deepcopy(game_plate_arr)
    game_plate_arr_copy[1][0] = "SM"  # super mario
    return game_plate_arr_copy


def get_super_mario_index(arr):
    string1, string2 = "SM", "SML"
    row_number = len(arr)
    for i in range(row_number):
        if string1 in arr[i]:
            index_j = arr[i].index(string1)
            return i, index_j

        if string2 in arr[i]:
            index_j = arr[i].index(string2)
            return i, index_j


def get_sequence_movement(win_path, game_plate_arr):
    sequence_movement_arr = []
    super_mario_index = 0

    first_state = get_first_state(game_plate_arr)
    sequence_movement_arr.append(first_state)

    i = 0
    while i < len(win_path):
        current_super_mario_index = get_super_mario_index(sequence_movement_arr[-1])

        if win_path[i] == "0":
            next_state = copy.deepcopy(sequence_movement_arr[-1])
            next_state[current_super_mario_index[0]][current_super_mario_index[1]] = "_"
            next_state[1][current_super_mario_index[1] + 1] = "SM"
            sequence_movement_arr.append(next_state)
            i += 1

        elif win_path[i] == "1":
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
            next_state = copy.deepcopy(sequence_movement_arr[-1])
            next_state[current_super_mario_index[0]][current_super_mario_index[1]] = "_"
            next_state[1][current_super_mario_index[1] + 1] = "SML"
            sequence_movement_arr.append(next_state)
            i += 1

    return sequence_movement_arr


# print(get_sequence_movement("0000", test))


class GraphicalUserInterface():

    def __init__(self, path):
        self.path = path
        self.step = 0
        self.Visualize()

    def Visualize(self, e=1):
        num_rows, num_cols = 2, 8

        WIDTH = (num_cols * 100) + 10
        HEIGHT = (num_rows * 100) + 10
        root.geometry(f"{WIDTH}x{HEIGHT}")
        root.title("goal chromosome!")
        root.config(bg="white")

        root.columnconfigure(0, weight=num_cols)
        root.columnconfigure(1, weight=num_rows)

        super_mario_image = ImageTk.PhotoImage(Image.open('./picture_for_gui/superMario1.png').resize((100, 100), Image.ANTIALIAS))
        half_super_mario_image = ImageTk.PhotoImage(Image.open('./picture_for_gui/superMario2.png').resize((100, 100), Image.ANTIALIAS))
        mushroom_image = ImageTk.PhotoImage(Image.open('./picture_for_gui/mushrooms.jpg').resize((100, 100), Image.ANTIALIAS))
        ghost_image = ImageTk.PhotoImage(Image.open('./picture_for_gui/ghost.jpg').resize((100, 100), Image.ANTIALIAS))
        goomba_image = ImageTk.PhotoImage(Image.open('./picture_for_gui/goomba.jpg').resize((100, 100), Image.ANTIALIAS))
        cell_image = ImageTk.PhotoImage(Image.open('./picture_for_gui/cell.png').resize((100, 100), Image.ANTIALIAS))
        flag_image = ImageTk.PhotoImage(Image.open('./picture_for_gui/flag.jpg').resize((100, 100), Image.ANTIALIAS))

        if self.step < len(self.path):
            root.geometry(f"{WIDTH}x{HEIGHT}")
            root.title("goal chromosome!")
            root.config(bg="white")

            root.columnconfigure(0, weight=num_cols)
            root.columnconfigure(1, weight=num_rows)
            super_mario_index = get_super_mario_index(self.path[self.step])
            print(super_mario_index)
            super_mario_index_i, super_mario_index_j = super_mario_index[0], super_mario_index[1] - 1
            print(self.path[self.step])
            for r in range(num_rows):
                for c in range(num_cols):
                    if self.path[self.step][r][c + super_mario_index_j] == "_":
                        cell_label = ttk.Label(root, image=cell_image)
                        cell_label.grid(column=c, row=r)


                    elif self.path[self.step][r][c + super_mario_index_j] == "G":
                        gumpa_label = ttk.Label(root, image=goomba_image)
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

                    elif self.path[self.step][r][c + super_mario_index_j] == "SML":
                        half_super_mario_label = ttk.Label(root, image=half_super_mario_image)
                        half_super_mario_label.grid(column=c, row=r)

                    elif self.path[self.step][r][c + super_mario_index_j] == "F":
                        flag_label = ttk.Label(root, image=flag_image)
                        flag_label.grid(column=c, row=r)

            self.step += 1
            root.after(800, self.Visualize)
        root.mainloop()


game_plate_arr = create_game_plate_arr("__GM__LL")
print(game_plate_arr)
movement = get_sequence_movement("01010220", game_plate_arr)
print(movement)
g = GraphicalUserInterface(movement)
g.Visualize()
# g = GraphicalUserInterface("001100", "_G_ML_")
