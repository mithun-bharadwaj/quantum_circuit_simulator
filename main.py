import numpy as np


# Return vector of size 2**num_qubits with all zeroes except first element which is 1
def get_ground_state(num_qbits):
    assert  num_qbits > 0, "Number of qbits specified should be greater than 0"
    ground_state = np.zeros((2*num_qbits))
    ground_state[0] = 1
    return ground_state


if __name__ == '__main__':
    print(get_ground_state(0))
