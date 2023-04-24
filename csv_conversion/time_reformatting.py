def reformat_time(intime):
    day = intime[0:2]
    month = intime[3:5]
    year = intime[6:10]
    hour = intime[11:13]
    minutes = intime[14:16]
    seconds = intime[17:19]

    outtime = "{}-{}-{}T{}:{}:{}.000Z".format(
        year, month, day, hour, minutes, seconds)

    return outtime
