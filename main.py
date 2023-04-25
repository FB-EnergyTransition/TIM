# from input_params import input_params
from csv_conversion import csv_conversion_main
from user_interaction import welcome_screen, option_handling

infile = './resources/test.csv'


def main():
    welcome_screen.print_welcome_screen()
    option_handling.print_options()
    option = option_handling.get_option()
    option_handling.execute_option(option)


    # args = input_params.process_input_params()
    csv_conversion_main.convert_csv(infile)
    # print(args)


if __name__ == "__main__":
    main()
