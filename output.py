from constants import MAX_DOMINO_VALUE, REDUCTION_TO_THREE
from status import status_change


def printing_intermediate_result(**kwargs) -> str:
    """Printing intermediate game results"""
    print("=" * 70)
    print(f"Stock pieces: {kwargs['stock_pieces']}")
    print(f"Computer pieces: {kwargs['computer_pieces']}")

    print_domino_snake(kwargs['domino_snake'])
    print_list_dominoes(kwargs['player_pieces'])
    status = status_change(**kwargs)
    print(f"\nStatus: {status}")

    return status


def print_list_dominoes(my_dominoes: list) -> None:
    """Print a row-by-row list of the player's dominoes"""
    print("Your pieces:")
    for number, value in enumerate(my_dominoes):
        print(f"{number + 1}:{value}")


def print_domino_snake(domino_snake) -> None:
    """Print of a "snake" from a domino. If there are a lot of dominoes on the table,
       then we cut off the output (the first three from the beginning and the last three from the end)"""
    str_ = ""
    length = len(domino_snake)
    if length >= MAX_DOMINO_VALUE:
        for i in range(REDUCTION_TO_THREE):
            str_ += str(domino_snake[i])
        str_ += "..."
        for i in range(length - REDUCTION_TO_THREE, length):
            str_ += str(domino_snake[i])
    else:
        for i in range(length):
            str_ += str(domino_snake[i])

    print(f"\n{str_}\n")