import numpy as np
import numpy.linalg as la

# Judge element for SL(2, Z)
def judge_sl2Z(matrix):
    # Define Determinant for ∈ SL(2, Z)
    SL2Z_DET = 1

    if int(np.round(la.det(matrix))) == SL2Z_DET:
        return True
    else:
        return False
