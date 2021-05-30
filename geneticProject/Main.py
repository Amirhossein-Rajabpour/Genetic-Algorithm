from AdditionalFunctions import *
generation_dict = {}




if __name__ == "__main__":
    test_case = input("Which level?! ")
    test_case_file_name = test_case + ".txt"
    num_of_population = input("Number of population: ")
    get_score_mode = input("Get score mode? (1: with calculating winning points, 0: without calculating winning points)")

    game_plate = read_level_game("level1.txt")
    s = generate_initial_population(100, game_plate, "1")

    print(game_plate)
    for ch in s:
        print(ch.score)
        print(ch.string)













