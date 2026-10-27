def player(prev_play, opponent_history=[], my_history=[], play_order={}):
    if prev_play in ["R", "P", "S"]:
        opponent_history.append(prev_play)

    if not opponent_history:
        opponent_history.append("R")
        return "P"

    # Predict opponent based on their last 3 moves
    if len(opponent_history) >= 3:
        last_three = "".join(opponent_history[-3:])

        play_order[last_three] = play_order.get(last_three, 0) + 1

        possible = [last_three[1:] + move for move in "RPS"]

        predicted_opponent_move = max(
            possible,
            key=lambda pattern: play_order.get(pattern, 0)
        )[-1]
    else:
        predicted_opponent_move = opponent_history[-1]

    counter_moves = {
        "R": "P",
        "P": "S",
        "S": "R"
    }

    my_move = counter_moves[predicted_opponent_move]

    # Avoid becoming predictable against Abbey
    if len(my_history) >= 3:
        my_last_three = "".join(my_history[-3:])

        if my_last_three in ["PPP", "SSS", "RRR"]:
            my_move = counter_moves[my_move]

    if len(opponent_history) % 150 == 0:
        play_order.clear()

    my_history.append(my_move)
    return my_move
