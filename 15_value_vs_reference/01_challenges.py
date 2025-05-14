import os
import sys

sys.path.append(os.getcwd())
from test_api.checks import run_test, skip_test

# DO NOT CHANGE CODE ABOVE THIS LINE

@run_test
def true_or_false_1():
    string_1 = 'hello'
    string_2 = 'hello'
    assert (string_1 == string_2) == True

@run_test
def true_or_false_2():
    ones = [1, 1]
    assert (ones[0] == ones[1]) == True

@run_test
def true_or_false_3():
    variable = "data"
    variable_2 = variable
    assert (variable == variable_2) == True


# DO NOT CHANGE CODE BELOW THIS LINE

if __name__ == "__main__":
    true_or_false_1()
    true_or_false_2()
    true_or_false_3()
