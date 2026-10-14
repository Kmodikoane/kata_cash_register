import unittest
from cash_register import cash_register

class Test_cash_register(unittest.TestCase):

    def test_amounts_format(self):
        with self.assertRaises(TypeError):
            cash_register("string", [-1, 2,3])

    def test_amouontPaid_greater_amountDue(self):
        with self.assertRaises(ValueError):
            cash_register(576, 459)

    def test_correct_change(self):
        return










if __name__ == '__main__':
    unittest.main()
        