# Start of unittest - add to completely test functions in exp_eval

import unittest
from exp_eval import *

class test_expressions(unittest.TestCase):

    def test_postfix_eval_custom(self):
        self.assertAlmostEqual(postfix_eval("5.0 1 2 + 4 ^ + 3.0 -"), 83)

    def test_postfix_eval_01(self):
        self.assertAlmostEqual(postfix_eval("3 5 +"), 8)

    def test_postfix_eval_02(self):
        try:
            postfix_eval("blah")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Invalid token")

    def test_postfix_eval_03(self):
        try:
            postfix_eval("4 +")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")

    def test_postfix_eval_04(self):
        try:
            postfix_eval("1 2 3 +")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Too many operands")

    def test_negative_squareroot(self):
        with self.assertRaises(ValueError):
            postfix_eval("-4 0.5 ^")

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            postfix_eval("3 0 /")

    def test_postfix_eval_double_exponent(self):
        self.assertAlmostEqual(postfix_eval("3 2 2 ^ ^"), 81)

    def test_postfix_eval_multiple_negatives(self):
        self.assertAlmostEqual(postfix_eval("-3 -4 *"), 12)

    def test_postfix_eval_floatExponentiation(self):
        self.assertAlmostEqual(postfix_eval("-3.0 3.0 2.0 ^ ^"), -19683)

    def test_infix_to_postfix_01(self):
        self.assertEqual(infix_to_postfix("6 - 3"), "6 3 -")
        self.assertEqual(infix_to_postfix("6"), "6")

    def test_infix_to_postfix_02(self):
        self.assertEqual(infix_to_postfix("3 + 4 * 2 / ( 1 - 5 ) ^ 2 ^ 3"),
                         '3 4 2 * 1 5 - 2 3 ^ ^ / +')
        
    def test_prefix_to_postfix(self):
        self.assertEqual(prefix_to_postfix("* - 3 / 2 1 - / 4 5 6"),
                         "3 2 1 / - 4 5 / 6 - *")

    def test_infix_to_postfix_evaluation(self):
        infix_expression = "2 ^ 3 ^ ( 1 + 1 )"
        #print(infix_to_postfix(infix_expression))
        self.assertEqual(postfix_eval(infix_to_postfix(infix_expression)), 512)

        infix_expression = "-2 ^ 3 ^ ( 1 + 1 )"
        self.assertEqual(postfix_eval(infix_to_postfix(infix_expression)), -512)

        infix_expression = "( ( 1494 ^ -1.72 ) * ( 1 - ( 38.4 ^ 2.5 ) ) ^ ( -1 / 3 ) ) * 10 ^ 7"
        self.assertEqual(postfix_eval(infix_to_postfix(infix_expression)), -1.65903977)

        infix_expression = "2000 - ( 3 * ( 441 ^ 0.5 ) * ( 3.5 * 2 ) )"
        #print(infix_to_postfix(infix_expression))
        self.assertEqual(postfix_eval(infix_to_postfix(infix_expression)), 1559)

        infix_expression = "2 ^ 0.5 ** 0.5 ** ( 1 / 2 )"
        self.assertAlmostEqual(postfix_eval(infix_to_postfix(infix_expression)), 1.528956463)

        infix_expression = "10 << 5"
        self.assertAlmostEqual(postfix_eval(infix_to_postfix(infix_expression)), 320)


    def test_07_postfix_eval_test_postfix_exceptions(self):
        try:
            postfix_eval("99 38 1.2 * 3.6 2.8 / + 6 - 3.7 2 / 5 / + 3 - 23 + 1.1 / 2.2 + 2.4 5 / - 1 - 1.6 3 / 9 / 2.8 * 3 - 6.2 4 / 12.8 2 * 1.1 / 4.4 3.2 1.1 5.2 / 9.9 * - / - + - +")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Too many operands")
        try:
            postfix_eval("38 1.2 * 3.6 2.8 / + 6 - 3.7 ** 2 / 5 / 3 - 23 + 1.1 / 2.2 + 2.4 5 / - 1 - 1.6 blah / 9 / 2.8 * 3 - 6.2 4 / 12.8 2 * 1.1 / 4.4 3.2 1.1 5.2 / 9.9 * - / - + - + -2 +")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Invalid token")
        try:
            postfix_eval("1.2 * 3.6 2.8 / + 6 - 3.7 2 / 5 / + 3 - 23 + 1.1 / 2.2 + 2.4 5 / - 1 - 1.6 3 / 9 / 2.8 * 3 - 6.2 4 / 12.8 2 * 1.1 / 4.4 3.2 1.1 5.2 / 9.9 * - / - + - +")
            self.fail()
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")

        print('the error we are concerned with is below')

        try:
            postfix_eval("12 1.2 * 10 10 - / 6 - 3.7 ** 2 / 5 / 3 - 23 + 1.1 / 2.2 + 2.4 5 / - 1 - 1.6 10 / 9 / 2.8 * 3 - 6.2 4 / 12.8 2 * 1.1 / 4.4 3.2 1.1 5.2 / 9.9 * - / - + - + -2 +")
        except PostfixFormatException as e:
            self.assertEqual(str(e), "Insufficient operands")

if __name__ == "__main__":
    unittest.main()
