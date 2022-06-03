"""
This module designed for multiple assertions.
"""

import logging


class AssertsAccumulator():
    """
    Class for multiple assertions.
    For example:
        assert_accumulator.accumulate(1 < 2, 'Bad condition!')
        assert_accumulator.accumulate(1 > 2, 'Bad condition!')
        assert_accumulator.release()
    """

    def __init__(self):
        self.__container = ''

    def accumulate(self, condition, message):
        """
        This method accumulate conditions, with fail message.
        :param condition: Condition for check.
        :param message: Fail message.
        """

        try:
            assert condition
        except AssertionError:
            self.__container += message + '\n'

    def release(self):
        """
        Release all assertions.
        """

        temp = self.__container
        self.__container = ''

        if temp != '':
            logging.error(temp)
            raise AssertionError('\n' + temp)
