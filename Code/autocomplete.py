#!python

import argparse
import time


def get_lines(filename='/usr/share/dict/words'):
    """Return a list of strings on separate lines in the given text file with
    any leading and trailing whitespace characters removed from each line."""
    # Open file and remove whitespace from each line
    with open(filename) as file:
        lines = [line.strip() for line in file]
    return lines


def generate_prefixes(vocabulary):
    """Return a set of unique prefixes from the given list of strings."""
    # Generate prefixes using the first half of each string
    return set(word[:len(word)//2] for word in vocabulary)


def autocomplete_setup(vocabulary, algorithm='linear_search'):
    """Return the main data structure needed to set up autocomplete using the
    given vocabulary and algorithm, specified as linear_search, trie, etc."""
    if algorithm == 'linear_search':
        # Use the given vocabulary list
        return vocabulary
    elif algorithm == 'trie':
        from prefixtree import PrefixTree
        # Create a prefix tree structure with the vocabulary
        return PrefixTree(vocabulary)


def autocomplete(prefix, structure, algorithm='linear_search'):
    """Return all vocabulary entries that start with the given prefix using the
    given structure and algorithm, specified as linear_search, trie, etc."""
    if algorithm == 'linear_search':
        # Search the list using linear search
        return [word for word in structure if word.startswith(prefix)]
    elif algorithm == 'trie':
        # Search the prefix tree for completions
        return structure.complete(prefix)


def main():
    """Read command-line arguments and test autocomplete algorithms."""
    parser = argparse.ArgumentParser(
        description='Autocomplete words from the English dictionary.'
    )
    parser.add_argument('prefix', help='Prefix string to autocomplete')
    parser.add_argument(
        '--algorithm', choices=['linear', 'trie'], default='linear',
        help='Search algorithm to use (default: linear)'
    )
    args = parser.parse_args()

    algorithm = 'linear_search' if args.algorithm == 'linear' else 'trie'
    vocabulary = get_lines('/usr/share/dict/words')

    # Start the clock for benchmarking
    start_time = time.time()

    # Set up autocomplete and mark the clock
    structure = autocomplete_setup(vocabulary, algorithm)
    setup_time = time.time()

    # Run autocomplete and mark the clock
    completions = autocomplete(args.prefix, structure, algorithm)
    end_time = time.time()

    print('Algorithm: {}'.format(args.algorithm))
    print('Vocabulary size: {}'.format(len(vocabulary)))
    print('Completions of {!r}: {}'.format(args.prefix, ', '.join(completions)))
    print()
    print('Initial setup time: {:.6f} sec'.format(setup_time - start_time))
    print('Autocomplete time:  {:.6f} sec'.format(end_time - setup_time))
    print('Total time elapsed: {:.6f} sec'.format(end_time - start_time))


if __name__ == '__main__':
    main()
