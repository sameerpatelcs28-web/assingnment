class Solution:
    def subsets(self, nums):
        ans = []

        def backtrack(index, path):
            if index == len(nums):
                ans.append(path[:])
                return

            # pick
            path.append(nums[index])
            backtrack(index + 1, path)

            # not pick
            path.pop()
            backtrack(index + 1, path)

        backtrack(0, [])
        return ans
