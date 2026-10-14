import unittest
from cash_register import cash_register

class Test_cash_register(unittest.TestCase):

    def test_amounts_format(self):
        with self.assertRaises(TypeError):
            cash_register("string", [-1, 2,3])

    def test_amouontPaid_greater_amountDue(self):
        with self.assertRaises(ValueError):
            cash_register(576, 459)

    def returns_correct_change(self):
        self.asserEqual(cash_register(1569.96, 4592.12), 3022.16)

    

    def returns_correct_denominations(self):
        correct_denominations = {200.0: 17215, 100.0: 1, 50.0: 0, 20.0: 2, 10.0: 0, 5.0: 1, 2.0: 0, 1.0: 0, 0.5: 0}
        self.asserEqual(cash_register(34887, 3478032.21),)
        return

    def test_positive_cents(self):
        return

    def raise_error_negative_cents(self):
        return










if __name__ == '__main__':
    unittest.main()
        