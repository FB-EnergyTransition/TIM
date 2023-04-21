# Requirements for CSV files

There are some requirements for csv files in order to make it possible for them to be uploaded to the InfluxDB.
The following requirements should apply for all csv files which serve as an input parameter for this program:

1. Timestamps have to and can only be in the first column.
2. Timestamps have to be in format "dd.MM.YYYY HH:mm:ss".
3. Value columns start from the second column.
4. Value columns can only contain valid values.
5. Headers of the columns should contain the name of the measurements/values.