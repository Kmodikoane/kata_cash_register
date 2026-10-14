import unittest
from cash_register import cash_register, change_in_cents

class Test_cash_register(unittest.TestCase):

    def test_amounts_format(self):
        with self.assertRaises(TypeError):
            cash_register("string", [-1, 2,3])

    def test_amouontPaid_greater_amountDue(self):
        with self.assertRaises(ValueError):
            cash_register(576, 459)

    def test_converts_to_cents(self):
        change_in_cents
        return

    def test_calculates_zero_cents(self):
        return

    def test_positive_cents(self):
        return

    def raise_error_negative_cents(self):
        return










if __name__ == '__main__':
    unittest.main()
        