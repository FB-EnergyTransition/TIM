from input_params import input_params
from csv_conversion import *

infile = './resources/test.csv'

def main():
    args = input_params.process_input_params()
    conversion_main.convert_csv(infile)
    print(args)


if __name__ == "__main__":
    main()