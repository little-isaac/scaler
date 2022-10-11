"""
Problem Description
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.



Problem Constraints
0 <= |intervals| <= 105



Input Format
First argument is the vector of intervals

second argument is the new interval to be merged



Output Format
Return the vector of intervals after merging



Example Input
Input 1:

Given intervals [1, 3], [6, 9] insert and merge [2, 5] .
Input 2:

Given intervals [1, 3], [6, 9] insert and merge [2, 6] .


Example Output
Output 1:

 [ [1, 5], [6, 9] ]
Output 2:

 [ [1, 9] ]


Example Explanation
Explanation 1:

(2,5) does not completely merge the given intervals
Explanation 2:

(2,6) completely merges the given intervals
"""

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def isOverLapping(self,a,b):
        
        si = a.start
        ei = a.end
        s = b.start
        e = b.end
        if s > ei or si > e:
            return False
        return True
    def solve(self, A,B):
        n = len(A)
        ans = []
        isNewAdded = False
        for i in range(n):
            if self.isOverLapping(A[i],B):
                B = Interval(min(A[i].start,B.start),max(A[i].end,B.end))
            else:
                if A[i].start > B.end and isNewAdded is False:
                    ans.append(B)
                    isNewAdded = True
                ans.append(A[i])
        if isNewAdded is False:
            ans.append(B)
        return ans

    def insert(self, intervals, newInterval):
        return self.solve(intervals,newInterval)
