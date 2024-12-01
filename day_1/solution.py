from collections import Counter
left_values = []
right_values = []
total_sum = 0
similarity_score = 0
with open('day_1\input.txt', 'r') as f:
    for line in f.readlines():
        left, right = line.split()
        left_values.append(int(left))
        right_values.append(int(right))
    left_values.sort()
    right_values.sort()
    right_counter = Counter(right_values)
    # part 1:
    for i in range(len(right_values)):
        if right_values[i] > left_values[i]:
            total_sum += right_values[i] - left_values[i]
        else:
            total_sum += left_values[i] - right_values[i]
    # part 2:
        similarity_score += left_values[i] * right_counter[left_values[i]]
print(total_sum)
print(similarity_score)
