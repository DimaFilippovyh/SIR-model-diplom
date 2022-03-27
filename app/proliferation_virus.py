import time
from Country import Country
from constans import length_virus


def proliferation_virus(Country: Country):
    """
    all_people - количество больных
    k_recuperation - коэф. выздоровления
    length_vir - протяженность болезни
    count_contakt - частота встречи людей
    infected_people - больные люди
    -1 - день с 1 заражения
    none_infected_people = не болеющие люди(выздоровили или "все")
    recovered_people - выздоровевшие
    """
    name, infected_people, none_infected_people, recovered_people, \
        contacting, recovered = Country.situation_in_country()

    tmp_infected_people = contacting * infected_people[-1] * \
        none_infected_people[-1]

    tmp_recovered_people = recovered * \
        infected_people[-1 - length_virus]

    tomr_infected_people = tmp_infected_people - tmp_recovered_people + \
        infected_people[-1]

    tomr_none_infected_people = none_infected_people[-1] - \
        tmp_infected_people

    tomr_recovered_people = recovered_people[-1] + tmp_recovered_people

    Country.change_situation([tomr_infected_people, tomr_none_infected_people,
        tomr_recovered_people])

    print(Country.name, [tomr_infected_people, tomr_none_infected_people,
        tomr_recovered_people])

    if tomr_none_infected_people < 0.02:
        print(F"All people infected in {name}")

    if tomr_recovered_people > 0.98:
        print(F"All people recuperation in {name}!!!")
    time.sleep(0)
    # time.sleep(0.3)


def proliferation_virus_with_other_county(Country: Country,
        infected_people_in_countries):
    """
    all_people - количество больных
    k_recuperation - коэф. выздоровления
    length_vir - протяженность болезни
    count_contakt - частота встречи людей
    infected_people - больные люди
    -1 - день с 1 заражения
    none_infected_people = не болеющие люди(выздоровили или "все")
    recovered_people - выздоровевшие
    """
    names_of_countries = list(infected_people_in_countries.keys())
    names_of_countries = [name for name in names_of_countries
        if name != Country.get_name_country()]

    name, infected_people, none_infected_people, recovered_people, \
        contacting, recovered = Country.situation_in_country()

    invected_people_from_other_countries = [
        infected_people_in_countries.get(i) *
        Country.list_of_contacts_country.get(i)
        for i in names_of_countries]

    other_infected_people = [none_infected_people[-1] * i
        for i in invected_people_from_other_countries]

    # tmp_infected_people = contacting * infected_people[-1] * \
    #     none_infected_people[-1] * sum(other_infected_people)

    tmp_infected_people = contacting * infected_people[-1] * \
        none_infected_people[-1]

    tmp_tme_infect = sum(other_infected_people)

    tmp_infected_people = tmp_infected_people + tmp_tme_infect

    tmp_recovered_people = recovered * \
        infected_people[-1 - length_virus]

    tomr_infected_people = tmp_infected_people - tmp_recovered_people + \
        infected_people[-1]

    tomr_none_infected_people = none_infected_people[-1] - \
        tmp_infected_people

    tomr_recovered_people = recovered_people[-1] + tmp_recovered_people

    Country.change_situation([tomr_infected_people, tomr_none_infected_people,
        tomr_recovered_people])

    print(Country.name + "_V2", [tomr_infected_people,
        tomr_none_infected_people, tomr_recovered_people])

    if tomr_none_infected_people < 0.02:
        print(F"All people infected in {name}")

    if tomr_recovered_people > 0.98:
        print(F"All people recuperation in {name}!!!")
    time.sleep(0)
    # time.sleep(0.3)
