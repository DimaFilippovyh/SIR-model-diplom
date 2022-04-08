from proliferation_virus import (
    proliferation_virus_for_one_country_without_two_wave,
    proliferation_virus_for_one_country,
    proliferation_virus,
    proliferation_virus_with_other_county,
    proliferation_virus_with_other_county_with_two_wave)
from draw_diagram import draw_situation_in_world, draw_situation_in_country


def chenge_count_infected_people(lst_countries_with_contacts):
    dict_countries = {}
    for country in lst_countries_with_contacts:
        dict_countries[country.name] = country.infected_people

    return dict_countries


def spread_virus_in_country(country, country_2):
    poll_count = 0
    while True:
        for _ in range(50):
            proliferation_virus_for_one_country_without_two_wave(country)
            proliferation_virus_for_one_country(country_2)

        print(f"poll nomber {poll_count}")
        poll_count += 1

        draw_situation_in_country(country, country_2)


def spread_virus_in_countries(lst_countries, lst_countries_with_contacts):
    infected_people_in_country = chenge_count_infected_people(
        lst_countries_with_contacts)
    poll_count = 0

    while True:
        for _ in range(50):
            for country in lst_countries:
                proliferation_virus(country)
            print()
            for country in lst_countries_with_contacts:
                # proliferation_virus_with_other_county(country,
                #     infected_people_in_country)
                proliferation_virus_with_other_county_with_two_wave(country,
                    infected_people_in_country)
            print()

            infected_people_in_country = chenge_count_infected_people(
                lst_countries_with_contacts)

        print(f"poll nomber {poll_count}")
        poll_count += 1

        draw_situation_in_world(lst_countries, lst_countries_with_contacts)