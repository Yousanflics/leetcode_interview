# 252 easy 是否可以参加会议
class Solution:
    def canAttendMeetings(intervals):
        intervals.sort(key=lambda x:x[0])
        for i in range(1, len(intervals)):
            # 检查是否有重叠
            if intervals[i][0] < intervals[i-1][1]:
                return False
        return True
