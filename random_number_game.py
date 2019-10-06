#!/usr/bin/env python3

# Created by: Wajd Mariam
# Created on: September 2019
# This is a number guessing program

import random


def main():

    random_number = random.randint(1, 10)

    # input
    number = int(input("Can you guess the number computer chose from 0-10"))

    # process
    if (number == random_number):
        print("You guessed it :)")
    else:
        print("You couldn't guess it :(")


if __name__ == main():
    main()
