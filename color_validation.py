import colors


def validate_primary_color(color):
    if color not in colors.PRIMARY_COLORS:
        print("Error: Color entered is not a primary color.\nExiting...")
        exit()