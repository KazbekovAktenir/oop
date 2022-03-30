
array = [1, 2, 3]


class Solution:
    def PlusOne(digits: list) -> list:
        array.append(array[-1] + 1)
        array.remove(array[-2])

Solution.PlusOne(array)
print(array)
