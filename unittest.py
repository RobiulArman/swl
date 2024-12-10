# Define the functions
def capitalize_word(word):
    """Capitalizes the first letter of a word."""
    if not isinstance(word, str):
        raise ValueError("Input must be a string")
    return word.capitalize()

def count_vowels(word):
    """Counts the number of vowels in a word."""
    if not isinstance(word, str):
        raise ValueError("Input must be a string")
    vowels = "aeiouAEIOU"
    return sum(1 for char in word if char in vowels)

# Unit test using unittest
import unittest

class TestStringFunctions(unittest.TestCase):

    def test_capitalize_word(self):
        self.assertEqual(capitalize_word("hello"), "Hello")
        self.assertEqual(capitalize_word("HELLO"), "Hello")
        self.assertEqual(capitalize_word("hElLo"), "Hello")
        self.assertEqual(capitalize_word(""), "")
        
        with self.assertRaises(ValueError):
            capitalize_word(123)
        
        with self.assertRaises(ValueError):
            capitalize_word(None)

    def test_count_vowels(self):
        self.assertEqual(count_vowels("hello"), 2)
        self.assertEqual(count_vowels("HELLO"), 2)
        self.assertEqual(count_vowels("rhythm"), 0)
        self.assertEqual(count_vowels("aAeEiIoOuU"), 10)
        
        self.assertEqual(count_vowels(""), 0)
        self.assertEqual(count_vowels("12345"), 0)
        
        with self.assertRaises(ValueError):
            count_vowels(123)
        
        with self.assertRaises(ValueError):
            count_vowels(None)

# To run the unit tests in Colab
unittest.main(argv=[''], verbosity=2, exit=False)  # This runs the tests in the notebook itself