import unittest
from age import categorize_by_age

class TestCategorizeByAge(unittest.TestCase):
    """
    Unit tests for the categorize_by_age function.
    """

    def test_child(self):
        """
        Test categorization for child age group (0-9 years).
        """
        self.assertEqual(categorize_by_age(0), "Child")
        self.assertEqual(categorize_by_age(9), "Child")

    def test_adolescent(self):
        """
        Test categorization for adolescent age group (10-18 years).
        """
        self.assertEqual(categorize_by_age(10), "Adolescent")
        self.assertEqual(categorize_by_age(18), "Adolescent")

    def test_adult(self):
        """
        Test categorization for adult age group (19-65 years).
        """
        self.assertEqual(categorize_by_age(19), "Adult")
        self.assertEqual(categorize_by_age(65), "Adult")

    def test_golden_age(self):
        """
        Test categorization for golden age group (66-150 years).
        """
        self.assertEqual(categorize_by_age(66), "Golden age")
        self.assertEqual(categorize_by_age(150), "Golden age")

    def test_invalid_age_negative(self):
        """
        Test categorization for invalid negative age.
        """
        self.assertEqual(categorize_by_age(-1), "Invalid age: -1")

    def test_invalid_age_too_old(self):
        """
        Test categorization for invalid age greater than 150.
        """
        self.assertEqual(categorize_by_age(151), "Invalid age: 151")

    def test_edge_cases(self):
        """
        Test categorization for edge cases between categories.
        """
        self.assertEqual(categorize_by_age(9), "Child")
        self.assertEqual(categorize_by_age(10), "Adolescent")
        self.assertEqual(categorize_by_age(18), "Adolescent")
        self.assertEqual(categorize_by_age(19), "Adult")
        self.assertEqual(categorize_by_age(65), "Adult")
        self.assertEqual(categorize_by_age(66), "Golden age")
        self.assertEqual(categorize_by_age(150), "Golden age")

if __name__ == "__main__":
    unittest.main()