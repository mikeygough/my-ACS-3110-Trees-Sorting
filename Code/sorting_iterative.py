#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    TODO: Running time: O(n) in the worst case, O(1) in the best case.
    TODO: Memory usage: O(1) since this is an in-place operation."""
    for i in range(len(items) - 1):
        if items[i] > items[i + 1]:
            return False
    return True


def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    TODO: Running time: O(n^2) in the worst case, O(n) in the best case.
    TODO: Memory usage: O(1) since this is an in-place sorting algorithm."""
    for i in range(len(items)):
        swapped = False
        for j in range(len(items) - 1 - i):
            # swap
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
        # no swaps occurred, items is already sorted!
        if not swapped:
            break
    return items


def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: O(n^2) in all cases.
    TODO: Memory usage: O(1) since this is an in-place sorting algorithm"""
    for i in range(len(items) - 1):
        # grab smallest index for unsorted section
        smallest_index = i
        for j in range(i, len(items)):
            if items[j] < items[smallest_index]:
                smallest_index = j
        # swap smallest item to sorted section
        items[i], items[smallest_index] = items[smallest_index], items[i]
    return items


def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: O(n^2) in the worst case, O(n) in the best case.
    TODO: Memory usage: O(1) since this is an in-place sorting algorithm. """
    for i in range(1, len(items)):
        j = i
        while j > 0 and items[j] < items[j - 1]:
            items[j], items[j - 1] = items[j - 1], items[j]
            j -= 1
    return items
