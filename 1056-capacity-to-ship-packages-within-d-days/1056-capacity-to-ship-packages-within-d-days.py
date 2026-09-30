class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        def isTimeExceeded(capacity: int):
            days_counter = 1
            temp_capacity = capacity
            for w in weights:
                if temp_capacity - w >= 0:
                    temp_capacity -= w
                else:
                    days_counter += 1
                    if days_counter > days:
                        print('True', days_counter, w, 'capacity:', capacity)
                        return True
                    temp_capacity = capacity - w
            print('False', days_counter, 'capacity:', capacity)
            return False
        
        l = max(weights)
        r = sum(weights)
        min_days = float('inf')
        while l <= r:
            m = (l + r) // 2
            if not isTimeExceeded(m):
                min_days = min(min_days, m)
                r = m - 1
            else:
                l = m + 1
        return min_days


        