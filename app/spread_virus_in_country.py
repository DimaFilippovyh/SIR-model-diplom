import matplotlib.pyplot as plt
import numpy as np
from Country import Country
from proliferation_virus import (
    proliferation_virus_for_one_country_without_two_wave,
    proliferation_virus_for_one_country,
    proliferation_virus_with_two_wave_koef,
    proliferation_virus,
    proliferation_virus_with_other_county,
    proliferation_virus_with_other_county_with_two_wave)
from draw_diagram import draw_situation_in_world, draw_situation_in_country, draw_situation_in_country_bifurcation


def change_count_infected_people(lst_countries_with_contacts):
    dict_countries = {}
    for country in lst_countries_with_contacts:
        dict_countries[country.name] = country.infected_people

    return dict_countries


def spread_virus_in_country(country, country_2):
    poll_count = 0
    plt.ion()
    while True:
        for _ in range(50):
            proliferation_virus_for_one_country_without_two_wave(country)
            proliferation_virus_for_one_country(country_2)

        print(f"poll nomber {poll_count}")
        poll_count += 1

        fig = draw_situation_in_country(country, country_2)

        plt.show()
        if poll_count == 1:
            plt.pause(10)
        plt.pause(0.5)
        plt.close()


def spread_virus_in_bifurcation():
    res = {}
    for i in np.arange(0.0, 1, 0.01):
        country = Country('Russia', 0.03, 0.005)
        country.start_viruses()

        for _ in range(1100):
            proliferation_virus_with_two_wave_koef(country, i)

        lst_results = country.get_situation_in_country()[0]

        res[i] = lst_results[len(lst_results) - 100:]

    draw_situation_in_country_bifurcation(res)


def spread_virus_in_countries(lst_countries, lst_countries_with_contacts):
    infected_people_in_country = change_count_infected_people(lst_countries_with_contacts)
    poll_count = 0
    plt.ion()
    while True:
        for _ in range(50):
            for country in lst_countries:
                # proliferation_virus(country)
                proliferation_virus_for_one_country(country)
                # proliferation_virus_with_other_county(country, infected_people_in_country)
            print()
            for country in lst_countries_with_contacts:
                # proliferation_virus_with_other_county(country, infected_people_in_country)
                proliferation_virus_with_other_county_with_two_wave(country, infected_people_in_country)
            print()

            infected_people_in_country = change_count_infected_people(lst_countries_with_contacts)

        print(f"poll nomber {poll_count}")
        poll_count += 1

        fig = draw_situation_in_world(lst_countries, lst_countries_with_contacts)
        plt.show()
        # if poll_count == 1:
        #     plt.pause(10)
        if poll_count < 5:
            plt.pause(1)
        else:
            plt.pause(0.5)
        plt.close()
