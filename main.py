from csv_conversion import csv_conversion_main
from user_interaction import welcome_screen, option_handling
from upload import upload_to_db

# infile = './resources/test.csv'


def main():
    welcome_screen.print_welcome_screen()
    option_handling.print_options()
    option = option_handling.get_option()

    args = option_handling.execute_option_and_get_args(option)
    infile = args[0]
    measurement = args[1]
    bucket = args[2]
    unit_s = args[3]

    csv_conversion_main.convert_csv(infile, unit_s)
    print(bucket)
    converted = './resources/test_Preis MC Auktion_formatted_neu.csv'

    upload_to_db.upload_data(converted, bucket, measurement)


if __name__ == "__main__":
    main()
