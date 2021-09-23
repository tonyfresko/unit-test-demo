from sam_utils.strings import to_camelcase
"""
Function is called in tests below
"""
expected_result = "ShouldBeCamelCase"


def test_to_camelcase_underscores():
    result_underscores = to_camelcase('should_be_camel_case')
    assert result_underscores == expected_result


def test_to_camelcase_spaces():
    result_spaces = to_camelcase('should be camel case')
    assert result_spaces == expected_result


def test_to_camelcase_alphanumeric():
    result_hyphens = to_camelcase('should@€$ bE camEl case')
    assert result_hyphens == expected_result
