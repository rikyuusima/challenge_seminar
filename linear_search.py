#coding: utf-8
import sys
import numpy as np
from generate_algorithm import Generate
import sl2z

def main():
    # Constract 2 x 2 Identity Matrix
    target = np.eye(2)

    # Create Instance
    gen = Generate()
    # List Initialization and (Min ~ Max) of Linear Search 
    list_size = 0
    SEARCH_MAX = 10
    SEARCH_MIN = 1
    # Linear Search for 1 ~ 10
    for i in range(SEARCH_MIN, SEARCH_MAX + 1):
        for j in range(SEARCH_MIN, SEARCH_MAX + 1):
            for k in range(SEARCH_MIN, SEARCH_MAX + 1):
                for l in range(SEARCH_MIN, SEARCH_MAX + 1):
                    target[(0, 0)] = i
                    target[(0, 1)] = j
                    target[(1, 0)] = k
                    target[(1, 1)] = l
                    # Judge element of SL(2, Z)
                    if sl2z.judge_sl2Z(target) == True :
                        print("----------------------")
                        print(target)
                        print("----------------------")
                        # Set and Judge element of SL(2, Z)
                        gen.set_target(target)
                        gen.set_isShowProcess(True)
                        # Run Search
                        gen.proof()
                        #  Print Result
                        print("result:")
                        print(gen. get_result())
                        # Judge List largest
                        if len(gen.get_exp_seed_matrix()) > list_size:
                            list_size = len(gen.get_exp_seed_matrix())
                            list_data = gen.get_exp_i_seed_matrix()[:]
                        # Judge loop final
                        if i == SEARCH and j == SEARCH and k == SEARCH and l == SEARCH:
                            for matrix in list_data:
                                if matrix['type'] == 'omega':
                                    sys.stdout.write('ω ^ ' + str(matrix['exp']))
                                elif matrix['type'] == 'sigma':
                                    sys.stdout.write('σ ^ ' + str(matrix['exp']))
                                sys.stdout.write(' ')
                            print("")

if __name__ == '__main__':
    main()
