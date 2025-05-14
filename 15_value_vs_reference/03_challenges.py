import os
import sys

sys.path.append(os.getcwd())
from test_api.checks import run_test, skip_test

# DO NOT CHANGE CODE ABOVE THIS LINE

@run_test
def true_or_false_1():
    list_1 = [1, 2, 3]
    list_2 = [4, 5, 6]
    list_2 = list_1
    assert (list_1 is list_2) == True

@run_test
def true_or_false_2():
    list_1 = [1, 2, 3]
    list_2 = list_1
    list_2.append(4)
    assert (list_1 is list_2) == True

@run_test
def true_or_false_3():
    list_1 = [1, 2, 3]
    list_2 = list_1
    list_1 = list_1 + [4, 5, 6] 
    assert (list_1 is list_2) == False


# DO NOT CHANGE CODE BELOW THIS LINE

if __name__ == "__main__":
    true_or_false_1()
    true_or_false_2()
    true_or_false_3()
