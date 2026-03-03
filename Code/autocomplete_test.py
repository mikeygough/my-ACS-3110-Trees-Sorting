#!python3

import unittest
from autocomplete import autocomplete_setup, autocomplete

WORDS = ['apple', 'application', 'apply', 'apt', 'banana', 'band', 'bandana']


class AutocompleteLinearTest(unittest.TestCase):
    """Tests for autocomplete using linear search."""

    def setUp(self):
        self.structure = autocomplete_setup(WORDS, algorithm='linear_search')

    def test_setup_returns_list(self):
        self.assertIsInstance(self.structure, list)

    def test_returns_correct_completions(self):
        result = autocomplete('app', self.structure, algorithm='linear_search')
        self.assertCountEqual(result, ['apple', 'application', 'apply'])

    def test_no_match_returns_empty(self):
        result = autocomplete('xyz', self.structure, algorithm='linear_search')
        self.assertEqual(result, [])

    def test_exact_word_match(self):
        result = autocomplete('banana', self.structure, algorithm='linear_search')
        self.assertEqual(result, ['banana'])


class AutocompleteTrieTest(unittest.TestCase):
    """Tests for autocomplete using prefix tree."""

    def setUp(self):
        from prefixtree import PrefixTree
        self.structure = autocomplete_setup(WORDS, algorithm='trie')

    def test_setup_returns_prefix_tree(self):
        from prefixtree import PrefixTree
        self.assertIsInstance(self.structure, PrefixTree)

    def test_returns_correct_completions(self):
        result = autocomplete('app', self.structure, algorithm='trie')
        self.assertCountEqual(result, ['apple', 'application', 'apply'])

    def test_no_match_returns_empty(self):
        result = autocomplete('xyz', self.structure, algorithm='trie')
        self.assertEqual(result, [])

    def test_exact_word_match(self):
        result = autocomplete('banana', self.structure, algorithm='trie')
        self.assertEqual(result, ['banana'])


class AutocompleteConsistencyTest(unittest.TestCase):
    """Verify that linear search and prefix tree return the same results."""

    def setUp(self):
        self.linear = autocomplete_setup(WORDS, algorithm='linear_search')
        self.trie = autocomplete_setup(WORDS, algorithm='trie')

    def _compare(self, prefix):
        linear_result = autocomplete(prefix, self.linear, algorithm='linear_search')
        trie_result = autocomplete(prefix, self.trie, algorithm='trie')
        self.assertCountEqual(linear_result, trie_result)

    def test_shared_prefix(self):
        self._compare('app')

    def test_no_match(self):
        self._compare('xyz')

    def test_single_char_prefix(self):
        self._compare('a')

    def test_full_word(self):
        self._compare('band')


if __name__ == '__main__':
    unittest.main()
