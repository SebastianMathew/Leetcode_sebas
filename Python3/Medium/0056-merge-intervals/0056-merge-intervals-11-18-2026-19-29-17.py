class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key = lambda x:x[0])
        output = [intervals[0]]

        for start, end in intervals[1:]:
            le = output[-1][1]

            if start<=le:
                output[-1][1] = max(end, le)
            else:
                output.append([start,end])

        return output

        