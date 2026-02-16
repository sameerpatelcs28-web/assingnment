class Solution:
    def combinationSum2(self, nums, target):
        nums.sort()
        result = []

        def dfs(index, curr, total):

            if total == target:
                result.append(curr[:])
                return

            for j in range(index, len(nums)):

                if j > index and nums[j] == nums[j - 1]:
                    continue

                if total + nums[j] > target:
                    break

                curr.append(nums[j])
                dfs(j + 1, curr, total + nums[j])
                curr.pop()

        dfs(0, [], 0)
        return result
