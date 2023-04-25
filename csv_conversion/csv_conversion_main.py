from csv_conversion import read_write_csv
from csv_conversion import outfile_validation
from csv_conversion import header_handling


def convert_csv(infile):
    outfile = infile.replace('.csv', '_formatted.csv')
    outfile_validation.check_existing_outfile(outfile)
    header_handling.write_header(outfile)
    read_write_csv.convert_csv(infile, outfile)

