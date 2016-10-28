import sys
import numpy as np
import numpy.linalg as la

class Generate:
    # Constructor
    def __init__(self):
        # target
        self.target = np.eye(2)
        # define search element
        self.TARGET_LINE = 1
        self.TARGET_COLUMN = 0
        # power
        self.power = 0
        # Define Seeds
        self.SIGMA = np.array([[1, 1], [0, 1]])
        self.OMEGA = np.array([[0, 1], [-1, 0]])
        # result
        self.result = []

    # Method

    # Getter
    def get_target(self):
        return self.target
    def get_power(self):
        return self.power
    # Setter
    def set_target(self, target):
        self.target = target
    def set_power(self, power):
        self.power = power + 1
    # target^power
    def power_matrix(self, target, power):
        if power > 0:
            return target.dot(self.power_matrix(target, power - 1))
        elif power == 0:
            # 2 x 2 identity matrix
            return np.eye(2)
    # Search
    def search(self):
        for i in range(0, self.power):
            for j in range(0, self.power):
                for k in range(0, self.power):
                    for l in range(0, self.power):
                        # SIGMA^i dot OMEGA^j dot SIGMA.I^k dot OMEGA.I^l dot target
                        result = self.power_matrix(self.SIGMA, i).dot(self.power_matrix(self.OMEGA, j).dot(self.power_matrix(la.inv(self.SIGMA), k).dot(self.power_matrix(la.inv(self.OMEGA), l).dot(self.target))))
                        if result[self.TARGET_LINE, self.TARGET_COLUMN] == 0.0:
                            self.result = [i, j, k, l]
                            return
        raise ValueError("Not found by " + str(self.power - 1) +".")

def main():
    TARGET = np.array([[2, 1], [5, 3]])
    SIGMA = np.array([[1, 1], [0, 1]])
    OMEGA = np.array([[0, 1], [-1, 0]])

    # Import power from argument
    argc = len(sys.argv)
    if argc == 2:
        POWER = int(sys.argv[1])
    else:
        POWER = 10

    # Create Instance
    gen = Generate()
    gen.set_target(TARGET)
    gen.set_power(POWER)

    # Run Search
    gen.search()
    #print(gen.power_matrix(SIGMA, POWER))
    print("i: " + str(gen.result[0]) + "\nj: " + str(gen.result[1]) + "\nk: " + str(gen.result[2]) + "\nl: " + str(gen.result[3]))

if __name__ == '__main__':
    main()
