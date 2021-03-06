import sc2
from sc2.constants import *


class FirstZergBot(sc2.BotAI):
    def __init__(self):
        self.drone_created_counter = 0
        self.first_pool_created = False

    async def on_step(self, iteration):
        if iteration == 0:
            await self.chat_send("gl hf")

        await self.expand()
        await self.build_extractor()
        await self.build_pool()

        await self.distribute_workers()  # in sc2/bot_ai.py
        await self.build_overlord()
        await self.build_workers()

    async def build_workers(self):
        larvae = self.units(LARVA)
        if self.supply_left > 3 and self.can_afford(DRONE) and larvae.exists:
            self.drone_created_counter += 1
            # print("drone_counter = " + str(self.drone_created_counter) + "\n")
            await self.do(larvae.random.train(DRONE))

    async def build_overlord(self):
        larvae = self.units(LARVA)
        if self.supply_left < 5 and self.can_afford(OVERLORD) \
                and not self.already_pending(OVERLORD) and larvae.exists:
            await self.do(larvae.random.train(OVERLORD))

    async def expand(self):
        if self.units(HATCHERY).amount < 3 and self.can_afford(HATCHERY) and not self.already_pending(HATCHERY):
            await self.expand_now()

    async def build_extractor(self):
        for hatch in self.units(HATCHERY).ready:
            vespenes = self.state.vespene_geyser.closer_than(10.0, hatch)
            for vespene in vespenes:
                if not self.can_afford(EXTRACTOR) or self.units(HATCHERY).amount < 2:
                    break
                worker = self.select_build_worker(vespene.position)
                if worker is None:
                    break
                if not self.units(EXTRACTOR).closer_than(1.0, vespene).exists:
                    await self.do(worker.build(EXTRACTOR, vespene))

    async def build_pool(self):
        if self.units(SPAWNINGPOOL).amount < 1 and self.can_afford(SPAWNINGPOOL) and not self.already_pending(
                SPAWNINGPOOL) and self.workers.exists:
            if not self.first_pool_created:
                if self.units(HATCHERY).amount > 1 and self.units(EXTRACTOR).amount > 0:
                    self.first_pool_created = True
                    firstHatch = self.units(HATCHERY).first
                    await self.build(SPAWNINGPOOL, near=firstHatch)#TODO: improve pool location
            else:
                # pool was destroyed, rebuild asap
                firstAvailableHatch = self.units(HATCHERY).first
                await self.build(SPAWNINGPOOL, near=firstAvailableHatch)
