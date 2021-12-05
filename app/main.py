from spread_virus_by_country import spread_virus_by_country
from Country import Country


def main():
    Russia = Country('Russia', contacting=0.07, recovered=0.005)
    Germany = Country('Germany', contacting=0.02, recovered=0.007)
    Italy = Country('Italy', contacting=0.03, recovered=0.006)

    Russia.start_viruses()
    Germany.start_viruses()
    Italy.start_viruses()
    lst_country = [Russia, Germany, Italy]
    spread_virus_by_country(lst_country)


if __name__ == "__main__":
    main()
