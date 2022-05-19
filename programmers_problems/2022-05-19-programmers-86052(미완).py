from collections import defaultdict


def solution(grid):
    n = len(grid)
    m = len(grid[0])
    dir_dict = {
        0: (-1, 0),
        1: (0, 1),
        2: (1, 0),
        3: (0, -1)
    }

    def next_dir(row, col, direction_number):
        next_dir_num = 0
        s = grid[row][col]
        if s == 'S':
            next_dir_num = direction_number
        elif s == 'L':
            next_dir_num = direction_number - 1 if direction_number - 1 >= 0 else 3
        elif s == 'R':
            next_dir_num = (direction_number + 1) % 4
        return next_dir_num

    results = []
    for num in range(4):
        discovered = defaultdict(int)
        stk = [(0, 0, num)]
        while stk:
            r, c, dir_num = stk.pop()
            discovered[(r, c, dir_num)] += 1
            nr, nc = r + dir_dict[dir_num][0], c + dir_dict[dir_num][1]
            if 0 > nr:
                nr = n - 1
            elif n <= nr:
                nr = 0
            elif 0 > nc:
                nc = m - 1
            elif m <= nc:
                nc = 0
            n_dir_num = next_dir(nr, nc, dir_num)
            if discovered[(nr, nc, n_dir_num)]:
                if discovered not in results:
                    results.append(discovered)
                break
            else:
                stk.append((nr, nc, n_dir_num))

    answer = []
    for result in results:
        answer.append(len(result))

    answer.sort
    print(answer)
    return answer

solution(['SS', 'SS'])