#coding: utf-8
import numpy as np
from generate_algorithm import Generate

def main():
    # Constract 2 x 2 Identity Matrix
    target = np.eye(2)

    # Input target
    print("Please set Part a:")
    target[(0, 0)] = float(input())
    print("Please set Part b:")
    target[(0, 1)] = float(input())
    print("Please set Part c:")
    target[(1, 0)] = float(input())
    print("Please set Part d:")
    target[(1, 1)] = float(input())

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
