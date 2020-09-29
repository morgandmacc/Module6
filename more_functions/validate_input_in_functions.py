"""
Author: Morgan McCarley
Program: validate_input_in_functions.py


prompts user for name and score, prints values to console.
"""


def score_input(test_name, test_score = 0, invalid_message = 'Invalid test score, try again!'):
    """
    Function that accepts params and returns a string....
    :param test_name: The name of a test/exam
    :type test_name: String
    :param test_score: A value between 0 and 100 representing a test score
    :type test_score: int
    :param invalid_message: Message displayed when an invalid score in provided.
    :type invalid_message: String
    :return: formatted string with test name and test score.
    :rtype: String
    """
    #print("{}: {}".format(test_name, test_score))
    return "{}: {}".format(test_name, test_score)


if __name__ == '__main__':
    score_input("test1", 45)
