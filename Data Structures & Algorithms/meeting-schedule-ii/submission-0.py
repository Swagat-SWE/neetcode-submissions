"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        startTimes = []
        endTimes = []

        for each in intervals:
            startTimes.append(each.start)
            endTimes.append(each.end)
        
        startTimes.sort()
        endTimes.sort()

        startPtr = 0
        endPtr = 0
        res = 0
        ct = 0
        while  startPtr != len(intervals):
            if startTimes[startPtr] < endTimes[endPtr]:
                ct += 1
                startPtr += 1
            else: 
                ct -= 1
                endPtr += 1
            res = max(res, ct)
        return res
        