#coding: utf-8
import sys
import numpy as np
from generate_algorithm import Generate

def main():
    # Constract 2 x 2 Identity Matrix
    target = np.eye(2)

    argc = len(sys.argv)
    # if argument is greater than 1
    if argc > 1:
        target[(0, 0)] = float(sys.argv[1])
    else:
        # Input target
        print("Please set Part a:")
        target[(0, 0)] = float(input())
        print("Please set Part b:")
        target[(0, 1)] = float(input())
        print("Please set Part c:")
        target[(1, 0)] = float(input())
        print("Please set Part d:")
        target[(1, 1)] = float(input())
    if argc > 2:
        target[(0, 1)] = float(sys.argv[2])
    if argc > 3:
        target[(1, 0)] = float(sys.argv[3])
    if argc > 4:
        target[(1, 1)] = float(sys.argv[4])

    # Create Instance
    gen = Generate()
    # Set and Judge element of SL(2, Z)
    gen.set_target(target)

    # Run Search
    gen.proof()
    #  Print Result
    print(gen.result)

if __name__ == '__main__':
    main()
