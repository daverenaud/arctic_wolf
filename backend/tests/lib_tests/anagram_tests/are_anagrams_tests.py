from unittest import TestCase

from lib.anagram import are_anagrams


class AreAnagramsTests(TestCase):

    def test_returns_true_when_no_words_passed(self):
        self.assertTrue(are_anagrams())

    def test_returns_true_when_one_word_is_passed(self):
        self.assertTrue(are_anagrams('wolf'))

    def test_returns_true_when_all_words_are_anagrams(self):
        self.assertTrue(are_anagrams('wolf', 'flow'))

    def test_returns_false_when_not_all_words_are_anagrams(self):
        self.assertFalse(are_anagrams('wolf', 'flow', 'fun'))

    def test_returns_true_when_all_words_are_empty_strings(self):
        self.assertTrue(are_anagrams('', ''))
