import sc2
from sc2 import maps, Race, Difficulty
from sc2.constants import *
from sc2.player import Bot, Computer

from zerg_bot import FirstZergBot

from examples.zerg.zerg_rush import ZergRushBot
from examples.terran.ramp_wall import RampWallBot



def main():
    # AcropolisLE, ThunderbirdLE, TurboCruise'84LE, KingsCoveLE, TritonLE, DiscoBloodbathLE
    sc2.run_game(maps.get("ThunderbirdLE"), [
        Bot(Race.Zerg, FirstZergBot()),
        # Bot(Race.Zerg, ZergRushBot())
        # Bot(Race.Terran, RampWallBot())
        Computer(Race.Terran, Difficulty.Easy)
    ], realtime=False)
    # , realtime=False, save_replay_as="ZvT.SC2Replay"


if __name__ == '__main__':
    main()
