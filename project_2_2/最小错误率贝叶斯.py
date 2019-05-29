def make_dic(W):
    delta = 0
    index = 0
    for i, w in enumerate(W):
        tmp = w[0] * w[1]
        if tmp > delta:
            delta = tmp
            index = i
    return index


W = [[0.9, 0.2],
     [0.1, 0.4]]
index = make_dic(W)
print("该样本属于w" + str(index + 1))
