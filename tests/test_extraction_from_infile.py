import csv_conversion.check_amount_of_measurements
from csv_conversion import read_write_csv, check_amount_of_measurements


def test_get_measurement_name_Preis_EXAA_10_15_Auktion():
    infile = '../resources/test_resources/test.csv'
    measurement_number = 1
    expected_result = "Preis EXAA 10:15 Auktion"
    csvrw = csv_conversion.read_write_csv.CsvReaderWriter(infile)
    assert csvrw.get_measurement_name(measurement_number)\
           == expected_result


def test_get_measurement_name_CHR_2():
    infile = '../resources/test_resources/test_loadprofiles.csv'
    measurement_number = 2
    expected_result = "CHR_2"
    csvrw = csv_conversion.read_write_csv.CsvReaderWriter(infile)
    assert csvrw.get_measurement_name(measurement_number)\
           == expected_result


def test_get_number_of_measurements_2():
    infile = '../resources/test_resources/test.csv'
    expected_result = 2
    mh = csv_conversion.check_amount_of_measurements.MeasurementHandler(infile)
    assert mh.get_number_of_measurements() == expected_result


def test_get_number_of_measurements_5():
    infile = '../resources/test_resources/test_loadprofiles.csv'
    expected_result = 5
    mh = csv_conversion.check_amount_of_measurements.MeasurementHandler(infile)
    assert mh.get_number_of_measurements() == expected_result


def test_get_number_of_measurements_1():
    infile = '../resources/test_resources/test_only_one_value.csv'
    expected_result = 1
    mh = csv_conversion.check_amount_of_measurements.MeasurementHandler(infile)
    assert mh.get_number_of_measurements() == expected_result


def test_check_if_splitting_is_needed_valid_test_csv():
    infile = '../resources/test_resources/test.csv'
    expected_result = True
    mh = csv_conversion.check_amount_of_measurements.MeasurementHandler(infile)
    assert mh.check_if_splitting_is_needed() == expected_result


def test_check_if_splitting_is_needed_valid_test_loadprofiles_csv():
    infile = '../resources/test_resources/test_loadprofiles.csv'
    expected_result = True
    mh = csv_conversion.check_amount_of_measurements.MeasurementHandler(infile)
    assert mh.check_if_splitting_is_needed() == expected_result


def test_check_if_splitting_is_needed_invalid_test_only_one_value():
    infile = '../resources/test_resources/test_only_one_value.csv'
    expected_result = False
    mh = csv_conversion.check_amount_of_measurements.MeasurementHandler(infile)
    assert mh.check_if_splitting_is_needed() == expected_result


def test_get_first_and_last_datetime_1():
    infile = '../resources/test_resources/test.csv'
    expected_result = ('2018-01-01T00:00:00.000Z', '2018-01-01T03:45:00.000Z')
    csvrw = csv_conversion.read_write_csv.CsvReaderWriter(infile)
    assert csvrw.get_first_and_last_datetime() == expected_result


def test_get_first_and_last_datetime_2():
    infile = '../resources/test_resources/test_loadprofiles.csv'
    expected_result = ('2015-12-31T23:00:00.000Z', '2015-12-31T23:15:00.000Z')
    csvrw = csv_conversion.read_write_csv.CsvReaderWriter(infile)
    assert csvrw.get_first_and_last_datetime() == expected_result
