class Printer:

    def __init__(self):
        self.file = ""

    def print_welcome_screen(self):
        print("""
        **********************************************************
        Welcome!
        With this program, you can upload data from csv files
        into a desired bucket in the Forschung Burgenland InfluxDB.
        
        NOTE: Before trying to upload, please read the CSV requirements.
        **********************************************************
    
        """)

    def print_successful_upload(self, file):
        self.file = file
        print("""
        **********************************************************
        Data from file """ + self.file + """ has been uploaded successfully.
        **********************************************************
        """)


    def print_end_program(self):
        print("""
        Ending program...
        """)

    def print_options(self):
        print("""
        Please chose an option:

        1 - Upload data from CSV
        2 - Read CSV Requirements
        """)

    def print_invalid_option(self):
        print("Invalid option. Please chose 1 oder 2.")

    def print_csv_requirements(self):
        print("""
        These are the requirements a CSV file has to fulfill
        in order to be uploaded into the InfluxDB:

        **********************************************************
        1. Delimiter of csv file has to be ','.
        2. Decimal separator of values has to be '.'.
        3. Timestamps have to and can only be in the first column.
        4. Timestamps have to be in format "dd.MM.YYYY HH:mm:ss".
        5. Value columns start from the second column.
        6. Value columns can only contain valid values.
        7. Headers of the columns should contain the name of the
        measurements/values.
        **********************************************************
        """)

    def print_invalid_answer(self):
        print("Invalid option. Please chose Y or N.")


