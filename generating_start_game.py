from random import seed, choice
from constants import MAX_DOMINO_VALUE


def the_first_move(computer_pieces: list, player_pieces: list) -> list:
    """Finding the maximum double domino from the player's or computer's set"""
    domino_sets = computer_pieces + player_pieces
    double_dominoes = []

    for i in range(MAX_DOMINO_VALUE):
        if [i, i] in domino_sets:
            double_dominoes.append([i, i])

    the_initial_domino = max(double_dominoes) if double_dominoes else []
    return the_initial_domino


def split_dominoes(remaining_dominoes: list, domino_set: list, quantity=MAX_DOMINO_VALUE) -> None:
    """Creating a set of 7 unique dominoes for the player or computer"""
    for i in range(quantity):
        selected_domino = choice(remaining_dominoes)
        remaining_dominoes.remove(selected_domino)
        domino_set.append(selected_domino)


def domino_generation(stock_pieces: list) -> None:
    """Creating a common set of 28 unique dominoes"""
    seed()
    start = 0
    for i in range(MAX_DOMINO_VALUE):
        for j in range(start, MAX_DOMINO_VALUE):
            stock_pieces.append([i, j])
        start += 1
