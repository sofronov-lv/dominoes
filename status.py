from constants import COMPUTER_STEP_STATUS, COMPUTER_VICTORY_STATUS, PLAYER_STEP_STATUS, PLAYER_VICTORY_STATUS
from checks import checking_for_draw


def status_change(**kwargs) -> str:
    """Changing the status of the game"""
    status = kwargs['status']

    # changing the order of the move
    status = PLAYER_STEP_STATUS if status == COMPUTER_STEP_STATUS else COMPUTER_STEP_STATUS

    # checking for a win or a draw
    if kwargs['computer_pieces'] == 0:
        status = COMPUTER_VICTORY_STATUS
    elif len(kwargs['player_pieces']) == 0:
        status = PLAYER_VICTORY_STATUS
    else:
        status = checking_for_draw(status, kwargs['domino_snake'])

    return status
