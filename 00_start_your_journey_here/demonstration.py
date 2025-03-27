from test_api.checks import run_test, skip_test, format_err_msg

"""
This is a demonstration problem to help you learn how to use the pre-made
tests.

The (not very useful) function `count_to_two` should count to two, but is
going wrong. To see the first test pass, from the command line, type:

python 00_start_your_journey_here/demonstration.py

The second test is currently being skipped, to run this test you should change
`@skip_test` to `@run_test` and run the same `python` command. This test should
fail until the code is fixed.

To fix the code, you should add 2 to the counter rather than 1.

Then run using the same `python` command in the terminal and you should see
all the tests pass.
"""


def count_to_two():
    counter = 0
    counter += 2  # <- change this!!
    return counter


@run_test
def count_to_two_should_return_integer():
    result = count_to_two()
    assert isinstance(result, int), format_err_msg(True, isinstance(result, int))


@run_test  # Switch skip_test to run_test
def count_to_two_should_return_two():
    result = count_to_two()
    assert result == 2, format_err_msg(2, count_to_two())


if __name__ == "__main__":
    count_to_two_should_return_integer()
    count_to_two_should_return_two()
