from checks import check_connection_dominoes


def choosing_best_move(dominoes_points: dict, computer_pieces: list, domino_snake: list):
    """An attempt to put the best rate of domino on the table, if no dominoes can be placed, we skip the move"""
    for key in dominoes_points.keys():
        if check_connection_dominoes(key, computer_pieces, domino_snake):
            return key
    return 0


def scoring_points(computer_pieces: list, graph: dict) -> dict:
    """Calculation of the rating for each domino in the computer deck"""
    dominoes_points = {}
    domino_number = 1
    for domino in computer_pieces:
        counter = 0
        for number in domino:
            counter += graph[number]
        # since dominoes can be placed at both ends, there will be twice as many options for values
        dominoes_points[domino_number] = counter
        dominoes_points[-domino_number] = counter
        domino_number += 1

    # sorting dominoes up your sleeve from bigger to smaller
    sorted_dominoes_points = {k: v for k, v in sorted(dominoes_points.items(), key=lambda x: x[1], reverse=True)}
    return sorted_dominoes_points  # {3: 8, 1: 7, 2: 4}


def get_domino_values(i: int, counter: int, dominoes_list: list) -> int:
    """How many times does the domino value occur on the table and in the deck"""
    for domino in dominoes_list:
        for number in domino:
            if i == number:
                counter += 1
    return counter


def computer_tactics(computer_pieces: list, domino_snake: list) -> int:
    """Here the main algorithm of the computer is carried out"""
    graph = {}
    for i in range(7):
        counter = 0
        counter = get_domino_values(i, counter, domino_snake)
        counter = get_domino_values(i, counter, computer_pieces)
        graph[i] = counter

    dominoes_points = scoring_points(computer_pieces, graph)
    domino_number = choosing_best_move(dominoes_points, computer_pieces, domino_snake)
    return domino_number
