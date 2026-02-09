#!python


def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    Running time: O(n) always because we need to iterate through items1 and items2.
    Memory usage: O(n) because we create a new list to hold all n elements."""
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
    Running time: O(n log n), this is largely based on Python's built-in implementation of .sort()
    Memory usage: O(n) because we create left, right and merged arrays"""
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
    Running time: O(n log n)
    Memory usage: O(n log n), the copying at each level is O(n) per level, plus O(log n) levels"""
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
    `[low...high]` by choosing a pivot from that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    Partition uses the Lomuto pivot which is the last element.
    Running time: Always O(n), one pass through every element in the range
    Memory usage: O(1) because we're working in-place"""
    pivot = items[high]
    p = low
    for i in range(low, high):
        if items[i] <= pivot:
            items[p], items[i] = items[i], items[p]
            p += 1
    items[p], items[high] = items[high], items[p]
    return p


def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    Best case running time: O(n log n) when the pivot lands near the middle
    Worst case running time: O(n ^ 2) when the pivot lands at the edge. For example, the list is already sorted and we're using the Lomuto pivot
    Memory usage: O(log n) in the best case, O(n) in the worst case. The memory usage is proportional to the recursion depth"""
    if low is None and high is None:
        low = 0
        high = len(items) - 1

    if low >= high:
        return

    pivot_index = partition(items, low, high)

    quick_sort(items, low, pivot_index - 1)
    quick_sort(items, pivot_index + 1, high)

