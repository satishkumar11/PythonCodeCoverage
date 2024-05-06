# code/statistics.py

from collections import Counter

def mean(data):
    """Calculate the mean of a list of numbers."""
    if not data:
        raise ValueError("Cannot calculate mean of an empty list.")
    return sum(data) / len(data)

def median(data):
    """Calculate the median of a list of numbers."""
    if not data:
        raise ValueError("Cannot calculate median of an empty list.")
    sorted_data = sorted(data)
    n = len(data)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2
    else:
        return sorted_data[mid]

def mode(data):
    """Calculate the mode(s) of a list of numbers."""
    if not data:
        raise ValueError("Cannot calculate mode of an empty list.")
    counts = Counter(data)
    max_count = max(counts.values())
    modes = [num for num, count in counts.items() if count == max_count]
    if len(modes) == len(data):
        return data  # If all values occur with the same frequency, return the original list
    return modes
