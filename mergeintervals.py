# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
#  and return an array of the non-overlapping intervals that cover all the intervals in the input.
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        i =0 
        while i< len(intervals)-1:
            if intervals[i][1]>= intervals[i+1][0]:
                if intervals[i][1]< intervals[i+1][1]: 
                    intervals[i][1] = intervals[i+1][1]
                intervals.remove(intervals[i+1])
            else:    
                i+=1
        return intervals