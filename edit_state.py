import numpy as np


def edit_state(s1, s2, s3):
    state = list()
    for value in s1.values:
        state.append(value)
    for value in s2.values:
        state.append(value)
    for value in s3:
        state.append(value)

    state = np.array(state)
    return state