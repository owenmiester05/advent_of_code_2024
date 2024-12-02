count1 = 0
count2 = 0
def is_valid(nums):
    if all(nums[i] < nums[i+1] and nums[i+1] - nums[i] <= 3 for i in range(len(nums)-1)) or \
    all(nums[i] > nums[i+1] and nums[i] - nums[i+1] <= 3 for i in range(len(nums)-1)):
        return 1
    else:
        return 0

def part_2(nums):
    if is_valid(nums): 
        return 1
    else:
        for i in range(len(nums)):
            if is_valid(nums[:i] + nums[i+1:]):
                return 1
    return 0

with open('day_2\input.txt', 'r') as f:
    for line in f.readlines():
        count1 += is_valid(list(map(int, line.split())))
        count2 += part_2(list(map(int, line.split())))
print(count1)
print(count2)