def solve():
    n = int(input())
    f = list(map(int, input().split()))
    
    givers = list(range(1, n + 1))
    receivers = list(range(1, n + 1))
    
    for gift in f:
        if gift != 0:
            if gift in receivers:
                receivers.remove(gift)
    
    zeros_indices = [i for i, x in enumerate(f) if x == 0]
    
    for i, index in enumerate(zeros_indices):
        giver = givers[index]
        
        if len(receivers) > 0:
            potential_receiver = receivers[0]
            
            if potential_receiver != giver:
                f[index] = potential_receiver
                receivers.remove(potential_receiver)
            else:
                if len(receivers) > 1:
                    potential_receiver = receivers[1]
                    f[index] = potential_receiver
                    receivers.remove(potential_receiver)
                else:
                    # Swap with another zero
                    for j in range(len(zeros_indices)):
                        if j != i:
                            
                            other_index = zeros_indices[j]
                            
                            temp = f[index]
                            f[index] = receivers[0]
                            f[other_index] = givers[index]

                            if givers[index] != f[other_index] and receivers[0]!=givers[index]:
                                f[other_index] = receivers[0]
                                f[index] = givers[other_index]
                                
                                if givers[other_index] != f[index]:
                                    
                                    if len(receivers) > 1:
                                        
                                        
                                        if len(receivers) > 0:
                                            potential_receiver = receivers[0]
                                            
                                            if potential_receiver != givers[index]:
                                                f[index] = potential_receiver
                                                receivers.remove(potential_receiver)
                                                break
                                            else:
                                                
                                                if len(receivers) > 1:
                                                    potential_receiver = receivers[1]
                                                    f[index] = potential_receiver
                                                    receivers.remove(potential_receiver)
                                                    break
                                    
                                    
                                    
                                    
                                
                                break
                            
                            else:
                                
                                
                                f[other_index] = 0
                                f[index] = 0
                                
                                
                                
                                
                    
    
    print(*f)

solve()