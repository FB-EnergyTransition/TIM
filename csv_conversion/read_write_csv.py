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
    # read and write lines one by one (no saving in memory)
    with open(file, newline='') as csvfile:
        # scip first line with next
        next(csvfile)
        csvreader = csv.reader(csvfile, delimiter=';')
        for index, row in enumerate(csvreader):
            rowlist = convert_row(index, row, startEndArray)
            # rowlist = add_startdate_and_enddate(rowlist, startdate, enddate)
            writedatatocsvfile(rowlist, outfile)

def convert_row(index, row, startEndArray):
    time = reformat_time.reformattime(row[0])
    value = row[2].replace(",", ".")
    # comments == requirements
    starttime = startEndArray[0]  # method to read only first time
    stoptime = startEndArray[1]  # method to read last time
    # methods to read this information from the first line:
    # (skipped above)
    field = "EUR/kWh"
    measurement = "Preis EXAA 10:15 Auktion"

    rowlist = [['','', index, starttime, stoptime,
                       time, value, field, measurement]]


    return rowlist

