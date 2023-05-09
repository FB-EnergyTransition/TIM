import datetime
import traceback

path = "./logfiles"

now = datetime.datetime.now()
day = now.strftime("%Y-%m-%d")
logfile = "{}/log_{}".format(path, day)

def print_to_log(measurement):
    text = open(logfile, "a")
    text.write(measurement)
    text.close()


def error_message(e):
    now = datetime.datetime.now()
    time = now.strftime("%Y-%m-%d %H:%M:%S")
    logf = open(logfile, "a")
    logf.write("{}: {}\n".format(time, traceback.format_exc()))
    print('\n!!! Error !!!\n{}\nCheck logfile in folder ./logfiles for details.\n'
          'Based on the information try again'.format(e))
