from constants import COMPUTER_STEP_STATUS, PLAYER_STEP_STATUS
from generating_start_game import domino_generation, split_dominoes, the_first_move
from output import printing_intermediate_result
from computer_algorithm import computer_tactics
from checks import checking_domino


def choosing_an_action(stock_pieces: list, domino_set: list, domino_snake: list, domino_number: int) -> None:
    """To make a move, the player has to specify the action they want to take."""
    # take an extra piece from the stock (if it's not empty) and skip a turn
    if domino_number == 0:
        if len(stock_pieces) > 0:
            split_dominoes(stock_pieces, domino_set, 1)

    else:
        index = abs(domino_number) - 1
        if domino_number < 0:
            # Select a domino and place it on the left side of the snake. Flip the dominoes if necessary
            end_domino_snake = domino_snake[0][0]
            if domino_set[index][1] == end_domino_snake:
                domino_snake.insert(0, domino_set[index])
            else:
                domino_snake.insert(0, domino_set[index][::-1])
        else:
            # select a domino and place it on the right side of the snake. Flip the dominoes if necessary
            end_domino_snake = domino_snake[len(domino_snake) - 1][1]
            if domino_set[index][0] == end_domino_snake:
                domino_snake.append(domino_set[index])
            else:
                domino_snake.append(domino_set[index][::-1])

        del domino_set[index]


def main():
    # if neither the player nor the computer has a double domino, all the dominoes are "shuffled".
    while True:
        stock_pieces = []
        computer_pieces, player_pieces = [], []
        domino_snake = []

        domino_generation(stock_pieces)

        split_dominoes(stock_pieces, computer_pieces)
        split_dominoes(stock_pieces, player_pieces)

        the_initial_domino = the_first_move(computer_pieces, player_pieces)

        if the_initial_domino:
            domino_snake.append(the_initial_domino)
            break

    # laying out the first domino on the field and assigning the next move (status)
    if the_initial_domino in computer_pieces:
        status = COMPUTER_STEP_STATUS
        computer_pieces.remove(the_initial_domino)
    else:
        status = PLAYER_STEP_STATUS
        player_pieces.remove(the_initial_domino)

    while True:
        status = printing_intermediate_result(stock_pieces=len(stock_pieces), computer_pieces=len(computer_pieces),
                                              domino_snake=domino_snake, player_pieces=player_pieces, status=status)

        if status == COMPUTER_STEP_STATUS:
            domino_number = computer_tactics(computer_pieces, domino_snake)
            choosing_an_action(stock_pieces, computer_pieces, domino_snake, domino_number)
            input()
        elif status == PLAYER_STEP_STATUS:
            domino_number = checking_domino(player_pieces, domino_snake)
            choosing_an_action(stock_pieces, player_pieces, domino_snake, domino_number)
        else:
            break


if __name__ == "__main__":
    main()
