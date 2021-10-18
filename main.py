import sc2
from sc2 import run_game, maps, Race, Difficulty
from sc2.player import Bot, Computer


class FirstBot(sc2.BotAI):
    async def on_step(self, iteration):
        # what to do every step
        await self.distribute_workers()  # in sc2/bot_ai.py
        # await self.build_workers()


run_game(maps.get("AcropolisLE"), [
    Bot(Race.Zerg, FirstBot()),
    Computer(Race.Terran, Difficulty.Easy)
], realtime=True)


# if __name__ == '__main__':
#     print_hi('PyCharm')

