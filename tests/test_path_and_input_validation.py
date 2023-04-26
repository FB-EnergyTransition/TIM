from csv_conversion import outfile_validation
from user_interaction import input_validation


def test_check_existing_outfile_1():
    outfile = '../resources/test.csv'
    expected_result = True
    assert outfile_validation.check_existing_outfile(outfile) == expected_result


def test_check_existing_outfile_2():
    outfile = '../resources/test2.csv'
    expected_result = False
    assert outfile_validation.check_existing_outfile(outfile) == expected_result


def test_check_measurement_name_1():
    measurement = 'test: Preis'
    expected_result = 'test Preis'
    assert outfile_validation.check_measurement_name(measurement) == expected_result


def test_check_measurement_name_2():
    measurement = 'Me/asuremen?t'
    expected_result = 'Measurement'
    assert outfile_validation.check_measurement_name(measurement) == expected_result


def test_existing_and_valid_csv_path():
    path = '../resources/test.csv'
    expected_output = True
    assert input_validation.validate_input_csv_path(path) == expected_output


def test_non_existing_csv_path():
    path = '../resources/test2000.csv'
    expected_output = False
    assert input_validation.validate_input_csv_path(path) == expected_output


def test_invalid_file_type_csv():
    path = '../resources/test.txt'
    expected_output = False
    assert input_validation.validate_input_csv_path(path) == expected_output


def test_validate_bucket_input_1():
    bucket = 'EXAA Data'
    expected_output = True
    assert input_validation.validate_bucket_input(bucket) == expected_output


def test_validate_bucket_input_2():
    bucket = 'helloWorld'
    expected_output = False
    assert input_validation.validate_bucket_input(bucket) == expected_output


def test_validate_option_1():
    option = "1"
    expected_output = True
    assert input_validation.validate_option(option) == expected_output


def test_validate_option_2():
    option = "3"
    expected_output = False
    assert input_validation.validate_option(option) == expected_output
