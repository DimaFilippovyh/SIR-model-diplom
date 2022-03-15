from spread_virus_by_country import spread_virus_by_country
from Country import Country


def main():
    contacting_R, recovered_R = 0.04, 0.005
    contacting_G, recovered_G = 0.02, 0.007
    contacting_I, recovered_I = 0.03, 0.006

    Russia = Country('Russia', contacting_R, recovered_R)
    Germany = Country('Germany', contacting_G, recovered_G)
    Italy = Country('Italy', contacting_I, recovered_I)

    Russia_with_countrys = Country('Russia', contacting_R, recovered_R,
        {'Germany': 0.012, 'Italy': 0.006})
    Germany_with_countrys = Country('Germany', contacting_G, recovered_G,
        {'Russia': 0.012, 'Italy': 0.006})
    Italy_with_countrys = Country('Italy', contacting_I, recovered_I,
        {'Germany': 0.006, 'Russia': 0.006})

    Russia.start_viruses()
    Germany.start_viruses()
    Italy.start_viruses()

    Russia_with_countrys.start_viruses()
    Germany_with_countrys.start_viruses()
    Italy_with_countrys.start_viruses()

    lst_country = [Russia, Germany, Italy,
        Russia_with_countrys, Germany_with_countrys, Italy_with_countrys]
    spread_virus_by_country(lst_country)


if __name__ == "__main__":
    main()
