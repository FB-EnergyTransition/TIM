from csv_conversion import csv_conversion_main
from user_interaction import welcome_and_end, option_handling
from upload import upload_to_db, file_handling
from logdata import logdata
import time


def main():
    welcome_and_end.print_welcome_screen()

    while True:
        try:
            option_handling.print_options()
            option = option_handling.get_option()
            args = option_handling.execute_option_and_get_args(option)
            infile = args[0]
            measurement = args[1]
            bucket = args[2]
            unit_s = args[3]

            start_time_conversion = time.time()
            csv_conversion_main.convert_csv(infile, unit_s)
            converted_csvs = file_handling.get_all_converted_csvs(infile)
            end_time_conversion = time.time()-start_time_conversion

            start_time_upload = time.time()
            for file in converted_csvs:
                upload_to_db.upload_data(infile, file, bucket, measurement)
                welcome_and_end.print_successful_upload(file)
            end_time_upload = time.time()-start_time_upload

            print("\n\nThe program needed {} seconds to convert the data\n".format(round(end_time_conversion, 2)))
            print("The program needed {} seconds to upload the data\n\n".format(round(end_time_upload, 2)))
            welcome_and_end.print_end_program()
            break

        except Exception as e:
            logdata.error_message(e)
            continue


if __name__ == "__main__":
    main()
