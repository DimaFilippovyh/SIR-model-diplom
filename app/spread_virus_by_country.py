import asyncio
import random
import time
from proliferation_virus import (
    proliferation_virus,
    proliferation_virus_with_other_county)
from draw_diagram import draw_situation_in_world


async def infecting_one_country():
    asyncio.sleep()
    pass


def infecting_countries(lst_country):
    random.shuffle(lst_country)
    for country in lst_country:
        time_infecting = random.randint(5, 50)
        time.sleep(time_infecting)


def chenge_count_infected_people(lst_country):
    infected_people_R = lst_country[0].return_infected_people()[-1]
    infected_people_G = lst_country[1].return_infected_people()[-1]
    infected_people_I = lst_country[2].return_infected_people()[-1]
    return {
        lst_country[0].get_name_country(): infected_people_R,
        lst_country[1].get_name_country(): infected_people_G,
        lst_country[2].get_name_country(): infected_people_I
    }


def spread_virus_by_country(lst_country):
    # print_every_10_sec()
    # draw_situarion_in_world(lst_country)
    # return None
    infected_people_in_country = chenge_count_infected_people(lst_country[3:])
    poll_count = 0
    while True:
        for _ in range(50):
            for country in lst_country[:3]:
                proliferation_virus(country)
            print()
            for country in lst_country[3:]:
                proliferation_virus_with_other_county(country,
                    infected_people_in_country)
            print()

            infected_people_in_country = chenge_count_infected_people(
                lst_country[3:])

        print(f"poll nomber {poll_count}")
        poll_count += 1

        draw_situation_in_world(lst_country)
