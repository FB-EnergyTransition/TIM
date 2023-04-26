from csv_conversion import outfile_validation


def test_check_existing_outfile():
    outfile = '../resources/test.csv'
    expected_result = True
    assert outfile_validation.check_existing_outfile(outfile) == expected_result


def test_check_measurement_name():
    measurement = 'test: Preis'
    expected_result = 'test Preis'
    assert outfile_validation.check_measurement_name(measurement) == expected_result