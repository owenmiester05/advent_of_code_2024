# In the future I will use regex
total = 0
enabled = True
with open('day_3/input.txt', 'r') as f:
    content = f.read()
    for i in range(len(content)):
        if content[i: i+4] == "do()":
            enabled = True
        elif content[i: i+7] == "don't()":
            enabled = False
        if enabled:
            if content[i:i+4] == "mul(":
                j = i + 5 
                while content[j] != ")" and j < len(content) - 1:
                    j += 1
                possible = content[i+4: j].split(',')
                if len(possible) == 2:
                    try:
                        total += int(possible[0]) * int(possible[1])
                    except ValueError:
                        pass  
print(total)
            

