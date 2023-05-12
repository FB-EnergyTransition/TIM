from user_interaction import input_validation
from csv_conversion import csv_input_validation


def test_validate_bucket_input_valid():
    bucket = 'EXAA Data'
    expected_output = True
    assert input_validation.validate_bucket_input(bucket) == expected_output


def test_validate_bucket_input_invalid():
    bucket = 'helloWorld'
    expected_output = False
    assert input_validation.validate_bucket_input(bucket) == expected_output


def test_validate_option_valid():
    option = "1"
    expected_output = True
    assert input_validation.validate_option(option) == expected_output


def test_validate_option_invalid_3():
    option = "3"
    expected_output = False
    assert input_validation.validate_option(option) == expected_output


def test_validate_option_invalid_exklamation_mark():
    option = "!"
    expected_output = False
    assert input_validation.validate_option(option) == expected_output


def test_validate_unit_option_valid_yes():
    option = "yes"
    expected_result = True
    assert input_validation.validate_unit_option(option) == expected_result


def test_validate_unit_option_invalid_nope():
    option = "nope"
    expected_result = False
    assert input_validation.validate_unit_option(option) == expected_result


def test_check_delimiter_valid():
    infile = '../resources/test.csv'
    expected_result = True
    assert csv_input_validation.check_delimiter(infile) == expected_result


def test_check_delimiter_invalid():
    infile = '../resources/test_delimiter_semikolon.csv'
    expected_result = False
    assert csv_input_validation.check_delimiter(infile) == expected_result


def test_check_input_timeformat_valid():
    infile = '../resources/test.csv'
    expected_result = True
    assert csv_input_validation.check_input_timeformat(infile) == expected_result


def test_check_input_timeformat_invalid():
    infile = '../resources/test_wrong_timeformat.csv'
    expected_result = False
    assert csv_input_validation.check_input_timeformat(infile) == expected_result


def test_check_valid_values_valid():
    infile = '../resources/test.csv'
    expected_result = True
    assert csv_input_validation.check_valid_values(infile) == expected_result


def test_check_valid_values_invalid():
    infile = '../resources/test_invalid_values.csv'
    expected_result = False
    assert csv_input_validation.check_valid_values(infile) == expected_result