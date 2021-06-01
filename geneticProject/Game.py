import copy


class Game:
    def __init__(self, game_plate):
        # Get a strings as game_plate
        # Store level length to determine if a sequence of action passes all the steps
        self.game_plate = game_plate

    def calculate_maximum_substring_length(self, failure_points):
        game_plate = self.game_plate
        length_game_plate = len(game_plate)
        substring_length = []

        failure_points.insert(0, 0)
        failure_points.append(length_game_plate)

        for i in range(1, len(failure_points)):
            length = failure_points[i] - failure_points[i - 1]
            substring_length.append(length)

        return max(substring_length)

    def get_score(self, actions, get_score_mode):
        # Get an action sequence and determine the steps taken/score
        # Return a tuple, the first one indicates if these actions result in victory
        # and the second one shows the steps taken

        game_plate = self.game_plate
        length_game_plate = len(game_plate)
        failure_points = []
        steps = 0
        scores = 0
        for i in range(length_game_plate):
            current_step = game_plate[i]
            if current_step == '_':
                steps += 1
            elif current_step == 'G':
                if actions[i - 1] == '1':
                    steps += 1
                elif i - 2 >= 0 and actions[i - 2] == "1":       # score section project
                    steps += 1
                    scores += 2
                else: failure_points.append(i)

            elif current_step == "M":  # score section project
                if actions[i - 1] != "1": scores += 2
                steps += 1
            # elif i == length_game_plate - 1 and current_step == "1":  # score section project
            #     steps += 1
            #     scores += 1
            elif current_step == 'L':
                if i - 2 >= 0:
                    if actions[i - 1] == "2" and actions[i - 2] != "1":
                        steps += 1
                    else: failure_points.append(i)
                elif actions[i - 1] == '2':
                    steps += 1
                else: failure_points.append(i)
            else:
                failure_points.append(i)

        if actions[-1] == "1": scores += 1 # score section project (when final action is jump and move right)

        # print(scores)
        # print(failure_points)
        failure_points_copy = copy.deepcopy(failure_points)
        maximum_substring_length = self.calculate_maximum_substring_length(failure_points_copy)

        # print(maximum_substring_length)
        if get_score_mode == "1":
            if len(failure_points) == 0: scores += 5    # if failure_points is empty => chromosome is win.

        return maximum_substring_length + scores, failure_points


# g = Game("____G_ML__G_")
#
#
# #
# print(g.get_score("001000101000", "1"))
