import pytest
from csv_conversion import time_reformatting, read_write_csv, check_amount_of_measurements


def test_reformat_time_1():
    input = '01.01.2018 00:00:00'
    expected_output = '2018-01-01T00:00:00.000Z'

    assert time_reformatting.reformat_time(input) == expected_output


def test_reformat_time_2():
    input = '23.04.2023 02:05:44'
    expected_output = '2023-04-23T02:05:44.000Z'

    assert time_reformatting.reformat_time(input) == expected_output


@pytest.fixture
def inputcsv():
    return '../resources/test.csv'
@pytest.fixture()
def outputcsv():
    return '../resources/test_formatted.csv'


def test_convert_row():

    infile = '../resources/test.csv'
    row = ['01.01.2018 00:00:00', '-6.00', '', '']
    rowlist = [['', '', 0, '2018-01-01T00:15:00.000Z', '2018-01-01T04:00:00.000Z',
                '2018-01-01T00:00:00.000Z', '-6.00', 'EUR/kWh',
                'Preis EXAA 10:15 Auktion']]

    assert read_write_csv.convert_row(0, row, ['2018-01-01T00:15:00.000Z',
                                      '2018-01-01T04:00:00.000Z'],
                                      infile) == rowlist


def test_get_measurement_name():
    infile = '../resources/test.csv'
    expected_result = "Preis EXAA 10:15 Auktion"
    assert read_write_csv.get_measurement_name(infile) == expected_result


def test_get_number_of_columns():
    infile = '../resources/test.csv'
    expected_result = 2
    assert check_amount_of_measurements.get_number_of_measurements(infile) == expected_result


def test_check_if_splitting_is_needed():
    infile = '../resources/test.csv'
    expected_result = True
    assert check_amount_of_measurements.check_if_splitting_is_needed(infile) == expected_result
