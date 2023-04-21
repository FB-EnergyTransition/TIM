import csv
from csv_conversion import reformat_time

def writedatatocsvfile(rowlist, outfile):
    with open(outfile, 'a', newline='') as file:
        csvwriter = csv.writer(file)
        csvwriter.writerows(rowlist)

def convert_csv(file, outfile):
    # read and write lines one by one (no saving in memory)
    with open(file, newline='') as csvfile:
        # scip first line with next
        next(csvfile)
        csvreader = csv.reader(csvfile, delimiter=';')
        for index, row in enumerate(csvreader):
            rowlist = convert_row(index, row)
            writedatatocsvfile(rowlist, outfile)

def convert_row(index, row):
    print(row)
    time = reformat_time.reformattime(row[0])
    value = row[2].replace(",", ".")
    # comments == requirements
    starttime = "2018-01-01T00:15:00.000Z"  # method to read only first time
    stoptime = "2018-01-01T04:00:00.000Z"  # method to read last time
    # methods to read this information from the first line:
    # (skipped above)
    field = "EUR/kWh"
    measurement = "Preis EXAA 10:15 Auktion"

    rowlist = [['','', index, starttime, stoptime,
                       time, value, field, measurement]]


    print(rowlist)

    return rowlist

