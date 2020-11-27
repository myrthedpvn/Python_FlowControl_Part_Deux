#!/usr/bin/env python

"""
 Bron: https://www.geeksforgeeks.org/difference-between-list-vs-set-vs-tuple-in-python/
 """

# import


__author__ = "Myrthe Diepeveen"
__email__ = "myrthe.diepeveen@student.kdg.be"
__status__ = "Development"


def main():
    # Creating a Set
    set1 = set()
    print("Intial blank Set: ")
    print(set1)

    # Creating a Set with
    # the use of Constructor
    # (Using object to Store String)
    String = 'Christmas'
    set1 = set(String)
    print("\nSet with the use of an Object: ")
    print(set1)

    # Creating a Set with
    # the use of a List
    set1 = set(["Is", "it", "Christmas"])
    print("\nSet with the use of List: ")
    print(set1)

if __name__ == '__main__':  # code to execute if called from command-line
    main()
