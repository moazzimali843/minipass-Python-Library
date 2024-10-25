# tests/test_checker.py

import unittest
from minipass.checker import PasswordChecker

class TestPasswordChecker(unittest.TestCase):
    def setUp(self):
        self.checker = PasswordChecker()

    def test_password_strength(self):
        score, suggestions = self.checker.check_strength("P@ssw0rd")
        self.assertEqual(score, 10)
        self.assertEqual(suggestions, [])

    def test_common_password(self):
        score, suggestions = self.checker.check_strength("1234")
        self.assertLess(score, 5)
        self.assertIn("Avoid common patterns", suggestions)

if __name__ == '__main__':
    unittest.main()
