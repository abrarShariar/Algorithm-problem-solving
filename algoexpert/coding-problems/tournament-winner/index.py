# SOLVED
def tournamentWinner(competitions, results):
    # Write your code here.
    game_pointer = 0
    max_key = ''
    max_winning_count = 0
    player_dict = {}

    while game_pointer < len(competitions):
        game = competitions[game_pointer]
        result = results[game_pointer]
        if result == 0:
            winner = game[1]
        else:
            winner = game[0]

        player_dict[winner] = player_dict.get(winner, 0) + 1
        if player_dict[winner] > max_winning_count:
            max_winning_count = player_dict[winner]
            max_key = winner

        game_pointer += 1

    return max_key


# tournamentWinner()
