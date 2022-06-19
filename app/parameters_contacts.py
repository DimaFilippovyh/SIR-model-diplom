def get_interaction_parameters(number_situation):
    if number_situation == 1:
        # фигура 1
        parameters_c_r = {
            'China': [0.04, 0.005],
            'Germany': [0.035, 0.006],
            'Italy': [0.02, 0.006],
            'Russia': [0.025, 0.006],
            'Kazakhstan': [0.015, 0.01]}
        parameters_interaction = {
            'China': {'Germany': 0.006, 'Italy': 0.0,
                'Russia': 0.0, 'Kazakhstan': 0.0},
            'Germany': {'China': 0.006, 'Italy': 0.006,
                'Russia': 0.004, 'Kazakhstan': 0.0035},
            'Italy': {'Germany': 0.006, 'China': 0.0,
                'Russia': 0.001, 'Kazakhstan': 0.0005},
            'Russia': {'Germany': 0.004, 'China': 0.0,
                'Italy': 0.001, 'Kazakhstan': 0.001},
            'Kazakhstan': {'Germany': 0.0035, 'China': 0.0,
                'Italy': 0.0005, 'Russia': 0.001}}
    elif number_situation == 2:
        # фигура 2 цикл
        parameters_c_r = {
            'China': [0.04, 0.005],
            'Germany': [0.04, 0.005],
            'Italy': [0.04, 0.005],
            'Russia': [0.04, 0.005],
            'Kazakhstan': [0.04, 0.005]}
        parameters_interaction = {
            'China': {'Germany': 0.006, 'Italy': 0.0,
                'Russia': 0.0, 'Kazakhstan': 0.0},
            'Germany': {'China': 0.0, 'Italy': 0.006,
                'Russia': 0.0, 'Kazakhstan': 0.0},
            'Italy': {'Germany': 0.0, 'China': 0.0,
                'Russia': 0.006, 'Kazakhstan': 0.0},
            'Russia': {'Germany': 0.0, 'China': 0.0,
                'Italy': 0.0, 'Kazakhstan': 0.006},
            'Kazakhstan': {'Germany': 0.0, 'China': 0.006,
                'Italy': 0.0, 'Russia': 0.0}}

    return parameters_c_r, parameters_interaction
