#!/usr/bin/env python3

# Created by Dylan Melo
# Created on Jan 2022
# This program gets the user to enter a rectangular
# prism's width, length, and height, and then displays
# the volume of the prism.

def calc_volume(length, width, height):
    volume = width * height * length
    return volume


def main():

    print("Welcome to the rectangular prism volume calculator!")
    while True:
        # get user number as a string
        length = input("Enter your length: ")
        print("")
        width = input("Enter your width: ")
        print("")
        height = input("Enter your height: ")
        print("")
        # Use try catch to prevent invalid entries

        try:
            # converts the first user input to integer
            length_int = float(length)
            width_int = float(width)
            height_int = float(height)

            if length_int < 0:
                print("{} is < 0 and cannot be calculated"
                      .format(length))
                print("")
                continue

            if width_int < 0:
                print("{} is < 0 and cannot be calculated"
                      .format(width_int))
                print("")
                continue

            if height_int < 0:
                print("{} is < 0 and cannot be calculated"
                      .format(height_int))
                print("")
                continue
            # Process/ calculate volume using def

            volume_main = calc_volume(length_int, width_int, height_int)
            print("your volume is: {:.2f}cm³ ". format(volume_main))
            break

        except Exception:
            print("Invalid input")
    print("")
    print("Have a great day!")


if __name__ == "__main__":
    main()
