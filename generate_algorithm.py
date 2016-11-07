import sys
import numpy as np
import numpy.linalg as la

class Generate:
    # Constructor
    def __init__(self):
        # target
        self.target = np.eye(2)
        # Define Part c Element
        self.PART_C_LINE = 1
        self.PART_C_COLUMN = 0
        # Define Seeds
        self.SIGMA = np.array([[1, 1], [0, 1]])
        self.OMEGA = np.array([[0, 1], [-1, 0]])

    # Method

    # Getter
    def get_target(self):
        return self.target
    # Setter
    def set_target(self, target):
        self.target = target
    # Search
    def proof(self):
        if self.target[0, 0] == 0:
            return self.OMEGA.dot(self.target)
        elif self.target[1, 0] == 0:
            return self.target
        else:
            return self.search()

    # if Part a * Part c != 0
    def search_algorithm(self, target_calc):
        # if |Part a| < |Part c|
        if np.fabs(target_calc[(0, 0)]) < np.fabs(target_calc[(1, 0)]):
            # ω・target_calc
            target_calc = self.OMEGA.dot(target_calc)


        # int((Part a)) // int((Part b))
        quotient = int(target_calc[(0, 0)]) // int(target_calc[(1, 0)])
        # int((Part a)) % int((Part b))
        remainder =  target_calc[(0, 0)] - quotient * target_calc[(1, 0)]

        # if |remainder| > |Part c|
        if remainder < 0:
            # int((Part a)) % int((Part c))
            remainder_inc =  target_calc[(0, 0)] - (quotient + 1) * target_calc[(1, 0)]
            remainder_dec =  target_calc[(0, 0)] - (quotient - 1) * target_calc[(1, 0)]

            if remainder_inc >= 0:
                quotient += 1
                remainder = remainder_inc
            else:
                quotient -= 1
                remainder = remainder_dec

        target_calc = la.matrix_power(self.SIGMA, -1 * int(quotient)).dot(target_calc)
        target_calc = self.OMEGA.dot(target_calc)

        return target_calc

    def search(self):
        target_calc = self.target
        while True:
            print(target_calc)
            input()
            target_calc = self.search_algorithm(target_calc)
            if target_calc[(1, 0)] == 0:
                return target_calc

def main():
    # Define Determinant for ∈ SL(2, Z)
    SL2Z_DET = 1
    # Constract 2 x 2 Identity Matrix
    target = np.eye(2)

    # Input to target
    print("Please set Part a:")
    target[(0, 0)] = float(input())
    print("Please set Part b:")
    target[(0, 1)] = float(input())
    print("Please set Part c:")
    target[(1, 0)] = float(input())
    print("Please set Part d:")
    target[(1, 1)] = float(input())

    # Judge element for SL(2. Z)
    if(int(la.det(target)) == SL2Z_DET):
        print(target)
    else:
        raise ValueError("Input Matrix is not element for SL(2, Z)")

    # Create Instance
    gen = Generate()
    gen.set_target(target)

    # Run Search and Print Result
    print(gen.proof())

if __name__ == '__main__':
    main()
