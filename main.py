# from input_params import input_params
from csv_conversion import csv_conversion_main
from user_interaction import welcome_screen, option_handling

# infile = './resources/test.csv'


def main():
    welcome_screen.print_welcome_screen()
    option_handling.print_options()
    option = option_handling.get_option()

    args = option_handling.execute_option_and_get_args(option)
    infile = args[0]
    # bucket = args[1]
    unit_s = args[2]

    csv_conversion_main.convert_csv(infile, unit_s)



if __name__ == "__main__":
    main()
