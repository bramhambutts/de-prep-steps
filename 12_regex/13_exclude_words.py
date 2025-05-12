import os
import sys
import re

sys.path.append(os.getcwd())

from test_api.checks import run_test, skip_test, format_err_msg

# DO NOT CHANGE CODE ABOVE THIS LINE

# This challenge is more advanced.
# Again, please do not change the tests
# For the function, delete the `pass` keyword and write code that makes the
#  tests pass


def exclude_words(text):
    """
    Write a function using regex which returns a string with everything except
    the words 'north' and 'coders'.

    Everything else, even words starting, including or ending with these words
    should be matched.

    Your matches and non-matches should be case insensitive.

    For example:
    - "I visited the north pole last year." should be "I visited the pole last
        year."
    - "I study at Northcoders." should be "I study at Northcoders."
    - "IBM hired a lot of coders." should be "IBM hired a lot of ."
    """
    north = re.compile(r'\snorth\s', re.IGNORECASE)
    text = ' '.join(re.split(north, text))
    coders = re.compile(r'\scoders\s', re.IGNORECASE)
    text = ' '.join(re.split(coders, text))
    return text


@run_test
def test_exclude_words_excludes_separate_words_only():
    assert exclude_words(
        "I visited the north pole last year") == "I visited the pole last year", \
        format_err_msg("I visited the pole last year",
                       exclude_words("I visited the north pole last year"))
    assert exclude_words("I study at Northcoders") == "I study at Northcoders", \
        format_err_msg(
            "I study at Northcoders", exclude_words("I study at Northcoders"))
    assert exclude_words(
        "IBM hired a lot of coders lately") == "IBM hired a lot of lately", \
        format_err_msg(
        "IBM hired a lot of lately",
        exclude_words("IBM hired a lot of coders lately"))


# DO NOT CHANGE CODE BELOW THIS LINE
if __name__ == '__main__':
    test_exclude_words_excludes_separate_words_only()
