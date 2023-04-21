from csv_conversion import read_write_csv
from csv_conversion import delete_file

# infile = '../resources/test.csv'
def convert_csv(infile):
    outfile = infile.replace('.csv', '_formatted.csv')
    delete_file.checkoutfile(outfile)
    read_write_csv.convert_csv(infile, outfile)

# convert_csv(infile)
