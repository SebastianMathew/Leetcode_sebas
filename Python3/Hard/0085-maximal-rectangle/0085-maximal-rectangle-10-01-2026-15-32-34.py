class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        n = len(matrix[0])+1
        arr = [0]*n
        max_area = 0
        for row in matrix:
            for i in range(n-1):
                if row[i] == '1':
                    arr[i]+=1
                else:
                    arr[i] = 0

            stack = []

            for i in range(n):
                while stack and arr[i]<arr[stack[-1]]:
                    idx = stack.pop()
                    height = arr[idx]
                    width = i if not stack else i-stack[-1]-1
                    area = height*width
                    max_area = max(max_area, area)
                stack.append(i)

        return max_area
