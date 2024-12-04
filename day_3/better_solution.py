import re
enabled = True
total_sum = 0
with open('day_3/input.txt', 'r') as f:
    content = f.read()
    matches = re.findall(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))", content)
    for match in matches:
        if match[2]:
            enabled = True
        if match[3]:
            enabled = False
        if enabled and match[0] and match[1]:
                total_sum += int(match[0]) * int(match[1]) 
print(total_sum)

