from csv_conversion import read_write_csv, check_amount_of_measurements


def test_get_measurement_name_Preis_EXAA_10_15_Auktion():
    infile = '../resources/test_resources/test.csv'
    measurement_number = 1
    expected_result = "Preis EXAA 10:15 Auktion"
    assert read_write_csv.get_measurement_name(infile, measurement_number)\
           == expected_result


def test_get_measurement_name_CHR_2():
    infile = '../resources/test_resources/test_loadprofiles.csv'
    measurement_number = 2
    expected_result = "CHR_2"
    assert read_write_csv.get_measurement_name(infile, measurement_number)\
           == expected_result


def test_get_number_of_measurements_2():
    infile = '../resources/test_resources/test.csv'
    expected_result = 2
    assert check_amount_of_measurements.get_number_of_measurements(infile)\
           == expected_result


def test_get_number_of_measurements_5():
    infile = '../resources/test_resources/test_loadprofiles.csv'
    expected_result = 5
    assert check_amount_of_measurements.get_number_of_measurements(infile)\
           == expected_result


def test_get_number_of_measurements_1():
    infile = '../resources/test_resources/test_only_one_value.csv'
    expected_result = 1
    assert check_amount_of_measurements.get_number_of_measurements(infile)\
           == expected_result


def test_check_if_splitting_is_needed_valid_test_csv():
    infile = '../resources/test_resources/test.csv'
    expected_result = True
    assert check_amount_of_measurements.check_if_splitting_is_needed(infile)\
           == expected_result


def test_check_if_splitting_is_needed_valid_test_loadprofiles_csv():
    infile = '../resources/test_resources/test_loadprofiles.csv'
    expected_result = True
    assert check_amount_of_measurements.check_if_splitting_is_needed(infile)\
           == expected_result


def test_check_if_splitting_is_needed_invalid_test_only_one_value():
    infile = '../resources/test_resources/test_only_one_value.csv'
    expected_result = False
    assert check_amount_of_measurements.check_if_splitting_is_needed(infile)\
           == expected_result


def test_get_first_and_last_datetime_1():
    infile = '../resources/test_resources/test.csv'
    expected_result = ('2018-01-01T00:00:00.000Z', '2018-01-01T03:45:00.000Z')
    assert read_write_csv.get_first_and_last_datetime(infile) == expected_result


def test_get_first_and_last_datetime_2():
    infile = '../resources/test_resources/test_loadprofiles.csv'
    expected_result = ('2015-12-31T23:00:00.000Z', '2015-12-31T23:15:00.000Z')
    assert read_write_csv.get_first_and_last_datetime(infile) == expected_result
