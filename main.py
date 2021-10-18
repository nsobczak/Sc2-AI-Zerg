import sc2
from sc2 import maps, Race, Difficulty
from sc2.constants import *
from sc2.player import Bot, Computer


class FirstBot(sc2.BotAI):
    def __init__(self):
        self.drone_created_counter = 0

    async def on_step(self, iteration):
        if iteration == 0:
            await self.chat_send("gl hf")

        await self.distribute_workers()  # in sc2/bot_ai.py
        await self.build_workers()
        await self.build_overlord()

    async def build_workers(self):
        larvae = self.units(LARVA)
        if self.supply_left > 3 and self.can_afford(DRONE) and larvae.exists:
            self.drone_created_counter += 1
            print("drone_counter = " + str(self.drone_created_counter) + "\n")
            await self.do(larvae.random.train(DRONE))

    async def build_overlord(self):
        larvae = self.units(LARVA)
        if self.supply_left < 5 and self.can_afford(OVERLORD) and not self.already_pending(
                OVERLORD) and larvae.exists:
            await self.do(larvae.random.train(OVERLORD))


def main():
    # AcropolisLE, ThunderbirdLE, TurboCruise'84LE, KingsCoveLE, TritonLE, DiscoBloodbathLE
    sc2.run_game(maps.get("ThunderbirdLE"), [
        Bot(Race.Zerg, FirstBot()),
        Computer(Race.Terran, Difficulty.Easy)
    ], realtime=False)
    # , realtime=False, save_replay_as="ZvT.SC2Replay"


if __name__ == '__main__':
    main()
