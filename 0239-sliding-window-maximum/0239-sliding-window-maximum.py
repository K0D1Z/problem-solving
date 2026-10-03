class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        # BOZO APPROACH (O((n-k)*k))
        # res = []
        # l, r = 0, k
        # while r <= len(nums):
        #     # res.append(max(nums[l:r]))
        #     l += 1
        #     r += 1
        # return res


        '''
        OPTIMAL MONOTONIC DECREASING QUEUE SOLUTION
        '''
        res = []
        q = collections.deque()
        l = r = 0
        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            if q[0] < l:
                q.popleft()
            if (r + 1 >= k):
                res.append(nums[q[0]])
                l += 1
            r += 1 
        return res
        
