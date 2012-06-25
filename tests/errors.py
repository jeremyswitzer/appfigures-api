import unittest
from appfigures.errors import AppFiguresException


class ErrorTest(unittest.TestCase):

    def setUp(self):
        self.status = 666
        self.description = "Test Description"
        self.message = "Test Message"
        self.additional = "Test Additional"
        self.reference = "0000000000"


    def test_appfigures_exception(self):
        args = (self.status, self.description, self.message, self.additional, self.reference)
        expected_str = "{0}. {1}. {2}. {3}. Ref #: {4}".format(*args)
        ex = AppFiguresException(*args)
        
        self.assertEqual(str(ex), expected_str)


if __name__ == "__main__":
    unittest.main()