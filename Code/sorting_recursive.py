#!python


def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    TODO: Running time: O(n) always because we need to iterate through items1 and items2.
    TODO: Memory usage: O(n) because we create a new list to hold all n elementbecause we create a new list to hold all n elements."""
    results = []
    # i for items1, j for items2
    i = 0
    j = 0
    while i < len(items1) and j < len(items2):
        # zipper!
        if items1[i] <= items2[j]:
            results.append(items1[i])
            i += 1
        else:
            results.append(items2[j])
            j += 1
    # these are already sorted
    results.extend(items1[i:])
    results.extend(items2[j:])

    return results

    
def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.
    TODO: Running time: O(n log n), this is largely based on Python's built-in implementation of .sort()
    TODO: Memory usage: O(n) because we create left, right and merged arrays?"""
    middle = len(items) // 2
    left = items[:middle]
    left.sort()
    right = items[middle:]
    right.sort()
    merged =  merge(left, right)

    return merged

    
def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: O(n log n)
    TODO: Memory usage: O(n log n), the copying at each level is O(n) per level, plus O(log n) levels"""
    if len(items) <= 1:
        return items

    middle = len(items) // 2
    left = merge_sort(items[:middle])
    right = merge_sort(items[middle:])
    merged_and_sorted = merge(left, right)

    items[:] = merged_and_sorted
    return items


def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (TODO: document your method here) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Choose a pivot any way and document your method in docstring above
    # TODO: Loop through all items in range [low...high]
    # TODO: Move items less than pivot into front of range [low...p-1]
    # TODO: Move items greater than pivot into back of range [p+1...high]
    # TODO: Move pivot item into final position [p] and return index p


def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: ??? Why and under what conditions?
    TODO: Worst case running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if high and low range bounds have default values (not given)
    # TODO: Check if list or range is so small it's already sorted (base case)
    # TODO: Partition items in-place around a pivot and get index of pivot
    # TODO: Sort each sublist range by recursively calling quick sort
