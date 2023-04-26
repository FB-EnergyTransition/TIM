from user_interaction import get_user_input_params


def print_options():
    print("""
    Please chose an option:

    1 - Upload data from CSV
    2 - Read CSV Requirements
    """)


def get_option():
    return input()


def validate_option(option):
    if option == "1" or option == "2":
        pass
    else:
        print_invalid_option()
        print_options()
        validate_option(get_option())


def print_invalid_option():
    print("Invalid option. Please chose 1 oder 2.")


def print_csv_requirements():
    print("""
    These are the requirements a CSV file has to fulfill
    in order to be uploaded into the InfluxDB:
    
    **********************************************************
    1. Delimiter of csv file has to be ','.
    2. Decimal separator of values has to be '.'.
    3. Timestamps have to and can only be in the first column.
    4. Timestamps have to be in format "dd.MM.YYYY HH:mm:ss".
    5. Value columns start from the second column.
    6. Value columns can only contain valid values.
    7. Headers of the columns should contain the name of the
    measurements/values.
    **********************************************************
    """)


def execute_option_and_get_args(option):
    validate_option(option)
    if option == "1":
        args = get_user_input_params.ask_for_parameters()
    else:
        print_csv_requirements()
        print_options()
        execute_option_and_get_args(get_option())
        args = []
    return args
