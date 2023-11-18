#!/usr/bin/env python3

# Created By: Julien Lamoureux
# Date: November 13, 2023
# This program displays all valid RGB color codes


def main():
    # ask the user if they would like to start
    start_RGB = input(
        "This program displays all valid RGB color codes. Do you want to begin (yes/no)?"
    )

    # define counters for red, green, and blue
    counterRed = 0
    counterGreen = 0
    counterBlue = 0

    # if the user wants to start, then begin the loops
    if start_RGB == "yes":
        # use a for loop to get all values for red
        for counterRed in range(0, 256, 1):
            # use a for loop to get all values for green
            for counterGreen in range(0, 256, 1):
                # use a for loop to get all values for blue
                for counterBlue in range(0, 256, 1):
                    # display colours
                    print(
                        "\033[38;2;{0};{1};{2}mRGB({0}, {1}, {2})\033[0m".format(
                            counterRed, counterGreen, counterBlue
                        )
                    )
    else:
        # otherwise, thank the user for playing
        print("Thanks for playing.")


if __name__ == "__main__":
    main()
