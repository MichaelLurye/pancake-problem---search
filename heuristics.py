

def base_heuristic(_pancake_state):
    state = _pancake_state.get_state_lst()
    check = len(state)
    res = 0
    for i in range(0,len(state)):
        if state[i]!= check:
            return sum(state[i:])
        check-=1    
    return res


def advanced_heuristic(_pancake_state):
    state = _pancake_state.get_state_lst()
    check = len(state)
    res = 0
    seen = 0
    for i in range(0,len(state)):
        if i == len(state)-1:
            return sum(state[i:])
        if state[i]== check and seen == 0:
            check -=1
            continue
        else:
            seen =1
        if state[i] != check:
            continue
        return sum(state[i:])+ sum(state[len(state)+1-check:])
        
    return res


