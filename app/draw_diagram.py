import time

import matplotlib.pyplot as plt
from Country import Country
from constans import NAMES_OF_COUNTRIES


def draw_situation_in_world(lst_countries, lst_countries_with_contacts):
    plt.close()
    labels = list(NAMES_OF_COUNTRIES)
    labels.extend([name + "W2" for name in NAMES_OF_COUNTRIES])
    width = 0.35

    general_list = [*lst_countries, *lst_countries_with_contacts]

    information_of_countries = [i.get_situation_in_country() for i in general_list]
    value_infected = [i[0][-1] * 100 for i in information_of_countries]
    value_none_infected = [i[1][-1] * 100 for i in information_of_countries]
    value_recovered = [i[2][-1] * 100 for i in information_of_countries]
    lst_bottom_none_infected = [(i[0][-1] + i[2][-1]) * 100 for i in information_of_countries]

    fig, ax = plt.subplots()
    fig.set_size_inches(12, 6)

    ax.bar(labels, value_none_infected, width, bottom=lst_bottom_none_infected, label='None infected', color='blue')
    ax.bar(labels, value_infected, width, bottom=value_recovered, label='Infected', color='red')
    ax.bar(labels, value_recovered, width, label='Recovered', color='green')

    ax.set_ylabel('Percentages')
    ax.set_title('Status by country')
    ax.legend()

    # plt.show()
    return fig

def draw_situation_in_country(country, country_2: Country):
    labels = ['Russia', 'Russia with 2 wave']
    width = 0.2

    general_list = [country, country_2]

    information_of_countries = [i.get_situation_in_country() for i in general_list]
    value_infected = [i[0][-1] * 100 for i in information_of_countries]
    value_none_infected = [i[1][-1] * 100 for i in information_of_countries]
    value_recovered = [i[2][-1] * 100 for i in information_of_countries]
    lst_bottom_none_infected = [(i[0][-1] + i[2][-1]) * 100 for i in information_of_countries]

    fig, ax = plt.subplots()
    fig.set_size_inches(12, 6)

    ax.bar(labels, value_none_infected, width, bottom=lst_bottom_none_infected, label='None infected', color='blue')
    ax.bar(labels, value_infected, width, bottom=value_recovered, label='Infected', color='red')
    ax.bar(labels, value_recovered, width, label='Recovered', color='green')

    ax.set_ylabel('Percentages')
    ax.set_title('Status by country')
    ax.legend()
    # plt.show()
    return fig


def draw_situation_in_country_bifurcation(results):
    X = []
    Y = []
    for x, y in results.items():
        X.extend([x] * len(y))
        Y.extend([i * 100 for i in y])

    plt.scatter(X, Y)
    plt.show()
