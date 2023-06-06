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


