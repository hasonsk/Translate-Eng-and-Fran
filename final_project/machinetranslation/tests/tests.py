import unittest 
import sys
sys.path.append("..")  

from translator import english_to_french, french_to_english

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertNotEqual(english_to_french("Hello"), "Salut")
    def test2(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertNotEqual(french_to_english("bien"), "bad")


unittest.main()