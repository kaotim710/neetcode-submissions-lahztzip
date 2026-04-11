"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # 想要知道同時間有多少會議正在開
        # 想像是有一條now的線，去iterate整個meeting room圖
        # start和end各為一個array
        # 只要有重複的，就計數加一
        # iterate the end time first then start time
        # so that won't get overlap
        
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        res, count = 0, 0
        s, e = 0, 0 # are used to iterate each lists
        while s < len(intervals):
            # means no meeting's ended and there are multiple meeting
            if start[s] < end[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1
            res = max(res, count)
        return res



