import asyncio
import random
import time
from proliferation_virus import proliferation_virus
from draw_diagram import draw_situarion_in_world


async def infecting_one_country():
    asyncio.sleep()
    pass


def infecting_countries(lst_country):
    random.shuffle(lst_country)
    for country in lst_country:
        time_infecting = random.randint(5, 50)
        time.sleep(time_infecting)


def spread_virus_by_country(lst_country):
    # print_every_10_sec()
    # draw_situarion_in_world(lst_country)
    # return None
    while True:
        for i in range(50):
            for country in lst_country:
                proliferation_virus(country)
        # TODO: draw country
        draw_situarion_in_world(lst_country)
