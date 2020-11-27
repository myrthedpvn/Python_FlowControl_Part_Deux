#!/usr/bin/env python

"""
 Vraag de gebruiker om een nummer.
 Afhankelijk van het feit of het nummer even of oneven is, print dan een passend bericht uit naar de gebruiker.
 """


__author__ = "Myrthe Diepeveen"
__email__ = "myrthe.diepeveen@student.kdg.be"
__status__ = "Development"


def main():
    try:
        number = int(input("Give me a random number.\n"))
        if (number % 2) == 0:
            print(f"It is", str(number), "an even number.")
        else:
           print(f" It is", str(number), "an odd number.")
    except ValueError as err:
        print("That was not a valid number:", err)


if __name__ == '__main__':
    main()
