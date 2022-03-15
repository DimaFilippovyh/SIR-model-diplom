import matplotlib.pyplot as plt


def draw_situation_in_world(lst_country):
    plt.close()
    labels = [i.get_name_country() for i in lst_country[:3]]
    labels.extend([i.get_name_country() + "V2" for i in lst_country[:3]])
    width = 0.35

    information_of_countries = [i.situation_in_country()[1:4]
        for i in lst_country]
    value_infected = [i[0][-1] * 100 for i in information_of_countries]
    value_none_infected = [i[1][-1] * 100 for i in information_of_countries]
    value_recovered = [i[2][-1] * 100 for i in information_of_countries]
    lst_bottom_none_infected = [(i[0][-1] + i[2][-1]) * 100
                                for i in information_of_countries]

    _, ax = plt.subplots()

    ax.bar(labels, value_none_infected, width, bottom=lst_bottom_none_infected,
            label='None infected', color='blue')
    ax.bar(labels, value_infected, width, bottom=value_recovered,
            label='Infected', color='red')
    ax.bar(labels, value_recovered, width, label='Recovered', color='green')

    ax.set_ylabel('Percentages')
    ax.set_title('Status by country')
    ax.legend()

    plt.show()


# _, ax = plt.subplots()
# Russia = Country('Russia')
# Germany = Country('Germany')
# Italy = Country('Italy')
# Russia.start_viruses()
# lst_country = [Russia, Germany, Italy]
# draw_situarion_in_world(lst_country, ax)
# plt.show()
# # Russia = Country('Russia')
# # Germany = Country('Germany')
# # Italy = Country('Italy')
# Russia.start_viruses()
# lst_country = [Russia, Germany, Italy]
# while True:
#     for country in lst_country:
#         proliferation_virus(country)
#     draw_situarion_in_world(lst_country, ax)
# time.sleep(5)


# import matplotlib.pyplot as plt


# labels = ['G1', 'G2', 'G3', 'G4', 'G5']
# men_means = [20, 35, 30, 35, 27]
# women_means = [25, 32, 34, 20, 25]
# men_std = [2, 3, 4, 1, 2]
# women_std = [3, 5, 2, 3, 3]
# width = 0.35       # the width of the bars: can also be len(x) sequence

# fig, ax = plt.subplots()

# ax.bar(labels, men_means, width, yerr=men_std, label='Men')
# ax.bar(labels, women_means, width, yerr=women_std, bottom=men_means,
#        label='Women')

# ax.set_ylabel('Scores')
# ax.set_title('Scores by group and gender')
# ax.legend()

# plt.show()

# def groupedbarplot(x_data, y_data_list, colors, y_data_names="", x_label="",
#  y_label="", title=""):
#     _, ax = plt.subplots()
#     # Total width for all bars at one x location
#     total_width = 0.8
#     # Width of each individual bar
#     ind_width = total_width / len(y_data_list)
#     # This centers each cluster of bars about the x tick mark
#     alteration = np.arange(-(total_width/2), total_width/2, ind_width)

#     # Draw bars, one category at a time
#     for i in range(0, len(y_data_list)-1):
#         # Move the bar to the right on the x-axis so it doesn't
#         # overlap with previously drawn ones
#         ax.bar(x_data + alteration[i], y_data_list[i], color=colors[i],
# label=y_data_names[i], width=ind_width)
#     ax.set_ylabel(y_label)
#     ax.set_xlabel(x_label)
#     ax.set_title(title)
#     ax.legend(loc='upper right')


# groupedbarplot(10, [2, 3, 4], ['red', 'green', 'blue'], ['a', 'b', 'c'])
