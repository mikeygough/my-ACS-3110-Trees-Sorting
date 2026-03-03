#!python

import argparse
import time
from prefixtree import PrefixTree


def get_lines(filename='/usr/share/dict/words'):
    """Return a list of strings on separate lines in the given text file with
    any leading and trailing whitespace characters removed from each line."""
    # Open file and remove whitespace from each line
    with open(filename) as file:
        lines = [line.strip() for line in file]
    return lines



def autocomplete_setup(vocabulary, algorithm='linear_search'):
    """Return the main data structure needed to set up autocomplete using the
    given vocabulary and algorithm, specified as linear_search, trie, etc."""
    if algorithm == 'linear_search':
        # Use the given vocabulary list
        return vocabulary
    elif algorithm == 'trie':
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


def run_benchmark(prefix, vocabulary):
    """Run both algorithms on the same prefix and print a timing comparison."""
    print('Benchmark: linear search vs prefix tree')
    print('Vocabulary size: {:,}'.format(len(vocabulary)))
    print('Prefix: {!r}'.format(prefix))
    print()

    results = {}
    for algorithm in ('linear_search', 'trie'):
        start_time = time.time()
        structure = autocomplete_setup(vocabulary, algorithm)
        setup_time = time.time()
        completions = autocomplete(prefix, structure, algorithm)
        end_time = time.time()
        results[algorithm] = {
            'completions': len(completions),
            'setup': setup_time - start_time,
            'search': end_time - setup_time,
            'total': end_time - start_time,
        }

    linear = results['linear_search']
    trie = results['trie']
    speedup = linear['search'] / trie['search'] if trie['search'] > 0 else float('inf')

    print('{:<20} {:>12} {:>12}'.format('', 'Linear Search', 'Prefix Tree'))
    print('{:<20} {:>12} {:>12}'.format('Setup time (sec)',
          '{:.6f}'.format(linear['setup']), '{:.6f}'.format(trie['setup'])))
    print('{:<20} {:>12} {:>12}'.format('Search time (sec)',
          '{:.6f}'.format(linear['search']), '{:.6f}'.format(trie['search'])))
    print('{:<20} {:>12} {:>12}'.format('Completions found',
          linear['completions'], trie['completions']))
    print()
    print('Prefix tree search was {:.0f}x faster than linear search.'.format(speedup))


def run_interactive(vocabulary):
    """Load vocabulary into a prefix tree and run an interactive autocomplete loop."""
    print('Loading {:,} words into prefix tree...'.format(len(vocabulary)))
    start_time = time.time()
    structure = autocomplete_setup(vocabulary, 'trie')
    elapsed = time.time() - start_time
    print('Ready in {:.2f} sec. Type a prefix to autocomplete. Press Enter to quit.\n'.format(elapsed))

    while True:
        try:
            prefix = input('> ').strip()
        except (KeyboardInterrupt, EOFError):
            print()
            break
        if not prefix:
            break
        completions = autocomplete(prefix, structure, 'trie')
        if completions:
            print('{} completions: {}'.format(len(completions), ', '.join(completions[:10])))
            if len(completions) > 10:
                print('  ... and {} more'.format(len(completions) - 10))
        else:
            print('No completions found for {!r}'.format(prefix))
        print()


def main():
    """Read command-line arguments and test autocomplete algorithms."""
    parser = argparse.ArgumentParser(
        description='Autocomplete words from the English dictionary.'
    )
    parser.add_argument('prefix', nargs='?', help='Prefix string to autocomplete')
    parser.add_argument(
        '--algorithm', choices=['linear', 'trie'], default='linear',
        help='Search algorithm to use (default: linear)'
    )
    parser.add_argument(
        '--benchmark', action='store_true',
        help='Compare linear search and prefix tree side by side'
    )
    parser.add_argument(
        '--interactive', action='store_true',
        help='Interactively autocomplete prefixes using a prefix tree'
    )
    args = parser.parse_args()

    vocabulary = get_lines('/usr/share/dict/words')

    if args.interactive:
        run_interactive(vocabulary)
        return

    if args.benchmark:
        run_benchmark(args.prefix, vocabulary)
        return

    if not args.prefix:
        parser.print_help()
        return

    algorithm = 'linear_search' if args.algorithm == 'linear' else 'trie'

    # Start the clock for benchmarking
    start_time = time.time()

    # Set up autocomplete and mark the clock
    structure = autocomplete_setup(vocabulary, algorithm)
    setup_time = time.time()

    # Run autocomplete and mark the clock
    completions = autocomplete(args.prefix, structure, algorithm)
    end_time = time.time()

    print('Algorithm: {}'.format(args.algorithm))
    print('Vocabulary size: {:,}'.format(len(vocabulary)))
    print('Completions of {!r}: {}'.format(args.prefix, ', '.join(completions)))
    print()
    print('Initial setup time: {:.6f} sec'.format(setup_time - start_time))
    print('Autocomplete time:  {:.6f} sec'.format(end_time - setup_time))
    print('Total time elapsed: {:.6f} sec'.format(end_time - start_time))


if __name__ == '__main__':
    main()
