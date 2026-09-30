class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        head = 0
        tail = len(numbers) - 1
        while head < tail:
            addition = numbers[head] + numbers[tail]
            if addition == target:
                return [head + 1, tail + 1]
            elif addition < target:
                head += 1
            else:
                tail -= 1
            
        return [-1, -1]