from constans import length_virus


class Country:
    def __init__(self, name, contacting=0.04, recovered=0.005, /, list_of_contacts_country={}):
        self.__name = name
        self.__infected_people = [0.0 for i in range(length_virus + 1)]
        self.__none_infected_people = [1.0 for i in range(length_virus + 1)]
        self.__recovered_people = [0.0 for i in range(length_virus + 1)]
        self.__contacting = contacting
        self.__recovered = recovered
        self.__list_of_contacts_country = list_of_contacts_country

    def __str__(self):
        return f"""{self.__infected_people, self.__none_infected_people,
            self.__recovered_people, self.__contacting, self.__recovered}"""

    def __repr__(self):
        return f"""{self.__infected_people, self.__none_infected_people,
            self.__recovered_people, self.__contacting, self.__recovered}"""

    def get_situation_in_country(self):
        return [self.__infected_people, self.__none_infected_people,
            self.__recovered_people]

    def get_parameters_country(self):
        return [self.__contacting, self.__recovered]

    def start_viruses(self):
        self.__infected_people[-1] = 0.001
        self.__none_infected_people[-1] = 1.0 - 0.001

    def change_situation(self, lst_param):
        self.__infected_people.append(lst_param[0])
        self.__none_infected_people.append(lst_param[1])
        self.__recovered_people.append(lst_param[2])

    @property
    def infected_people(self):
        return self.__infected_people[-1]

    @property
    def name(self):
        return self.__name

    @property
    def contacts_country(self):
        return self.__list_of_contacts_country

    @classmethod
    def normalize_solution(cls, lst_param):
        for i, p in enumerate(lst_param):
            if p < 0:
                lst_param[i] = 0
            if p > 1:
                lst_param[i] = 1
        return lst_param
