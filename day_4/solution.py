with open('day_4\input.txt', 'r') as f:
    inp = [[char for char in line.strip()] for line in f.readlines()]

height = len(inp) - 1
width = len(inp[0]) - 1
current_sum = 0
part_two_sum = 0

def check_horizontal_right(i, j):
    if i+3 <= width:
        if ''.join(inp[i][j] + inp[i+1][j] + inp[i+2][j] + inp[i+3][j]) == "XMAS":
            return 1
    return 0  

def check_horizontal_left(i, j):
    if i-3 >= 0:
        if ''.join(inp[i][j] + inp[i-1][j] + inp[i-2][j] + inp[i-3][j]) == "XMAS":
            return 1
    return 0 
 
def check_vertical_up(i, j):
    if j-3 >= 0:
        if ''.join(inp[i][j] + inp[i][j-1] + inp[i][j-2] + inp[i][j-3]) == "XMAS":
            return 1
    return 0  

def check_vertical_down(i, j):
    if j+3 <= height:
        if ''.join(inp[i][j] + inp[i][j+1] + inp[i][j+2] + inp[i][j+3]) == "XMAS":
            return 1
    return 0

def check_upper_right_diagonal(i, j):
    if i+3 <= width and j-3 >= 0:
        if ''.join(inp[i][j] + inp[i+1][j-1] + inp[i+2][j-2] + inp[i+3][j-3]) == "XMAS":
            return 1
    return 0  

def check_lower_right_diagonal(i, j):
    if i+3 <= width and j+3 <= height:
        if ''.join(inp[i][j] + inp[i+1][j+1] + inp[i+2][j+2] + inp[i+3][j+3]) == "XMAS":
            return 1
    return 0  

def check_lower_left_diagonal(i, j):
    if i-3 >= 0 and j+3 <= height:
        if ''.join(inp[i][j] + inp[i-1][j+1] + inp[i-2][j+2] + inp[i-3][j+3]) == "XMAS":
            return 1
    return 0  

def check_upper_left_diagonal(i, j):
    if i-3 >= 0 and j-3 >= 0:
        if ''.join(inp[i][j] + inp[i-1][j-1] + inp[i-2][j-2] + inp[i-3][j-3]) == "XMAS":
            return 1
    return 0 

def check_upper_left_diagonal(i, j):
    if i-3 >= 0 and j-3 >= 0:
        if ''.join(inp[i][j] + inp[i-1][j-1] + inp[i-2][j-2] + inp[i-3][j-3]) == "XMAS":
            return 1
    return 0 

# part two methods
def check_right_up_diagonal(i, j):
    if i-1 >= 0 and i+1 <= width and j-1 >= 0 and j+1 <= height:
        join_string = ''.join(inp[i-1][j+1] + inp[i][j] + inp[i+1][j-1])
        if  join_string == "MAS" or join_string == "SAM":
            return 1
    return 0  

def check_right_down_diagonal(i, j):
    if i-1 >= 0 and i+1 <= width and j-1 >= 0 and j+1 <= height:
        join_string = ''.join(inp[i-1][j-1] + inp[i][j] + inp[i+1][j+1])
        if  join_string == "MAS" or join_string == "SAM":
            return 1
    return 0  

def check_positions(i, j):
    return check_horizontal_right(i, j) + check_horizontal_left(i, j) + check_vertical_up(i, j) + check_vertical_down(i, j) + check_upper_right_diagonal(i, j) + check_lower_right_diagonal(i, j) + \
        check_lower_left_diagonal(i, j) + check_upper_left_diagonal(i, j)

def part_two(i, j):
    return check_right_down_diagonal(i, j) and check_right_up_diagonal(i, j)

for i in range(len(inp[0])):
    for j in range(len(inp)):
        current_sum += check_positions(i, j)
        part_two_sum += part_two(i, j)
print(current_sum)
print(part_two_sum)
