from os import path

from user_interaction import get_user_input_params


def validate_unit_input(option):
    if option == "Y" or option == "N" \
            or option == "YES" or option == "NO" \
            or option == "y" or option == "n" \
            or option == "yes" or option == "no":
        pass
    else:
        get_user_input_params.print_invalid_answer()
        validate_unit_input(get_user_input_params.ask_for_units())


def validate_input_csv_path(csv_path):
    if not path.exists(csv_path):
        print("Path not found")
        valid = False
    elif not csv_path.endswith('.csv'):
        print("Not a csv file")
        valid = False
    else:
        valid = True
    return valid


def validate_bucket_input():
    pass