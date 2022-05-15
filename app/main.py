import sys
from spread_virus_in_country import (
    spread_virus_in_country,
    spread_virus_in_bifurcation,
    spread_virus_in_countries
)
from Country import Country
from parameters_contacts import get_interaction_parameters
from constans import NAMES_OF_COUNTRIES


def main():
    try:
        number_situation = int(sys.argv[1])
    except IndexError:
        print("Надо добавить параметр number_situation\n")
        number_situation = -1
    # number_situation = 4

    if number_situation == 0:
        # для одной страны
        country = Country('Russia', 0.03, 0.005)
        country.start_viruses()
        country_2 = Country('Russia', 0.03, 0.005)
        country_2.start_viruses()
        spread_virus_in_country(country, country_2)

    elif number_situation in (1, 2):
        parameters_contact_countries = get_interaction_parameters(number_situation)

        lst_countries = []
        for name in NAMES_OF_COUNTRIES:
            country = Country(name, *parameters_contact_countries[0].get(name))
            lst_countries.append(country)

        lst_countries_with_contacts = []
        for name in NAMES_OF_COUNTRIES:
            country = Country(name, *parameters_contact_countries[0].get(name),
                              parameters_contact_countries[1].get(name))
            lst_countries_with_contacts.append(country)

        if number_situation == 1:
            # фигура 1
            # TODO:
            for country in lst_countries:
                country.start_viruses()

            for country in lst_countries_with_contacts:
                country.start_viruses()
        elif number_situation == 2:
            # фигура 2 цикл
            lst_countries[0].start_viruses()
            lst_countries_with_contacts[0].start_viruses()

        spread_virus_in_countries(lst_countries, lst_countries_with_contacts)

    elif number_situation == 3:
        """Ситуация для бифуркации"""
        spread_virus_in_bifurcation()


if __name__ == "__main__":
    main()
