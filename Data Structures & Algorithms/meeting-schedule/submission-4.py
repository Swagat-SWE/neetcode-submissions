"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda x: x.start)
        prevEnd = float("-inf")
        for each in intervals:
            if each.start < prevEnd:
                return False
            prevEnd = each.end
        return True
