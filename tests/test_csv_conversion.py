import csv_conversion.csv_conversion_main
from csv_conversion import csv_conversion_main


def test_convert_row_1():
    infile = '../resources/test_resources/test.csv'
    units = 'EUR/kWh'
    row = ['01.01.2018 00:00:00', '-6.00', '', '']
    row_list = [['', '', 0, '2018-01-01T00:15:00.000Z', '2018-01-01T04:00:00.000Z',
                '2018-01-01T00:00:00.000Z', '-6.00', 'EUR/kWh',
                'Preis EXAA 10:15 Auktion']]
    csvc = csv_conversion.csv_conversion_main.CsvConverter(infile, units)
    assert csvc.convert_row(0, row, ['2018-01-01T00:15:00.000Z',
                                     '2018-01-01T04:00:00.000Z'], item=1) \
           == row_list


def test_convert_row_2():
    infile = '../resources/test_resources/test_loadprofiles.csv'
    units = 'EUR'
    row = ['31.12.2015 23:00:00', '0.001497553', '0.001093118', '0.000598087',
           '0.0008511', '0.002365702']
    row_list = [['', '', 0, '2015-12-31T23:00:00.000Z', '2015-12-31T23:15:00.000Z',
                 '2015-12-31T23:00:00.000Z', '0.001093118', 'EUR', 'CHR_2']]
    csvc = csv_conversion.csv_conversion_main.CsvConverter(infile, units)
    assert csvc.convert_row(0, row, ['2015-12-31T23:00:00.000Z',
                                     '2015-12-31T23:15:00.000Z'],
                            item=2) == row_list




