#coding: utf-8
import sys
import numpy as np
import numpy.linalg as la
import sl2z
import division as divi

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
        # Show Calc Process(You can print the process)
        self.isshowprocess = False

    # Method

    # Getter
    def get_target(self):
        return self.target

    # Setter
    def set_target(self, target):
        if sl2z.judge_sl2Z(target):
            self.target = target

    def set_isShowProcess(self, isshowprocess):
        self.isshowprocess = bool(isshowprocess)

    # Search
    def proof(self):
        if self.target[0, 0] == 0:
            self.result = self.OMEGA.dot(self.target)
        elif self.target[1, 0] == 0:
            self.result = self.target
        else:
            self.result = self.search_loop()

    # loop algorithm
    def search_loop(self):
        target_calc = self.target

        # Show Calc Process
        if self.isshowprocess:
            print(target_calc)

        while True:
            target_calc = self.search_algorithm(target_calc)

            # Show Calc Process
            if self.isshowprocess:
                print(target_calc)

            if target_calc[(1, 0)] == 0:
                return target_calc

    # if Part a * Part c != 0
    def search_algorithm(self, target_calc):
        # if |Part a| < |Part c|
        if np.fabs(target_calc[(0, 0)]) < np.fabs(target_calc[(1, 0)]):
            # ω・target_calc
            target_calc = self.OMEGA.dot(target_calc)

        # Part a // Part c, Part a % Part c
        division = divi.euclidean(target_calc[0, 0], target_calc[1, 0])

        # ω・σ^(-quotient)・target_calc
        target_calc = self.OMEGA.dot(la.matrix_power(self.SIGMA, -1 * division["quotient"]).dot(target_calc))

        return target_calc
