import unittest
from cash_register import *

class Test_cash_register(unittest.TestCase):

    def test_amountPaid_isfloat(self):
        with self.assertRaises(TypeError):
            cash_register(amountDue, amountPaid)












if __name__ == '__main__':
    unittest.main()
        