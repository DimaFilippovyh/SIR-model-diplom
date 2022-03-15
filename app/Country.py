from constans import length_virus


class Country:
    def __init__(self, name, contacting=0.04, recovered=0.005,
                /, list_of_contacts_country={}):
        self.name = name
        self.status_country = "healthy"
        self.infected_people = [0.0 for i in range(length_virus + 1)]
        self.none_infected_people = [1 for i in range(length_virus + 1)]
        self.recovered_people = [0.0 for i in range(length_virus + 1)]
        self.contacting = contacting
        self.recovered = recovered
        self.list_of_contacts_country = list_of_contacts_country

    def __str__(self):
        return f"""{self.infected_people, self.none_infected_people,
            self.recovered_people, self.contacting, self.recovered}"""

    def __repr__(self):
        return f"""{self.infected_people, self.none_infected_people,
            self.recovered_people, self.contacting, self.recovered}"""

    def situation_in_country(self):
        return [self.name, self.infected_people, self.none_infected_people,
                self.recovered_people, self.contacting, self.recovered]

    def start_viruses(self):
        self.infected_people[-1] = 0.001

    def change_situation(self, lst_param):
        self.infected_people.append(lst_param[0])
        self.none_infected_people.append(lst_param[1])
        self.recovered_people.append(lst_param[2])

    def return_infected_people(self):
        return self.infected_people

    def get_name_country(self):
        return self.name
