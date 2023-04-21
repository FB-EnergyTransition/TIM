from input_params import input_params


def test_existing_and_valid_csv_path():
    path = '../resources/test.csv'
    expected_output = True
    assert input_params.validate_csv_path(path) == expected_output

def test_non_existing_csv_path():
    path = '../resources/test2000.csv'
    expected_output = False
    assert input_params.validate_csv_path(path) == expected_output

def test_invalid_file_type_csv():
    path = '../resources/test.txt'
    expected_output = False
    assert input_params.validate_csv_path(path) == expected_output

