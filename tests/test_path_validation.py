import csv_conversion.outfile_validation
from csv_conversion import outfile_validation
import user_interaction.input_validation


def test_validate_input_csv_path_non_existing_csv_path():
    path = '../resources/test_resources/test2000.csv'
    expected_output = False
    iv = user_interaction.input_validation.InputValidator()
    assert iv.validate_input_csv_path(path) == expected_output


def test_validate_input_csv_path_invalid_file_type_csv():
    path = '../resources/test_resources/test.txt'
    expected_output = False
    iv = user_interaction.input_validation.InputValidator()
    assert iv.validate_input_csv_path(path) == expected_output


def test_validate_input_csv_path_valid():
    path = '../resources/test_resources/test.csv'
    expected_output = True
    iv = user_interaction.input_validation.InputValidator()
    assert iv.validate_input_csv_path(path) == expected_output


def test_check_existing_outfile_valid():
    outfile = '../resources/test_resources/test.csv'
    expected_result = True
    ov = csv_conversion.outfile_validation.OutfileValidator()
    assert ov.check_existing_outfile(outfile) == expected_result


def test_check_existing_outfile_invalid():
    outfile = '../resources/test_resources/test2.csv'
    expected_result = False
    ov = csv_conversion.outfile_validation.OutfileValidator()
    assert ov.check_existing_outfile(outfile) == expected_result


def test_check_measurement_name_incl_colon():
    measurement = 'test: Preis'
    expected_result = 'test Preis'
    ov = csv_conversion.outfile_validation.OutfileValidator()
    assert ov.check_measurement_name(measurement) == expected_result


def test_check_measurement_name_incl_slash_question_mark():
    measurement = 'Me/asuremen?t'
    expected_result = 'Measurement'
    ov = csv_conversion.outfile_validation.OutfileValidator()
    assert ov.check_measurement_name(measurement) == expected_result


def test_check_measurement_name_already_valid():
    measurement = 'Preis MC Auktion'
    expected_result = 'Preis MC Auktion'
    ov = csv_conversion.outfile_validation.OutfileValidator()
    assert ov.check_measurement_name(measurement) == expected_result







