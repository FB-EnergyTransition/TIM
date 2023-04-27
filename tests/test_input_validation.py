from user_interaction import input_validation


def test_validate_bucket_input_1():
    bucket = 'EXAA Data'
    expected_output = True
    assert input_validation.validate_bucket_input(bucket) == expected_output


def test_validate_bucket_input_2():
    bucket = 'helloWorld'
    expected_output = False
    assert input_validation.validate_bucket_input(bucket) == expected_output


def test_validate_option_1():
    option = "1"
    expected_output = True
    assert input_validation.validate_option(option) == expected_output


def test_validate_option_2():
    option = "3"
    expected_output = False
    assert input_validation.validate_option(option) == expected_output


def test_validate_unit_option_1():
    option = "yes"
    expected_result = True
    assert input_validation.validate_unit_option(option) == expected_result


def test_validate_unit_option_2():
    option = "nope"
    expected_result = False
    assert input_validation.validate_unit_option(option) == expected_result
