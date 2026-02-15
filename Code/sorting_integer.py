#!python


def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    TODO: Running time: O(n + k) where n is the length of numbers and k is the range
    TODO: Memory usage: O(k) for the counts list, O(n) for the output if not mutating in-place"""
    minimum = min(numbers)
    maximum = max(numbers)
    counts = [0] * (maximum - minimum + 1)
    for number in numbers:
        counts[number - minimum] += 1

    output = []
    for number, count in enumerate(counts):
        for _ in range(count):
            output.append(number + minimum)

    return output
    # inplace implementation... Improve this to mutate input instead of creating new output list
    # mutate the input array:
    # i = 0
    # for number, count in enumerate(counts):
    #   for _ in range(count):
    #       numbers[i] = number + minimum
    #       i += 1


def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    TODO: Running time: O(n + k) where n is the number of elements and k is the number of buckets.
    Worst case though is O(n log n) if all the numbers land in one bucket since we're using Python's built-in .sort() method.
    TODO: Memory usage: O(n + k), k buckets plus n elements spread across them"""
    minimum = min(numbers)
    maximum = max(numbers)
    # early return if all numbers are equal
    if minimum == maximum:
        return numbers
    ranges = (maximum - minimum) / num_buckets

    buckets = []
    for i in range(num_buckets):
        buckets.append([]) # append empty buckets

    for number in numbers:
        bucket_index = min(int((number - minimum) / ranges), num_buckets - 1)
        buckets[bucket_index].append(number)

    for bucket in buckets:
        bucket.sort()

    output = []
    for bucket in buckets:
        output.extend(bucket)
    return output

    # inplace implementation... Improve this to mutate input instead of creating new output list
    # i = 0
    # for bucket in buckets:
    #     for number in bucket:
    #        numbers[i] = number
    #        i += 1
