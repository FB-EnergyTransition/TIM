import input_params


def test_existing_and_valid_csv_path():
    path = 'C:/Users/fbkmedwenitsch/OneDrive - Fachhochschule Burgenland GmbH/Dokumente/Aufgaben Karina/TIM Praxisprojekt/Bearbeitung csvs/vb für umwandlung annotated/EXAA 2022-04_2023 vb.csv'
    expected_output = True
    assert input_params.validate_csv_path(path) == expected_output


def test_non_existing_csv_path():
    path = 'C:/Users/fbkmedwenitsch/OneDrive - Fachhochschule Burgenland GmbH/Dokumente/Aufgaben Karina/TIM Praxisprojekt/Bearbeitung csvs/vb für umwandlung annotated/hallo.csv'
    expected_output = False
    assert input_params.validate_csv_path(path) == expected_output


def test_invalid_file_type_csv():
    path = 'C:/Users/fbkmedwenitsch/OneDrive - Fachhochschule Burgenland GmbH/Dokumente/Aufgaben Karina/TIM Praxisprojekt/Bearbeitung csvs/vb für umwandlung annotated/EXAA 2022-04_2023 vb.txt'
    expected_output = False
    assert input_params.validate_csv_path(path) == expected_output
