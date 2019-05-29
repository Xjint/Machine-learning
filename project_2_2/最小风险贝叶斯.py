def get_threshold(W,L):
    return ((L[0][1] - L[1][1]) * W[0][1]) / ((L[1][0] - L[0][0]) * W[0][0])


def get_l_1_2(W):
    return W[0][1] / W[1][1]






W = [[0.9, 0.2],
     [0.1, 0.4]]
L = [[0,6],
     [1,0]]
theta = get_threshold(W, L)
value = get_l_1_2(W)
if(value > theta):
    print("该样本属于w1 正常")
else:
    print("该样本属于w2 异常")
