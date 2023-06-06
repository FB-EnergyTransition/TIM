class TimeFormatter:

    def __init__(self, intime):
        self.intime = intime

    def reformat_time(self):
        day = self.intime[0:2]
        month = self.intime[3:5]
        year = self.intime[6:10]
        hour = self.intime[11:13]
        minutes = self.intime[14:16]
        seconds = self.intime[17:19]

        outtime = "{}-{}-{}T{}:{}:{}.000Z".format(
            year, month, day, hour, minutes, seconds)

        return outtime
