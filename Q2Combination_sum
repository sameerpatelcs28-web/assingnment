class Solution:
    def combinationSum(self, nums, target):
        result = []

        def dfs(index, current, total):
            if total == target:
                result.append(list(current))
                return
            if total > target:
                return

            for j in range(index, len(nums)):
                current.append(nums[j])
                dfs(j, current, total + nums[j])
                current.pop()

        dfs(0, [], 0)
        return result
