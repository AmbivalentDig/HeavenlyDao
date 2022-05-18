from . import heavenly_dao
from .config import config as cfg

def main():
    game = heavenly_dao.Game(cfg.resolution)
    return game.start()