import csv
from csv_conversion import reformat_time

def writedatatocsvfile(rowlist, outfile):
    with open(outfile, 'a', newline='') as file:
        csvwriter = csv.writer(file)
        csvwriter.writerows(rowlist)

def get_first_and_last_datetime(filename):
    with open(filename, newline='') as csvfile:
        next(csvfile)
        csvreader = csv.reader(csvfile, delimiter=';')
        csvList = list(csvreader)
        return reformat_time.reformattime(csvList[0][0]), \
            reformat_time.reformattime(csvList[-1][0])


def convert_csv(file, outfile):
    startEndArray = get_first_and_last_datetime(file)
    measurement_field_list = get_measurement_field(file)
    # read and write lines one by one (no saving in memory)
    with open(file, newline='') as csvfile:
        # scip first line with next
        next(csvfile)
        csvreader = csv.reader(csvfile, delimiter=';')
        for index, row in enumerate(csvreader):
            rowlist = convert_row(index, row, startEndArray, measurement_field_list)
            # rowlist = add_startdate_and_enddate(rowlist, startdate, enddate)
            writedatatocsvfile(rowlist, outfile)

def get_measurement_field(file):
    with open(file, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=';')
        for row in csvreader:
            firstline = row
            break

    measurement_field = firstline[2]

    # 1) extract field (== unit indicated by [])
    field = measurement_field[measurement_field.find('[') +
                              1: measurement_field.find(']')]

    # 2) extract rest of string (== measurement) removing field
    measurement = measurement_field.replace(field, '').\
        replace('[', '').\
        replace(']', '').\
        rstrip()

    measurement_field_list = []
    measurement_field_list.extend((field, measurement))

    return measurement_field_list



def convert_row(index, row, startEndArray, measurement_field_list):
    time = reformat_time.reformattime(row[0])
    value = row[2].replace(",", ".")
    # comments == requirements
    starttime = startEndArray[0]  # method to read only first time
    stoptime = startEndArray[1]  # method to read last time

    # methods to read measurement and field informationfrom the first line:
    field = measurement_field_list[0]
    measurement = measurement_field_list[1]


    rowlist = [['','', index, starttime, stoptime,
                       time, value, field, measurement]]


    return rowlist

