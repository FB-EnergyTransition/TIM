import csv
import os

file = '../resources/test.csv'
outfile = file.replace('.csv', '_formatted.csv')


def checkoutfile(outfile):
    if os.path.exists(outfile):
        os.remove(outfile)


checkoutfile(outfile)


def writedatatocsvfile(outfile, indicator, starttime, stoptime,
                       time, value, field, measurement):
    with open(outfile, 'a', newline='') as file:
        csvwriter = csv.writer(file)
        # csvwriter = csv.writer(file, quoting=csv.QUOTE_NONE, escapechar='')
        datastream = ',,{},{},{},{},{},{},{}'.format(indicator, starttime,
                                                     stoptime, time, value,
                                                     field, measurement)

        print(datastream)
        csvwriter.writerow([str(datastream)])
        # print(time)
        # csvwriter.writerow([time])


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
    # print(outtime)
    # 2022-12-31T23:59:59.999Z


def convert_csv(file):
    # read and write lines one by one (no saving in memory)
    with open(file, newline='') as csvfile:
        # scip first line with next
        next(csvfile)
        # spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
        csvreader = csv.reader(csvfile, delimiter=';')
        # indicator = 0
        for index, row in enumerate(csvreader):
            convert_row(index, row)



    return outfile


def convert_row(indicator, row):
    time = reformattime(row[1])
    value = row[2].replace(",", ".")
    # comments == requirements
    starttime = "2018-01-01T00:15:00.000Z"  # method to read only first time
    stoptime = "2018-01-01T04:00:00.000Z"  # method to read last time
    # methods to read this information from the first line:
    # (skipped above)
    field = "EUR/kWh"
    measurement = "Preis EXAA 10:15 Auktion"
    writedatatocsvfile(outfile, indicator, starttime, stoptime,
                       time, value, field, measurement)

convert_csv(file)
