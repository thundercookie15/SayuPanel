'''Game folder for DIVEKICK'''
GAME_DIVEKICK = {'name': 'Divekick', 'config': 'data/config/Divekick_T2_T3.json'}
'''Game folder for Duck Game'''
GAME_DUCKGAME = {'name': 'Duck Game', 'config': 'data/config/DuckGame_T2_T3.json'}
'''Game folder for Jump King'''
GAME_JUMPKING = {'name': 'Jump King', 'config': 'data/config/JumpKing_remote.json'}
'''Game folder for Stick Fight'''
GAME_STICKFIGHT = {'name': 'Stick Fight', 'config': 'data/config/StickFight_GP2_localremote.json'}


def get_games():
    """Returns a list of all games"""
    return [GAME_DIVEKICK, GAME_DUCKGAME, GAME_JUMPKING, GAME_STICKFIGHT]


def get_game_names():
    """Returns a list of all game names"""
    return [game['name'] for game in get_games()]


def get_selected_game_config(game_name):
    """Returns the config for the selected game"""
    return [game['config'] for game in get_games() if game['name'] == game_name][0]
