from csv_conversion import csv_conversion_main


def test_convert_row_1():
    infile = '../resources/test.csv'
    row = ['01.01.2018 00:00:00', '-6.00', '', '']
    row_list = [['', '', 0, '2018-01-01T00:15:00.000Z', '2018-01-01T04:00:00.000Z',
                '2018-01-01T00:00:00.000Z', '-6.00', 'EUR/kWh',
                'Preis EXAA 10:15 Auktion']]

    assert csv_conversion_main.convert_row(0, row, ['2018-01-01T00:15:00.000Z',
                                      '2018-01-01T04:00:00.000Z'],
                                      infile, item=1, units='EUR/kWh') == row_list


def test_convert_row_2():
    infile = '../resources/test_loadprofiles.csv'
    row = ['31.12.2015 23:00:00', '0.001497553', '0.001093118', '0.000598087',
           '0.0008511', '0.002365702']
    row_list = [['', '', 0, '2015-12-31T23:00:00.000Z', '2015-12-31T23:15:00.000Z',
                 '2015-12-31T23:00:00.000Z', '0.001093118', 'EUR', 'CHR_2']]

    assert csv_conversion_main.convert_row(0, row, ['2015-12-31T23:00:00.000Z',
                                                    '2015-12-31T23:15:00.000Z'],
                                           infile, item=2, units='EUR') == row_list




