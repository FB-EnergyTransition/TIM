import csv_conversion
from csv_conversion import readcsv
def test_reformat_time_1():
    input = '01.01.2018 00:00:00'
    expected_output = '2018-01-01T00:00:00.000Z'

    assert csv_conversion.readcsv.reformattime(input) == expected_output

def test_reformat_time_2():
    input = '23.04.2023 02:05:44'
    expected_output = '2023-04-23T02:05:44.000Z'

    assert csv_conversion.readcsv.reformattime(input) == expected_output