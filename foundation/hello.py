# 1
def twoSum(nums: List[int], target: int) -> List[int]:
    seen = {}
    for i, num in enumerate(nums):
        tmp = target - num
        if tmp in seen:
            return [seen[tmp], i]
        seen[num] = i
    return []

# 1480
def runningSum(nums: List[int]) -> List[int]:
    for i in range(len(nums) - 1):
        nums[i+1] += nums[i]
    return nums

# 709
def toLowerCase(s: str) -> str:
    result = []
    for ch in s:
        if 'A' <= ch <= 'Z':
            ch = chr(ord(ch) + 32)
        result.append(ch)
    return "".join(result)

nums_1 = [1,2,3,4]
print(runningSum(nums_1))

nums_2 = [2,7,11,15]
print(twoSum(nums_2, 9))

print(toLowerCase("Hello"))



