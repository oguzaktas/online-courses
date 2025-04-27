import pytest
from preprocessing_helpers import row_to_list


def test_on_no_tab_with_missing_value():  # (0, 1) case
    # Assign to the actual return value for the argument "\n"
    actual = None
    # Write the assert statement with a failure message
    assert row_to_list("\n") is actual, "Expected: None, Actual: {0}".format(actual)


def test_on_two_tabs_with_missing_value():  # (2, 1) case
    # Assign to the actual return value for the argument "123\t\t89\n"
    actual = None
    # Write the assert statement with a failure message
    assert row_to_list("123\t\t89\n") is actual, "Expected: None, Actual: {0}".format(actual)