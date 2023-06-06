import time

import csv_conversion.csv_conversion_main
import upload.upload_to_db
import upload.file_handling
import user_interaction.get_user_input_params
import user_interaction.welcome_and_end
from csv_conversion import csv_conversion_main
from logdata import logdata
from user_interaction import option_handling


def main():
    pr = user_interaction.welcome_and_end.Printer()
    params = user_interaction.get_user_input_params.InputParams()
    oh = user_interaction.option_handling.OptionHandler(params)
    pr.print_welcome_screen()

    while True:
        try:
            pr.print_options()
            option = oh.get_option()
            oh.execute_option_and_get_args(option)
            #infile = args[0]
            #measurement = args[1]
            #bucket = args[2]
            #unit_s = args[3]

            start_time_conversion = time.time()
            csvc = csv_conversion.csv_conversion_main.CsvConverter(params.infile, params.units)
            csvc.convert_csv()

            fh = upload.file_handling.FileHandler(params.infile)

            converted_csvs = fh.get_all_converted_csvs()
            end_time_conversion = time.time()-start_time_conversion

            start_time_upload = time.time()

            for file in converted_csvs:
                uploader = upload.upload_to_db.\
                    Uploader(params.infile, file, params.bucket, params.measurement)
                uploader.upload_data()
                pr.print_successful_upload(file)
            end_time_upload = time.time()-start_time_upload

            print("\n\nThe program needed {} seconds to convert the data"
                  .format(round(end_time_conversion, 2)))
            print("The program needed {} seconds to upload the data\n\n"
                  .format(round(end_time_upload, 2)))
            pr.print_end_program()
            break

        except Exception as e:
            logdata.error_message(e)
            continue


if __name__ == "__main__":
    main()
