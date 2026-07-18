#!/usr/bin/env python3

import unittest

from google_automation.testing.pytest.tryexcept import validate_user2

class TestValidateUser(unittest.TestCase):
  def test_valid(self):
    self.assertEqual(validate_user2("validuser", 3), True)

  def test_too_short(self):
    self.assertEqual(validate_user2("inv", 5), False)

  def test_invalid_characters(self):
    self.assertEqual(validate_user2("invalid_user", 1), False)
  def test_invalid_minlen(self):
    self.assertRaises(ValueError, validate_user2, "user", -1)


# Run the tests
unittest.main()
