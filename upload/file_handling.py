import os


class FileHandler:

    def get_all_converted_csvs(self, infile):
        csvs = []
        for file in os.listdir(os.path.dirname(infile)):
            if file.endswith('_formatted.csv'):
                csvs.append(file)
                print(file)
        return csvs
