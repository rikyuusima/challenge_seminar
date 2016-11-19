#coding: utf-8
import sys
import numpy as np
import numpy.linalg as la

# Judge element for SL(2. Z)
def judge_sl2Z(matrix):
    # Define Determinant for ∈ SL(2, Z)
    SL2Z_DET = 1

    if(int(la.det(matrix)) == SL2Z_DET):
        return True
    else:
        raise ValueError("Input matrix is not element of SL(2, Z)")


# calced by euclidean_division
def euclidean_division(dividend, divisor):
    # calc division
    quotient = int(dividend) // int(divisor)
    # calc remainder
    remainder =  dividend - quotient * divisor

    if remainder < 0:
        # calc remainder
        remainder_inc =  dividend - (quotient + 1) * divisor
        remainder_dec =  dividend - (quotient - 1) * divisor

        if remainder_inc >= 0:
            quotient += 1
            remainder = remainder_inc
        else:
            quotient -= 1
            remainder = remainder_dec

    return {"quotient": int(quotient),
            "remainder": int(remainder)}

class Generate:
    # Constructor
    def __init__(self):
        # target
        self.target = np.eye(2)
        # result
        self.result = np.eye(2)
        # Define Seeds
        self.SIGMA = np.array([[1, 1], [0, 1]])
        self.OMEGA = np.array([[0, 1], [-1, 0]])

    # Method

    # Getter
    def get_target(self):
        return self.target
    # Setter
    def set_target(self, target):
        if judge_sl2Z(target):
            self.target = target
    # Search
    def proof(self):
        if self.target[0, 0] == 0:
            result = self.OMEGA.dot(self.target)
        elif self.target[1, 0] == 0:
            result = self.target
        else:
            result = self.search_loop()

    # loop algorithm
    def search_loop(self):
        target_calc = self.target
        while True:
            print(target_calc)
            target_calc = self.search_algorithm(target_calc)
            if target_calc[(1, 0)] == 0:
                return target_calc

    # if Part a * Part c != 0
    def search_algorithm(self, target_calc):
        # if |Part a| < |Part c|
        if np.fabs(target_calc[(0, 0)]) < np.fabs(target_calc[(1, 0)]):
            # ω・target_calc
            target_calc = self.OMEGA.dot(target_calc)

        # Part a // Part c, Part a % Part c
        division = euclidean_division(target_calc[0, 0], target_calc[1, 0])

        # ω・σ^(-quotient)・target_calc
        target_calc = self.OMEGA.dot(la.matrix_power(self.SIGMA, -1 * division["quotient"]).dot(target_calc))

        return target_calc
