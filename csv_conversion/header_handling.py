import csv


def write_header(outfile):

    def write_first_line():
        # first_line = '#group,false,true,true,false,false,true,true,'
        first_line = ['#group', 'false', 'true', 'true', 'false',
                      'false', 'true', 'true', '']
        with open(outfile, 'w', newline='') as file:
            csvwriter = csv.writer(file)
            csvwriter.writerow(first_line)

    def write_second_line():
        # second_line = '#datatype,string,long,dateTime:RFC3339,
        # dateTime:RFC3339,dateTime:RFC3339,double,string,string'
        second_line = ['#datatype', 'string', 'long',
                       'dateTime:RFC3339', 'dateTime:RFC3339', 'dateTime:RFC3339',
                       'double', 'string', 'string']
        with open(outfile, 'a', newline='') as file:
            csvwriter = csv.writer(file)
            csvwriter.writerow(second_line)

    def write_third_line():
        # third_line = '#default,_result,,,,,,,'
        third_line = ['#default', '_result', '', '', '', '', '', '', '']
        with open(outfile, 'a', newline='') as file:
            csvwriter = csv.writer(file)
            csvwriter.writerow(third_line)

    def write_fourth_line():
        # fourth_line = ',result,table,_start,_stop,_time,_value,_field,_measurement'
        fourth_line = ['', 'result', 'table', '_start', '_stop', '_time', '_value',
                       '_field', '_measurement']
        with open(outfile, 'a', newline='') as file:
            csvwriter = csv.writer(file)
            csvwriter.writerow(fourth_line)

    write_first_line()
    write_second_line()
    write_third_line()
    write_fourth_line()
