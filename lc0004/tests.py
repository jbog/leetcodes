import pytest
from solution import Solution

solution = Solution()

def test_obtain_pos_merged_median():
    assert solution.obtain_pos_merged_median([1,2,3], [4,5]) == 2
    assert solution.obtain_pos_merged_median([1,1,1,1], [1]) == 2
    assert solution.obtain_pos_merged_median([1,1], [1]) == 1
    assert solution.obtain_pos_merged_median([1,1,1,1], [1,1]) == 2

def test_compose_median_candidates():
    assert solution.compose_median_candidates(5, [1,2,2,3,3,3,3,4,5,5,5,6,7,8,9,9,9,10]) == [1,2,2,3,3,3,3,4,5,5,5]
    assert solution.compose_median_candidates(5, [1,2,2,3,3,3,3,4,5,5,5]) == [1,2,2,3,3,3,3,4,5,5,5]
    assert solution.compose_median_candidates(5, [6,7,8,9,9,9,10]) == []
    assert solution.compose_median_candidates(5, [5,5,5,6,7,8,9,9,9,10]) == [5,5,5]
    assert solution.compose_median_candidates(0, []) == []

def test_initialize_pos_candidate_median():
    assert solution.initialize_pos_candidate_median(7, 1) == 6
    assert solution.initialize_pos_candidate_median(7, 2) == 6
    assert solution.initialize_pos_candidate_median(7, 3) == 5
    assert solution.initialize_pos_candidate_median(7, 4) == 5
    assert solution.initialize_pos_candidate_median(7, 5) == 4
    assert solution.initialize_pos_candidate_median(7, 6) == 4
    assert solution.initialize_pos_candidate_median(7, 7) == 3

def test_example1():
    assert solution.findMedianSortedArrays([1,3], [2]) == 2.0

def test_example2():
    assert solution.findMedianSortedArrays([1,2], [3,4]) == 2.5

def test_example3():
    assert solution.findMedianSortedArrays([1,3,4,5,7,15,18,21], [5,10,14,20,20,25,26,27]) == 14.5

def test_example4():
    assert solution.findMedianSortedArrays([3, 5, 13, 21, 23, 23, 23, 29, 40], [7, 12, 14, 23, 39, 56]) == 23

def test_example5():
    assert solution.findMedianSortedArrays([3, 5, 12, 13, 21, 23, 23, 23, 29, 40], [7, 14, 23, 39, 56]) == 23

def test_example6():
    assert solution.findMedianSortedArrays([5, 7, 12, 13, 14, 21, 23, 23, 29, 56], [3, 14, 21, 23, 23, 40]) == 22

def test_example7():
    assert solution.findMedianSortedArrays([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1

def test_example8():
    assert solution.findMedianSortedArrays([1, 2, 3, 4, 5, 6, 7, 8], [9, 10, 11, 12, 13, 14, 15]) == 8

def test_example9():
    assert solution.findMedianSortedArrays([1, 1, 3, 4, 7, 9, 10, 11, 14], [1, 2, 5, 7, 12]) == 5

def test_example10():
    assert solution.findMedianSortedArrays([1, 1, 3, 5, 7, 9, 10, 11, 14], [1, 2, 4, 7, 12]) == 5
