import math
from bisect import bisect_right
# See https://leetcode.com/problems/median-of-two-sorted-arrays/
# My approach to this problem would be a process that constitutes two phases.
# Consider arrA and arrB where size(arrA) >= size(arrB)
# Arrays nums1 and nums2 can be filled into these according to their size, and I continue with
# this naming convention for simplicity of both documentation as well as the algorithm itself.
# Some important properties I can support on are:
#   (a) Arrays are sorted. Hence, I build on binary search to maximally exploit this to curb complexity.
#   (b) The position of the median of the merged array pos_merged_median = (size(arrA) + size(arrB)) / 2.
#       Since the assignment does not require reconstruction of all elements of the merged array,
#       it suffices to know how many places elements need to shift to the position of the new median if
#       start merging from arrA. More on this later.
#   (c) Consider arrB_median_candidates the set of elements cand for which
#           cand <= arrA[pos_merged_median].
#       Each element in arrB_median_candidates has an impact on the value of the resulting median.
#       Either these elements will shift the current elements of arrA to a rightward position if
#       I conduct a merger starting from arrA, or else they are themselves candidates for becoming the median.
#       Any element of arrB which is not part of arrB_median_candidates will not have any influence on the new median.
#   (d) In order to find the value of the new median, I need to consider both arrB_median_candidates and
#       arrA[(pos_arrA_median - size(arrB_median_candidates)):pos_merged_median] (all elements
#       between the 'old' median and current position of the median for arrA). To analyse this,
#       consider two cases:
#           (i.)    arrB_median_candidates are all smaller than or equal to current arrA median
#                   arrA[pos_arrA_median]: in this case, the latter will move rightward up until
#                   the new median position
#           (ii.)   In the other case, the new median will be an element in either the arrA candidate
#                   range above, or part of the arrB_median_candidates. I need to conduct comparisons
#                   of the values to determine the value.
#
# Supporting on these properties, I can go ahead and find an approach that does the following:
#   1. Compose arrB_median_candidates. For this, I need to collect all elements in arrB which
#       are smaller than or equal to the position of the new, merged median pos_merged_median.
#       I conduct a search for the largest element in arrB that is smaller than or equal to
#       arrA[pos_merged_median] at position pos_arrB_insertion.
#       The subarray arrB[0:pos_arrB_insertion] can then be used as arrB_median_candidates.
#       By depending on property (a), we can conduct a binary search for this and resolve This
#       step in O(log (m)) complexity.
#   2. Find the value of merged_array[pos_merged_median]. I need to know the impact of arrB_median_candidates
#       on the median of the merged array. I do not need to know the contents of merged_array,
#       but do need to take into account that elements in arrB_median_candidates have an influence
#       on the merged median. To do this, I need to iteratively disregard the elements in arrB_median_candidates
#       through comparing them with the candidate to-be median candidate_median. This needs to be
#       searched for in the range arrA[(pos_merged_median - size(arrB_median_candidates)):pos_merged_median].
#       The new median will certainly fall within this range because in 'best' case, all arrB_median_candidates
#       are smaller than the first element in that range and hence that element will be the new median.
#       In order to search for the median within arrA[(pos_merged_median - size(arrB_median_candidates)):pos_merged_median]
#       and arrB_median_candidates, I select a candidate_median. Property (a) supports me to do a
#       binary search iteratively. This is started with the median position of the
#       arrA[(pos_merged_median - size(arrB_median_candidates)):pos_merged_median] range.
#       For this candidate_median, I look for all the elements in arrB_median_candidates that can be disregarded.
#       Given a candidate_median, another binary search is conducted on arrB_median_candidates to
#       discover the position of the largest element smaller than or equal to the candidate_median.
#       This position pos_subset_limit demarks the subarray arrB_median_candidates[0:pos_subset_limit] with
#       all elements that satisfy this condition.
#TODO   If the size of this subarray, size(arrB_median_candidates[0:pos_subset_limit]) equals
#       the size of subset arrA[(pos_merged_median - size(arrB_median_candidates)):pos_candidate_median],
#       I know I've hit the final median in candidate_median and need not look further.
#       The same holds if no arrB_median_candidates are left.
#TODO   Because this approach conducts a binary search to continuously trim the candidates, this step has < O(log n*m) complexity.
# Do not that there is the cornercase in which size(arrA) + size(arrB) is even.
# This does not have an impact the approach nor the time complexity, but needs to be considered when designing the algorithm.
#
class Solution:
    # Finds the position of the largest element that is smaller than the given value
    def find_position(self, list, value):
        return bisect_right(list, value)

    # Finds the value of the largest element that is smaller than the given values
    def find_value(self, list, value):
        return list[self.find_position(list, value)]

    def obtain_pos_merged_median(self, arrA, arrB):
        result = math.floor((len(arrA) + len(arrB) + 1) / 2.0) - 1
        return result

    def compose_median_candidates(self, reference_value, arr):
        # Obtain the rightmost position for the candidates. This is the largest element smaller than or equal to reference_value.
        right = self.find_position(arr, reference_value)
        return arr[0:right]

    # Determines the median in an interval [pos_start, pos_end]
    def determine_pos_candidate_median(self, pos_start, pos_end):
        return pos_start + math.ceil((pos_end - pos_start) / 2.0)

    def findMedianSortedArrays(self, nums1, nums2):
        result = None
        # Ensure that arrA is always the largest in size, for simplicity of the algorithm
        if len(nums1) < len(nums2):
            arrA = nums2
            arrB = nums1
        else:
            arrA = nums1
            arrB = nums2
        pos_merged_median = self.obtain_pos_merged_median(arrA, arrB)
        # Step 1: Compose arrB_median_candidates
        arrB_median_candidates = self.compose_median_candidates(arrA[pos_merged_median], arrB)
        # Step 2: Find merged median
        # Initialize the candidate_median to reflect the median position of arrA
        pos_min = 0  # Reflects the minimal potential position for the new median, if it was inside arrA
        pos_max = len(arrA) - 1  # Reflects the maximal potential position for the new median, if it was inside arrA
        pos_candidate_median = self.determine_pos_candidate_median(pos_min, pos_max)
        calibrated = False  # note that the first run may be off
        while True:
            if (pos_candidate_median + len(arrB_median_candidates)) > pos_merged_median:
                pos_min = pos_min
                pos_max = pos_candidate_median
            else:
                pos_min = pos_candidate_median
                pos_max = pos_max
            pos_candidate_median = self.determine_pos_candidate_median(pos_min, pos_max)
            arrB_median_candidates = self.compose_median_candidates(arrA[pos_candidate_median], arrB)
            if (len(arrB_median_candidates) + pos_candidate_median) >= pos_merged_median or len(arrB_median_candidates) is 0:
                break
        if (len(arrB_median_candidates) + pos_candidate_median) > pos_merged_median:
            # The merged median is residing inside arrB_median_candidates
            result = arrB_median_candidates[len(arrB_median_candidates) + pos_candidate_median - pos_merged_median]
        else:
            result = arrA[pos_candidate_median]
        # cornercase: the sum of lenghts of both arrays is even
        if (len(arrA) + len(arrB)) % 2 is 0:
            if arrB_median_candidates[len(arrB_median_candidates) + pos_candidate_median - pos_merged_median + 1] <= arrA[self.find_position(arrA, result)]:
                result = (result + arrB_median_candidates[len(arrB_median_candidates) + pos_candidate_median - pos_merged_median + 1]) / 2.0
            else:
                result = (result + arrA[self.find_position(arrA, result)]) / 2.0
        return result
