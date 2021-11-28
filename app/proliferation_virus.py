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
