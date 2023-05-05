from csv_conversion import csv_conversion_main
from user_interaction import welcome_and_end, option_handling
from upload import upload_to_db, file_handling


def main():
    welcome_and_end.print_welcome_screen()
    option_handling.print_options()
    option = option_handling.get_option()

    args = option_handling.execute_option_and_get_args(option)
    infile = args[0]
    measurement = args[1]
    bucket = args[2]
    unit_s = args[3]

    csv_conversion_main.convert_csv(infile, unit_s)
    converted_csvs = file_handling.get_all_converted_csvs()

    for file in converted_csvs:
        upload_to_db.upload_data(file, bucket, measurement)
        welcome_and_end.print_successful_upload(file)

    welcome_and_end.print_end_program()







if __name__ == "__main__":
    main()
