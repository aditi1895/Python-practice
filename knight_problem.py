from timeit import timeit

def solution(src, dest):
    def valid_position(x,y):
        if -1 < x < 8 and -1 < y < 8:
            return True
        else:
            return False
    def check_visited(visited_locations, next_location):
        return next_location in visited_locations
    if src==dest:
        return 0
    src_x, src_y = src // 8, src % 8
    dest_x, dest_y = dest // 8, dest % 8
    # print(f"Source ({src_x}, {src_y})")
    # print(f"Jestination ({dest_x}, {dest_y})")
    level_count = {0: [(src_x, src_y)]}
    is_visited = [(src_x, src_y)]
    level = 0
    while True:
        # print(level, level_count[level])
        level += 1
        level_count[level] = []
        for location in level_count[level - 1]:
            # x_dist, y_dist = dest_x - location[0], dest_y - location[1]
            # if x_dist:
            #     x_sign = x_dist // abs(x_dist)
            # else:
            #     x_sign = 1
            # if y_dist:
            #     y_sign = y_dist // abs(y_dist)
            # else:
            #     y_sign = 1
            loc_x, loc_x_minus, loc_y1, loc_y2 = location[0] + 2, location[0] -2, location[1] + 1, location[1] - 1
            if valid_position(loc_x, loc_y1) and not check_visited(is_visited, (loc_x, loc_y1)):
                level_count[level].append((loc_x, loc_y1))
                is_visited.append((loc_x, loc_y1))
            if valid_position(loc_x, loc_y2) and not check_visited(is_visited, (loc_x, loc_y2)):
                level_count[level].append((loc_x, loc_y2))
                is_visited.append((loc_x, loc_y2))
            if valid_position(loc_x_minus, loc_y1) and not check_visited(is_visited, (loc_x_minus, loc_y1)):
                level_count[level].append((loc_x_minus, loc_y1))
                is_visited.append((loc_x_minus, loc_y1))
            if valid_position(loc_x_minus, loc_y2) and not check_visited(is_visited, (loc_x_minus, loc_y2)):
                level_count[level].append((loc_x_minus, loc_y2))
                is_visited.append((loc_x_minus, loc_y2))
            # else:
            loc_x1, loc_x2, loc_y, loc_y_minus = location[0] + 1, location[0] - 1, location[1] + 2, location[1] - 2
            if valid_position(loc_x1, loc_y) and not check_visited(is_visited, (loc_x1, loc_y)):
                level_count[level].append((loc_x1, loc_y))
                is_visited.append((loc_x1, loc_y))
            if valid_position(loc_x2, loc_y) and not check_visited(is_visited, (loc_x2, loc_y)):
                level_count[level].append((loc_x2, loc_y))
                is_visited.append((loc_x2, loc_y))
            if valid_position(loc_x1, loc_y_minus) and not check_visited(is_visited, (loc_x1, loc_y_minus)):
                level_count[level].append((loc_x1, loc_y_minus))
                is_visited.append((loc_x1, loc_y_minus))
            if valid_position(loc_x2, loc_y_minus)  and not check_visited(is_visited, (loc_x2, loc_y_minus)):
                level_count[level].append((loc_x2, loc_y_minus))
                is_visited.append((loc_x2, loc_y_minus))
            if (dest_x, dest_y) in level_count[level]:
                return level
            
print(solution(src=56, dest=56))
print(timeit(lambda: solution(src=56, dest=56), number=100_000))
