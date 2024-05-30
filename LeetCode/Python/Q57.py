class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        answers = []

        i = 0

        while(i < len(intervals) and intervals[i][1] < newInterval[0]):
            answers.append(intervals[i])
            i += 1

        if(i == len(intervals) or intervals[i][0] > newInterval[1]):
            answers.append(newInterval)
        else:
            while(i < len(intervals) and intervals[i][0] <= newInterval[1]):
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])
                i += 1

            answers.append(newInterval)

        while(i < len(intervals)):
            answers.append(intervals[i])
            i += 1

        return answers
            