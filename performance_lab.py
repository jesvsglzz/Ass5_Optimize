# 🔍 Problem 1: Find Most Frequent Element
# Given a list of integers, return the value that appears most frequently.
# If there's a tie, return any of the most frequent.
#
# Example:
# Input: [1, 3, 2, 3, 4, 1, 3]
# Output: 3

def most_frequent(numbers):
    freq = {}
    max_count = 0
    result = None
    for num in numbers:
        freq[num] = freq.get(num, 0) + 1
        if freq[num] > max_count:
            max_count = freq[num]
            result = num
    return result

"""
Time and Space Analysis for problem 1:
- Best-case: O(n); must scan all numbers at least once.
- Worst-case: O(n); same as best, we still process all numbers.
- Average-case: O(n).
- Space complexity: O(k), where k is number of unique elements.
- Why this approach? Efficient dictionary counting allows single-pass tracking.
- Could it be optimized? No major optimization; dictionary counting is optimal here.
"""


# 🔍 Problem 2: Remove Duplicates While Preserving Order
# Write a function that returns a list with duplicates removed but preserves order.
#
# Example:
# Input: [4, 5, 4, 6, 5, 7]
# Output: [4, 5, 6, 7]

def remove_duplicates(nums):
    seen = set()
    result = []
    for num in nums:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result

"""
Time and Space Analysis for problem 2:
- Best-case: O(n); must check all items.
- Worst-case: O(n); same since each item processed once.
- Average-case: O(n).
- Space complexity: O(n) for storing unique elements.
- Why this approach? Using a set allows O(1) lookups to avoid duplicates.
- Could it be optimized? Not really; this is optimal for order-preserving deduplication.
"""


# 🔍 Problem 3: Return All Pairs That Sum to Target
# Write a function that returns all unique pairs of numbers in the list that sum to a target.
# Order of output does not matter. Assume input list has no duplicates.
#
# Example:
# Input: ([1, 2, 3, 4], target=5)
# Output: [(1, 4), (2, 3)]

def find_pairs(nums, target):
    seen = set()
    pairs = []
    for num in nums:
        complement = target - num
        if complement in seen:
            pairs.append((complement, num))
        seen.add(num)
    return pairs

"""
Time and Space Analysis for problem 3:
- Best-case: O(n); must scan all elements.
- Worst-case: O(n); same since one pass through list.
- Average-case: O(n).
- Space complexity: O(n) for set and pairs.
- Why this approach? Using a set gives O(1) lookups and avoids nested loops.
- Could it be optimized? A sorting + two-pointer method also works (O(n log n)), but this O(n) approach is faster.
"""


# 🔍 Problem 4: Simulate List Resizing (Amortized Cost)
# Create a function that adds n elements to a list that has a fixed initial capacity.
# When the list reaches capacity, simulate doubling its size by creating a new list
# and copying all values over (simulate this with print statements).
#
# Example:
# add_n_items(6) → should print when resizing happens.

def add_n_items(n):
    capacity = 1
    arr = []
    for i in range(n):
        if len(arr) == capacity:
            print(f"Resizing: capacity {capacity} to {capacity * 2}")
            capacity *= 2
        arr.append(i)
    return arr

"""
Time and Space Analysis for problem 4:
- When do resizes happen? When list size == capacity.
- What is the worst-case for a single append? O(n); when resizing occurs and items are copied.
- What is the amortized time per append overall? O(1).
- Space complexity: O(n).
- Why does doubling reduce the cost overall? Because resizes happen less frequently as size grows, so average cost per append stays constant.
"""


# 🔍 Problem 5: Compute Running Totals
# Write a function that takes a list of numbers and returns a new list
# where each element is the sum of all elements up to that index.
#
# Example:
# Input: [1, 2, 3, 4]
# Output: [1, 3, 6, 10]
# Because: [1, 1+2, 1+2+3, 1+2+3+4]

def running_total(nums):
    result = []
    current_sum = 0
    for num in nums:
        current_sum += num
        result.append(current_sum)
    return result

"""
Time and Space Analysis for problem 5:
- Best-case: O(n); need to sum all.
- Worst-case: O(n).
- Average-case: O(n).
- Space complexity: O(n) for result list.
- Why this approach? Simple single-pass accumulation.
- Could it be optimized? This is already optimal.
"""

# Testing

print("- Problem 1: Most Frequent")
print(most_frequent([1, 3, 2, 3, 4, 1, 3]))   # Expected 3
print(most_frequent([1, 1, 2, 2]))           # Expected 1 or 2
print(most_frequent([5]))                    # Expected 5

print("-Problem 2: Remove Duplicates")
print(remove_duplicates([4, 5, 4, 6, 5, 7])) # Expected [4, 5, 6, 7]
print(remove_duplicates([]))                 # Expected []
print(remove_duplicates([1, 1, 1]))          # Expected [1]

print("- Problem 3: Find Pairs")
print(find_pairs([1, 2, 3, 4], 5))           # Expected [(1, 4), (2, 3)]
print(find_pairs([1, 2], 10))                # Expected []
print(find_pairs([], 5))                     # Expected []

print("- Problem 4: Add N Items")
print(add_n_items(6))                        # Expected [0, 1, 2, 3, 4, 5]

print("- Problem 5: Running Total")
print(running_total([1, 2, 3, 4]))           # Expected [1, 3, 6, 10]
print(running_total([]))                     # Expected []
print(running_total([5]))                    # Expected [5]