def get_interaction_parameters(number_situation):
    if number_situation == 1:
        # фигура 1
        pass
        # TODO: add
    elif number_situation == 2:
        # фигура 2 цикл
        parameters_c_r = {
            'Russia': [0.04, 0.005],
            'Germany': [0.04, 0.005],
            'Italy': [0.04, 0.005],
            'Serbia': [0.04, 0.005],
            'Kazakhstan': [0.04, 0.005]}
        parameters_interaction = {
            'Russia': {'Germany': 0.006, 'Italy': 0.0,
                'Serbia': 0.0, 'Kazakhstan': 0.0},
            'Germany': {'Russia': 0.0, 'Italy': 0.006,
                'Serbia': 0.0, 'Kazakhstan': 0.0},
            'Italy': {'Germany': 0.0, 'Russia': 0.0,
                'Serbia': 0.006, 'Kazakhstan': 0.0},
            'Serbia': {'Germany': 0.0, 'Russia': 0.0,
                'Italy': 0.0, 'Kazakhstan': 0.006},
            'Kazakhstan': {'Germany': 0.0, 'Russia': 0.006,
                'Italy': 0.0, 'Serbia': 0.0}}

    return parameters_c_r, parameters_interaction
