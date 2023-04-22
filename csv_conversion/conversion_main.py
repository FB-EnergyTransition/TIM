from csv_conversion import read_write_csv
from csv_conversion import delete_file
from csv_conversion import write_header

# infile = '../resources/test.csv'
def convert_csv(infile):
    outfile = infile.replace('.csv', '_formatted.csv')
    delete_file.checkoutfile(outfile)
    write_header.write_header(outfile)
    read_write_csv.convert_csv(infile, outfile)

# convert_csv(infile)
