#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Finds a peak in list_of_integers"""

    # Check for empty list or None
    if not list_of_integers:
        return None

    # Binary search for a peak
    lo = 0
    hi = len(list_of_integers) - 1

    while lo < hi:
        mid = (lo + hi) // 2

        # Check if mid is a peak
        if list_of_integers[mid] >= list_of_integers[mid + 1]:
            hi = mid
        else:
            lo = mid + 1

    # At this point, lo and hi point to the same element,
    # which is a peak
    return list_of_integers[lo]
