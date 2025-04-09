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
    
    num_examples = len(examples)
    num_regular = len(regular)

    # Move examples to 1, 2, ..., num_examples
    for i in range(num_examples):
        if examples[i][0] != str(i + 1):
            
            if any(files[j][0] == str(i+1) for j in range(n)):
                temp_name = generate_temp_name(files)
                moves.append(f"move {str(i+1)} {temp_name}")
                
                # update files
                for j in range(n):
                    if files[j][0] == str(i+1):
                        files[j][0] = temp_name
                        break
                
            moves.append(f"move {examples[i][0]} {str(i + 1)}")
            
            # update files
            for j in range(n):
                if files[j][0] == examples[i][0]:
                    files[j][0] = str(i+1)
                    break
            
    # Move regular to num_examples + 1, num_examples + 2, ..., n
    for i in range(num_regular):
        if regular[i][0] != str(num_examples + i + 1):
            
            if any(files[j][0] == str(num_examples + i + 1) for j in range(n)):
                temp_name = generate_temp_name(files)
                moves.append(f"move {str(num_examples + i + 1)} {temp_name}")

                # update files
                for j in range(n):
                    if files[j][0] == str(num_examples + i + 1):
                        files[j][0] = temp_name
                        break
                        
            moves.append(f"move {regular[i][0]} {str(num_examples + i + 1)}")
            
            # update files
            for j in range(n):
                if files[j][0] == regular[i][0]:
                    files[j][0] = str(num_examples + i + 1)
                    break
            
    print(len(moves))
    for move in moves:
        print(move)

def generate_temp_name(files):
    import random
    import string
    while True:
        temp_name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
        if not any(files[i][0] == temp_name for i in range(len(files))):
            return temp_name

solve()