from app.player_state import PLAYER_STATE, PlayerState


def get_player_state() -> PlayerState:
    """
    Return player_state singleton
    :return:
    """
    return PLAYER_STATE
