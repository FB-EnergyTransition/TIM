def print_welcome_screen():
    print("""
    **********************************************************
    Welcome!
    With this program, you can upload data from csv files
    into a desired bucket in the Forschung Burgenland InfluxDB.
    
    NOTE: Before trying to upload, please read the CSV requirements.
    **********************************************************

    """)


def print_successful_upload(file):
    print("""
    **********************************************************
    Data from file """ + file + """ has been uploaded successfully.
    **********************************************************
    """)


def print_end_program():
    print("""
    Ending program...
    """)


