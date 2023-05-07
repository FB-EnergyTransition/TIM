import datetime
import os

path = "./logfiles"

now = datetime.datetime.now()
day = now.strftime("%Y-%m-%d")
time = now.strftime("%Y-%m-%d %H:%M:%S")
logfile = "{}/log_{}".format(path, day)


def clearfiles():
    for file in os.listdir(path):
        date = datetime.datetime.strptime(file.replace("log_", "").
                                          replace(".txt", ""), "%Y-%m-%d")
        fileday = date.day

        if int(now.strftime("%d")) - 7 >= fileday:
            os.remove('{}/{}'.format(path, file))


def print_to_log(measurement):
    text = open(logfile, "a")
    text.write(measurement)
    text.close()


def error_message(e):
    logf = open(logfile, "a")
    logf.write("{}: {}\n".format(time, str(e)))
    print('\n!!! Error !!! Check logfile in folder ./logfiles for details. \n'
          'Based on the information try again')
