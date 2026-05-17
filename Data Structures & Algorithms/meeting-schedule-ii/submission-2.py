"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        times = []

        for each in intervals:
            times.append((each.start, 1))
            times.append((each.end, -1))

        
        times.sort()

        res = 0
        ct = 0
        for each in times:
            ct += each[1]
            res = max(res, ct)
        return res
        