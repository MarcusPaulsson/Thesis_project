def solve():
    n = int(input())
    files = []
    for _ in range(n):
        files.append(input().split())

    examples = []
    regular = []
    for i in range(n):
        if files[i][1] == '1':
            examples.append((files[i][0], i))
        else:
            regular.append((files[i][0], i))

    moves = []
    e = len(examples)

    def find_unused_temp_file(files):
        temp_file = "temp"
        temp_count = 0
        while True:
            is_used = False
            for f in files:
                if f[0] == temp_file:
                    is_used = True
                    break
            if not is_used:
                return temp_file
            temp_count += 1
            temp_file = "temp" + str(temp_count)

    for i in range(e):
        if examples[i][0] != str(i + 1):
            target_file = str(i + 1)
            target_index = -1
            for j in range(n):
                if files[j][0] == target_file:
                    target_index = j
                    break
            
            if target_index != -1:
                if target_index != examples[i][1]:
                  temp_file = find_unused_temp_file(files)
                  moves.append("move " + target_file + " " + temp_file)
                  files[target_index][0] = temp_file
            
            moves.append("move " + examples[i][0] + " " + str(i + 1))
            files[examples[i][1]][0] = str(i + 1)

    for i in range(len(regular)):
        if regular[i][0] != str(e + i + 1):
            target_file = str(e + i + 1)
            target_index = -1
            for j in range(n):
                if files[j][0] == target_file:
                    target_index = j
                    break
            
            if target_index != -1:
                if target_index != regular[i][1]:
                    temp_file = find_unused_temp_file(files)
                    moves.append("move " + target_file + " " + temp_file)
                    files[target_index][0] = temp_file
            
            moves.append("move " + regular[i][0] + " " + str(e + i + 1))
            files[regular[i][1]][0] = str(e + i + 1)

    print(len(moves))
    for move in moves:
        print(move)

solve()