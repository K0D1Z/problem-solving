class Solution:
    class Solution:
        def minimumCost(self, cost) -> int:
            total_cost = 0
            free_counter = 0
            cost = sorted(cost)
            for i in cost[::-1]:
                if free_counter != 2:
                    total_cost += i
                    free_counter += 1
                else:
                    free_counter = 0
            return total_cost
    # def minimumCost(self, cost) -> int:
    #     total_cost = 0
    #     free_counter = 0
    #     hashmap = defaultdict(int)
    #     for i in cost:
    #         hashmap[i] += 1
    #     list_of_keys = sorted(hashmap.items(), key=lambda x: int(x[0]), reverse=True)
    #     list_of_keys = [i[0] for i in list_of_keys]
    #     for i in list_of_keys:
    #         while hashmap[i] > 0:
    #             if free_counter < 2:
    #                 free_counter += 1
    #                 total_cost += int(i)
    #             else:
    #                 free_counter = 0
    #             hashmap[i] -= 1
    #     return total_cost

