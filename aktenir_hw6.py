def get_list() -> list:
    return list(range(0, 1_000_000, 2))


class Solution:

    def find_target(self, list, target):
        limit_1 = 0
        limit_2 = len(list)
        a = 0
        while limit_1 <= limit_2:
            a += 1
            midind = (limit_1 + limit_2) // 2
            if list[midind] < target:
                limit_1 = midind + 1
            elif list[midind] > target:
                limit_2 = midind - 1
            else:
                return a


print(Solution().find_target(get_list(), 100))
