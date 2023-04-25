# Requirements for CSV files

There are some requirements for csv files in order to make it possible for them to be uploaded to the InfluxDB.
The following requirements should apply for all csv files which serve as an input parameter for this program:

1. Delimiter of csv file has to be ','.
2. Decimal separator of values has to be '.'.
3. Timestamps have to and can only be in the first column.
4. Timestamps have to be in format "dd.MM.YYYY HH:mm:ss".
5. Value columns start from the second column.
6. Value columns can only contain valid values.
7. Headers of the columns should contain the name of the measurements/values.