from constants import MAX_DOMINO_VALUE, STATUS_DRAW


class WrongDominoError(Exception):
    def __str__(self):
        return "Illegal move. Please try again."


def check_connection_dominoes(domino_number: int, domino_set: list, domino_snake: list) -> bool:
    """Checks whether the selected domino can connect to snake"""
    if domino_number < 0:
        end_domino_snake = domino_snake[0][0]
    else:
        end_domino_snake = domino_snake[len(domino_snake) - 1][1]

    my_domino = domino_set[abs(domino_number) - 1]
    return True if end_domino_snake in my_domino else False


def checking_domino(player_pieces: list, domino_snake: list) -> int:
    """Checking the correct value of the selected domino from a number in the list"""
    while True:
        try:
            domino_number = int(input())
            if abs(domino_number) > len(player_pieces):
                raise ValueError
            elif domino_number == 0:
                return domino_number
            elif check_connection_dominoes(domino_number, player_pieces, domino_snake):
                return domino_number
            else:
                raise WrongDominoError

        except ValueError:
            print("Invalid input. Please try again.")
        except WrongDominoError as err:
            print(err)


def checking_for_draw(status: str, domino_snake: list) -> str:
    """ Checking for a draw. If the numbers at the ends of the snake are identical
        and appear inside the snake 8 times, the game ends in a draw"""
    first_domino = domino_snake[0][0]
    last_domino = domino_snake[len(domino_snake) - 1][1]
    first_amount, last_amount = 0, 0

    for domino in domino_snake:
        for number in domino:
            if first_domino == number:
                first_amount += 1
            if last_domino == number:
                last_amount += 1

    if first_amount > MAX_DOMINO_VALUE and last_amount > MAX_DOMINO_VALUE:
        return STATUS_DRAW
    return status
