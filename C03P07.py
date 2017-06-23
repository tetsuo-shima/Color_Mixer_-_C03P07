# Color Mixer
# The colors red, blue, and yellow are known as the primary colors because they
# cannot be made by mixing other colors. When you mix two primary colors, you
# get a secondary color, as shown here:
#   When you mix red and blue, you get purple.
#   When you mix red and yellow, you get orange.
#   When you mix blue and yellow, you get green.
# Design a program that prompts the user to enter the names of two primary
# colors to mix. If the user enters anything other than “red,” “blue,” or
# “yellow,” the program should display an error message. Otherwise, the program
# should display the name of the secondary color that results.

'''
def get_new_color(user_colors):
    if user_colors[0] == user_colors[1]:
        return user_colors[0]

    if 'red' in user_colors:
        if 'blue' in user_colors:
            return 'purple'
        if 'yellow' in user_colors:
            return 'orange'
    if 'blue' in user_colors: #test for blue + yellow
        return 'green'
'''

#investigate frozenset

import colors
import color_validation


def get_new_color(user_colors):
    if user_colors[0] == user_colors[1]:
        return user_colors[0]

    for key, value in colors.MIXED_COLORS.items():
        if user_colors[0] in key and user_colors[1] in key:
            return value

    return "ERROR"


def get_primary_colors():
    user_primary_color_list = []
    print("Primary Color Mixer (Red/Blue/Yellow)")

    for index in range(1,3):
        color = input("Enter primary color " + str(index) + ": ").strip()
        color_validation.validate_primary_color(color)
        user_primary_color_list.append(color)

    return user_primary_color_list


def main():
    user_colors = get_primary_colors()
    print("New color:", get_new_color(user_colors).title())


main()