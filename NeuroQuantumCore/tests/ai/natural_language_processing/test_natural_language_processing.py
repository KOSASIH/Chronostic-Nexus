import unittest
from natural_language_processing.natural_language_processing import NaturalLanguageProcessing

class TestNaturalLanguageProcessing(unittest.TestCase):
    def test_natural_language_processing(self):
        natural_language_processing = NaturalLanguageProcessing()
        self.assertIsNotNone(natural_language_processing.model)

    def test_train(self):
        natural_language_processing = NaturalLanguageProcessing()
        natural_language_processing.train(["Hello, World!", "This is a test."])
        self.assertIsNotNone(natural_language_processing.model)

    def test_predict(self):
        natural_language_processing = NaturalLanguageProcessing()
        natural_language_processing.train(["Hello, World!", "This is a test."])
        self.assertIsNotNone(natural_language_processing.predict("Hello, World!"))

if __name__ == '__main__':
    unittest.main()
