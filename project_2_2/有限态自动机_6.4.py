import queue


def trans_states(state, s):
    res = []
    if state == 'S' and s == '0':
        res = ['A']
    elif state == 'S' and s == '1':
        res = ['B', 'C']
    elif state == 'A' and s == '0':
        res = ['A']
    elif state == 'A' and s == '1':
        res = ['B', 'F']
    elif state == 'B' and s == '0':
        res = ['B', 'F']
    elif state == 'C' and s == '0':
        res = ['C']
    elif state == 'C' and s == '1':
        res = ['F']
    else:
        res = ['NULL']
    return res


def is_match(target_x="00100"):
    q = queue.Queue()
    first_s = target_x[0]
    count = 1
    first_state = 'S'
    new_state = trans_states(first_state, first_s)
    for s in new_state:
        q.put(s)
    while ~q.empty():
        length = q.qsize()
        for i in range(length):
            tmp = q.get()
            new_state = trans_states(tmp, target_x[count])
            for ns in new_state:
                if ns == 'NULL':
                    continue
                if count == len(target_x) - 1 and ns == 'F':
                    print('succeed!')
                    return True
                else:
                    q.put(ns)
        count += 1
    print('Fail!')
    return False


is_match()
