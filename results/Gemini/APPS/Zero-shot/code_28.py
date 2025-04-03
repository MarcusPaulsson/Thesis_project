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

    # Move examples to 1, 2, ..., e
    for i in range(e):
        if examples[i][0] != str(i + 1):
            
            # Check if i+1 is occupied by an example or regular test
            occupied = False
            for ex in examples:
                if ex[0] == str(i+1):
                    occupied = True
                    break
            if not occupied:
                for reg in regular:
                    if reg[0] == str(i+1):
                        occupied = True
                        break
            
            if occupied:
                # Move to temporary name
                temp_name = str(n + moves.__len__()+1)
                while True:
                    conflict = False
                    for ex in examples:
                        if ex[0] == temp_name:
                            conflict = True
                            break
                    if not conflict:
                        for reg in regular:
                            if reg[0] == temp_name:
                                conflict = True
                                break
                    if not conflict and temp_name not in [move[1] for move in moves]:
                        break
                    else:
                        temp_name = str(int(temp_name) + 1)
                moves.append((examples[i][0], temp_name))
                moves.append((str(i+1), examples[i][0]))
                moves.append((temp_name, str(i + 1)))
            else:
                moves.append((examples[i][0], str(i + 1)))

    # Move regular tests to e+1, e+2, ..., n
    for i in range(len(regular)):
        if regular[i][0] != str(e + i + 1):

            # Check if e+i+1 is occupied by an example or regular test
            occupied = False
            for ex in examples:
                if ex[0] == str(e+i+1):
                    occupied = True
                    break
            if not occupied:
                for reg in regular:
                    if reg[0] == str(e+i+1):
                        occupied = True
                        break

            if occupied:
                # Move to temporary name
                temp_name = str(n + moves.__len__()+1)
                while True:
                    conflict = False
                    for ex in examples:
                        if ex[0] == temp_name:
                            conflict = True
                            break
                    if not conflict:
                        for reg in regular:
                            if reg[0] == temp_name:
                                conflict = True
                                break
                    if not conflict and temp_name not in [move[1] for move in moves]:
                        break
                    else:
                        temp_name = str(int(temp_name) + 1)
                moves.append((regular[i][0], temp_name))
                moves.append((str(e+i+1), regular[i][0]))
                moves.append((temp_name, str(e+i+1)))
            else:
                moves.append((regular[i][0], str(e + i + 1)))

    print(len(moves))
    for move in moves:
        print("move", move[0], move[1])

solve()