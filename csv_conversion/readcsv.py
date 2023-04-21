import csv
import os

file = '../resources/test.csv'
outfile = file.replace('.csv', '_formatted.csv')

def checkoutfile(outfile):
    if os.path.exists(outfile):
        os.remove(outfile)

checkoutfile(outfile)

def writedatatocsvfile(rowlist):
    with open(outfile, 'a', newline='') as file:
        csvwriter = csv.writer(file)
        csvwriter.writerows(rowlist)

def reformattime(intime):
    day = intime[0:2]
    month = intime[3:5]
    year = intime[6:10]
    hour = intime[11:13]
    minutes = intime[14:16]
    seconds = intime[17:19]

    outtime = "{}-{}-{}T{}:{}:{}.000Z".format(
        year, month, day, hour, minutes, seconds)

    return outtime

def convert_csv(file):
    # read and write lines one by one (no saving in memory)
    with open(file, newline='') as csvfile:
        # scip first line with next
        next(csvfile)
        csvreader = csv.reader(csvfile, delimiter=';')
        for index, row in enumerate(csvreader):
            rowlist = convert_row(index, row)
            writedatatocsvfile(rowlist)

    return outfile


def convert_row(indicator, row):
    print(row)
    time = reformattime(row[0])
    value = row[2].replace(",", ".")
    # comments == requirements
    starttime = "2018-01-01T00:15:00.000Z"  # method to read only first time
    stoptime = "2018-01-01T04:00:00.000Z"  # method to read last time
    # methods to read this information from the first line:
    # (skipped above)
    field = "EUR/kWh"
    measurement = "Preis EXAA 10:15 Auktion"

    rowlist = [['','',indicator, starttime, stoptime,
                       time, value, field, measurement]]


    print(rowlist)

    return rowlist

    #writedatatocsvfile(rowlist)


convert_csv(file)
