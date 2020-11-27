#!/usr/bin/env python

"""
Bron: https://www.geeksforgeeks.org/difference-between-list-vs-set-vs-tuple-in-python/
"""

# import


__author__ = "Myrthe Diepeveen"
__email__ = "myrthe.diepeveen@student.kdg.be"
__status__ = "Development"


def main():
    # Creating an empty Tuple
    Tuple1 = ()
    print("Initial empty Tuple: ")
    print(Tuple1)

    # Creating a Tuple with
    # the use of list
    list1 = [1, 2, 4, 5, 6]
    print("\nTuple using List: ")
    print(tuple(list1))

    # Creating a Tuple
    # with the use of built-in function
    Tuple1 = tuple('Christmas')
    print("\nTuple with the use of function: ")
    print(Tuple1)

if __name__ == '__main__':  # code to execute if called from command-line
    main()
