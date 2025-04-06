def solve():
    n = int(input())
    tests = []
    for _ in range(n):
        tests.append(input().split())

    examples = []
    regular = []
    for i in range(n):
        if tests[i][1] == '1':
            examples.append((tests[i][0], i))
        else:
            regular.append((tests[i][0], i))

    moves = []
    
    e = len(examples)

    # Move examples to 1...e
    for i in range(e):
        if examples[i][0] != str(i + 1):
            if any(test[0] == str(i + 1) for test in tests):
                
                found = False
                for j in range(n):
                    if tests[j][0] not in [str(k+1) for k in range(n)]:
                         moves.append(f"move {tests[j][0]} temp{j}")
                         tests[j][0] = f"temp{j}"
                         found = True
                         break
                if not found:
                    moves.append(f"move {tests[0][0]} temp")
                    tests[0][0] = "temp"
                
                found_index = -1
                for j in range(len(tests)):
                    if tests[j][0] == str(i+1):
                        found_index = j
                        break
                
                moves.append(f"move {examples[i][0]} temp1")
                moves.append(f"move {str(i+1)} {examples[i][0]}")
                moves.append(f"move temp1 {str(i+1)}")
                
                for p in range(len(examples)):
                    if examples[p][0] == examples[i][0]:
                        examples[p] = (str(i+1), examples[p][1])
                        break
                
                for p in range(len(tests)):
                    if tests[p][0] == examples[i][0]:
                        tests[p][0] = str(i+1)
                        break
                
            else:
                moves.append(f"move {examples[i][0]} {i+1}")
                for p in range(len(examples)):
                    if examples[p][0] == examples[i][0]:
                        examples[p] = (str(i+1), examples[p][1])
                        break
                for p in range(len(tests)):
                    if tests[p][0] == examples[i][0]:
                        tests[p][0] = str(i+1)
                        break

    # Move regular tests to e+1...n
    for i in range(len(regular)):
        if regular[i][0] != str(e + i + 1):
            if any(test[0] == str(e + i + 1) for test in tests):
                found = False
                for j in range(n):
                    if tests[j][0] not in [str(k+1) for k in range(n)]:
                         moves.append(f"move {tests[j][0]} temp{j}")
                         tests[j][0] = f"temp{j}"
                         found = True
                         break
                if not found:
                     moves.append(f"move {tests[0][0]} temp")
                     tests[0][0] = "temp"
                
                found_index = -1
                for j in range(len(tests)):
                    if tests[j][0] == str(e + i + 1):
                        found_index = j
                        break
                
                moves.append(f"move {regular[i][0]} temp1")
                moves.append(f"move {str(e + i + 1)} {regular[i][0]}")
                moves.append(f"move temp1 {str(e + i + 1)}")

                for p in range(len(regular)):
                    if regular[p][0] == regular[i][0]:
                        regular[p] = (str(e + i + 1), regular[p][1])
                        break

                for p in range(len(tests)):
                    if tests[p][0] == regular[i][0]:
                        tests[p][0] = str(e + i + 1)
                        break
            else:
                moves.append(f"move {regular[i][0]} {e + i + 1}")
                for p in range(len(regular)):
                    if regular[p][0] == regular[i][0]:
                        regular[p] = (str(e + i + 1), regular[p][1])
                        break
                for p in range(len(tests)):
                    if tests[p][0] == regular[i][0]:
                        tests[p][0] = str(e + i + 1)
                        break

    print(len(moves))
    for move in moves:
        print(move)

solve()