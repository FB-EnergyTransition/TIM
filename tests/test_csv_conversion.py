from csv_conversion import time_reformatting, csv_conversion_main


def test_reformat_time_1():
    time = '01.01.2018 00:00:00'
    expected_output = '2018-01-01T00:00:00.000Z'
    assert time_reformatting.reformat_time(time) == expected_output


def test_reformat_time_2():
    time = '23.04.2023 02:05:44'
    expected_output = '2023-04-23T02:05:44.000Z'
    assert time_reformatting.reformat_time(time) == expected_output


def test_convert_row():
    infile = '../resources/test.csv'
    row = ['01.01.2018 00:00:00', '-6.00', '', '']
    row_list = [['', '', 0, '2018-01-01T00:15:00.000Z', '2018-01-01T04:00:00.000Z',
                '2018-01-01T00:00:00.000Z', '-6.00', 'EUR/kWh',
                'Preis EXAA 10:15 Auktion']]

    assert csv_conversion_main.convert_row(0, row, ['2018-01-01T00:15:00.000Z',
                                      '2018-01-01T04:00:00.000Z'],
                                      infile, item=1, units='EUR/kWh') == row_list





