import time
from Country import Country
from constans import length_virus, NAMES_OF_COUNTRIES


def proliferation_virus_for_one_country_without_two_wave(country: Country):
    """
    contacting - частота встречи людей
    recovered - коэф. выздоровления
    length_vir - протяженность болезни
    infected_people - больные люди
    none_infected_people = не болевшие люди
    recovered_people - выздоровевшие
    k_two_wave - коэф. с которым люди заболевают повторно
    """
    name = country.name
    infected_people, none_infected_people, recovered_people = \
        country.get_situation_in_country()
    contacting, recovered = country.get_parameters_country()

    tmp_infected_people = contacting * infected_people[-1] * \
        none_infected_people[-1]

    tmp_recovered_people = recovered * \
        infected_people[-1 - length_virus]

    tomr_infected_people = tmp_infected_people - tmp_recovered_people + \
        infected_people[-1]

    tomr_none_infected_people = none_infected_people[-1] - \
        tmp_infected_people

    tomr_recovered_people = recovered_people[-1] + tmp_recovered_people

    new_values = Country.normalize_solution([tomr_infected_people,
        tomr_none_infected_people, tomr_recovered_people])

    country.change_situation(new_values)

    print(name, *new_values)

    if tomr_none_infected_people < 0.02:
        print(F"All people infected in {name}")

    if tomr_recovered_people > 0.98:
        print(F"All people recuperation in {name}!!!")
    time.sleep(0)
    # time.sleep(0.3)


def proliferation_virus_for_one_country(country: Country):
    """
    contacting - частота встречи людей
    recovered - коэф. выздоровления
    length_vir - протяженность болезни
    infected_people - больные люди
    none_infected_people = не болевшие люди
    recovered_people - выздоровевшие
    k_two_wave - коэф. с которым люди заболевают повторно
    """

    k_two_wave = 0.1
    """
    # при 0.1 побеждается болезнь
    # при параметре 0.5 останавливаеться на 66 и 33 процентах
    # при 0.7 гуляет в нижней части
    # при 0.9 интересно по всему графику ходит
    # при 1.1 побеждает болезнь
    """

    name = country.name
    infected_people, none_infected_people, recovered_people = \
        country.get_situation_in_country()
    contacting, recovered = country.get_parameters_country()

    tmp_infected_people = contacting * infected_people[-1] * \
        none_infected_people[-1]

    tmp_recovered_people = recovered * \
        infected_people[-1 - length_virus]

    if len(infected_people) > 92:
        tmp_two_wave_infected_people = k_two_wave * contacting * \
            infected_people[-1] * recovered_people[-1 - 90]
    else:
        tmp_two_wave_infected_people = 0

    tomr_infected_people = tmp_infected_people - tmp_recovered_people + \
        infected_people[-1] + tmp_two_wave_infected_people  # FIXME:

    tomr_none_infected_people = none_infected_people[-1] - \
        tmp_infected_people

    tomr_recovered_people = recovered_people[-1] + tmp_recovered_people - \
        tmp_two_wave_infected_people

    new_values = Country.normalize_solution([tomr_infected_people,
        tomr_none_infected_people, tomr_recovered_people])

    country.change_situation(new_values)

    print(name + "_V2", *new_values)

    if tomr_none_infected_people < 0.02:
        print(F"All people infected in {name}")

    if tomr_recovered_people > 0.98:
        print(F"All people recuperation in {name}!!!")
    time.sleep(0)
    # time.sleep(0.3)


def proliferation_virus(country: Country):
    """
    contacting - частота встречи людей
    recovered - коэф. выздоровления
    length_vir - протяженность болезни
    infected_people - больные люди
    none_infected_people = не болевшие люди
    recovered_people - выздоровевшие
    k_two_wave - коэф. с которым люди заболевают повторно
    """
    name = country.name
    infected_people, none_infected_people, recovered_people = \
        country.get_situation_in_country()
    contacting, recovered = country.get_parameters_country()

    tmp_infected_people = contacting * infected_people[-1] * \
        none_infected_people[-1]

    tmp_recovered_people = recovered * \
        infected_people[-1 - length_virus]

    tomr_infected_people = tmp_infected_people - tmp_recovered_people + \
        infected_people[-1]

    tomr_none_infected_people = none_infected_people[-1] - \
        tmp_infected_people

    tomr_recovered_people = recovered_people[-1] + tmp_recovered_people

    new_values = Country.normalize_solution([tomr_infected_people,
        tomr_none_infected_people, tomr_recovered_people])

    country.change_situation(new_values)

    print(name, *new_values)

    if tomr_none_infected_people < 0.02:
        print(F"All people infected in {name}")

    if tomr_recovered_people > 0.98:
        print(F"All people recuperation in {name}!!!")
    time.sleep(0)
    # time.sleep(0.3)


def proliferation_virus_with_other_county(country: Country,
        infected_people_in_countries):
    """
    contacting - частота встречи людей
    recovered - коэф. выздоровления
    length_vir - протяженность болезни
    infected_people - больные люди
    none_infected_people = не болевшие люди
    recovered_people - выздоровевшие
    k_two_wave - коэф. с которым люди заболевают повторно
    other_infected_people - больные люди прибывшие из других стран
    """
    name = country.name
    infected_people, none_infected_people, recovered_people = \
        country.get_situation_in_country()
    contacting, recovered = country.get_parameters_country()

    other_names_of_countries = [i for i in NAMES_OF_COUNTRIES if i != name]

    infected_people_from_other_countries = [
        infected_people_in_countries.get(i) *
        country.contacts_country.get(i)
        for i in other_names_of_countries]

    other_infected_people = [none_infected_people[-1] * i
        for i in infected_people_from_other_countries]

    tmp_infected_people = contacting * infected_people[-1] * \
        none_infected_people[-1]

    # FIXME: chenge expression
    if tmp_infected_people == 0:
        tmp_infected_people = sum(other_infected_people)
    else:
        tmp_infected_people *= (1 + sum(other_infected_people))

    tmp_recovered_people = recovered * \
        infected_people[-1 - length_virus]

    tomr_infected_people = tmp_infected_people - tmp_recovered_people + \
        infected_people[-1]

    tomr_none_infected_people = none_infected_people[-1] - \
        tmp_infected_people

    tomr_recovered_people = recovered_people[-1] + tmp_recovered_people

    new_values = Country.normalize_solution([tomr_infected_people,
        tomr_none_infected_people, tomr_recovered_people])

    country.change_situation(new_values)

    print(name + "_V2", *new_values)

    if tomr_none_infected_people < 0.02:
        print(F"All people infected in {name}")

    if tomr_recovered_people > 0.98:
        print(F"All people recuperation in {name}!!!")
    time.sleep(0)
    # time.sleep(0.3)


def proliferation_virus_with_other_county_with_two_wave(country: Country,
        infected_people_in_countries):
    """
    contacting - частота встречи людей
    recovered - коэф. выздоровления
    length_vir - протяженность болезни
    infected_people - больные люди
    none_infected_people = не болевшие люди
    recovered_people - выздоровевшие
    k_two_wave - коэф. с которым люди заболевают повторно
    other_infected_people - больные люди прибывшие из других стран
    """
    # FIXME:

    k_two_wave = 1.1
    """
    при 0.5 переливы
    """

    name = country.name
    infected_people, none_infected_people, recovered_people = \
        country.get_situation_in_country()
    contacting, recovered = country.get_parameters_country()

    other_names_of_countries = [i for i in NAMES_OF_COUNTRIES if i != name]

    infected_people_from_other_countries = [
        infected_people_in_countries.get(i) *
        country.contacts_country.get(i)
        for i in other_names_of_countries]

    other_infected_people = [none_infected_people[-1] * i
        for i in infected_people_from_other_countries]

    tmp_infected_people = contacting * infected_people[-1] * \
        none_infected_people[-1]

    # FIXME: chenge expression
    if tmp_infected_people == 0:
        tmp_infected_people = sum(other_infected_people)
    else:
        tmp_infected_people *= (1 + sum(other_infected_people))

    tmp_recovered_people = recovered * \
        infected_people[-1 - length_virus]

    if len(infected_people) > 92:
        tmp_two_wave_infected_people = k_two_wave * contacting * \
            infected_people[-1] * recovered_people[-1 - 90]
    else:
        tmp_two_wave_infected_people = 0

    tomr_infected_people = tmp_infected_people - tmp_recovered_people + \
        infected_people[-1] + tmp_two_wave_infected_people

    tomr_none_infected_people = none_infected_people[-1] - \
        tmp_infected_people

    tomr_recovered_people = recovered_people[-1] + tmp_recovered_people - \
        tmp_two_wave_infected_people

    new_values = Country.normalize_solution([tomr_infected_people,
        tomr_none_infected_people, tomr_recovered_people])

    country.change_situation(new_values)

    print(name + "_V2", *new_values)

    if tomr_none_infected_people < 0.02:
        print(F"All people infected in {name}")

    if tomr_recovered_people > 0.98:
        print(F"All people recuperation in {name}!!!")
    time.sleep(0)
    # time.sleep(0.3)
