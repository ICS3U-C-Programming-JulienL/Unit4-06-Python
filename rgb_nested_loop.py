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
    counter_red = 0
    counter_green = 0
    counter_blue = 0

    # if the user wants to start, then begin the loops
    if start_RGB == "yes":
        # use a for loop to get all values for red
        for counter_red in range(0, 256, 1):
            # use a for loop to get all values for green
            for counter_green in range(0, 256, 1):
                # use a for loop to get all values for blue
                for counter_blue in range(0, 256, 1):
                    # display colours
                    print(
                        "\033[38;2;{0};{1};{2}mRGB({0}, {1}, {2})\033[0m".format(
                            counter_red, counter_green, counter_blue
                        )
                    )
    else:
        # otherwise, thank the user for playing
        print("Thanks for playing.")


if __name__ == "__main__":
    main()
