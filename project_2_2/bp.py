import math
import random
import pickle

random.seed(0)


# 生成[a,b)之间的随机数
def rand(a, b):
    return (b - a) * random.random() + a


# 用tanh函数作为激活函数
def sigmoid(x):
    return math.tanh(x)


# tanh的导数
def dsigmoid(y):
    return 1.0 - y ** 2


class Unit:
    def __init__(self, length):
        self.weight = [rand(-0.2, 0.2) for i in range(length)]
        self.change = [0.0] * length
        self.threshold = rand(-0.2, 0.2)
    # 正向传播 计算预期输出
    def calc(self, sample):
        self.sample = sample[:]
        partsum = sum([i * j for i, j in zip(self.sample, self.weight)]) - self.threshold
        self.output = sigmoid(partsum)
        return self.output

    # 反向传播，修改权重
    def update(self, diff, rate=0.5, factor=0.1):
        change = [rate * x * diff + factor * c for x, c in zip(self.sample, self.change)]
        self.weight = [w + c for w, c in zip(self.weight, change)]
        self.change = [x * diff for x in self.sample]

    def get_weight(self):
        return self.weight[:]

    def set_weight(self, weight):
        self.weight = weight[:]


class Layer:
    def __init__(self, input_length, output_length):
        self.units = [Unit(input_length) for i in range(output_length)]
        self.output = [0.0] * output_length
        self.ilen = input_length

    def calc(self, sample):
        self.output = [unit.calc(sample) for unit in self.units]
        return self.output[:]

    def update(self, diffs, rate=0.5, factor=0.1):
        for diff, unit in zip(diffs, self.units):
            unit.update(diff, rate, factor)

    def get_error(self, deltas):
        def _error(deltas, j):
            return sum([delta * unit.weight[j] for delta, unit in zip(deltas, self.units)])

        return [_error(deltas, j) for j in range(self.ilen)]

    def get_weights(self):
        weights = {}
        for key, unit in enumerate(self.units):
            weights[key] = unit.get_weight()
        return weights

    def set_weights(self, weights):
        for key, unit in enumerate(self.units):
            unit.set_weight(weights[key])


class BPNNet:
    def __init__(self, ni, nh, no):
        # 各个层的节点数量
        self.ni = ni + 1  #  bias node
        self.nh = nh
        self.no = no
        self.hlayer = Layer(self.ni, self.nh)
        self.olayer = Layer(self.nh, self.no)

    def calc(self, inputs):
        if len(inputs) != self.ni - 1:
            raise ValueError('wrong number of inputs')

        # input activations
        self.ai = inputs[:] + [1.0]

        # hidden activations
        self.ah = self.hlayer.calc(self.ai)
        # output activations
        self.ao = self.olayer.calc(self.ah)

        return self.ao[:]

    def update(self, targets, rate, factor):
        if len(targets) != self.no:
            raise ValueError('wrong number of target values')

        # 计算输出层误差
        output_deltas = [dsigmoid(ao) * (target - ao) for target, ao in zip(targets, self.ao)]

        # 计算隐层误差
        hidden_deltas = [dsigmoid(ah) * error for ah, error in zip(self.ah, self.olayer.get_error(output_deltas))]

        # 更新隐层-输出层权重
        self.olayer.update(output_deltas, rate, factor)

        # 更新输入层-隐层权重
        self.hlayer.update(hidden_deltas, rate, factor)
        # 返回错误率
        return sum([0.5 * (t - o) ** 2 for t, o in zip(targets, self.ao)])

    def test(self, patterns):
        for p in patterns:
            print(p[0], '->', self.calc(p[0]))

    def train(self, patterns, iterations=1000, N=0.5, M=0.1):
        # N: 学习率
        # M: 动量因子
        for i in range(iterations):
            error = 0.0
            for p in patterns:
                inputs = p[0]
                targets = p[1]
                self.calc(inputs)
                error = error + self.update(targets, N, M)
            if i % 100 == 0:
                print('error %-.10f' % error)

    def save_weights(self, fn):
        weights = {
            "olayer": self.olayer.get_weights(),
            "hlayer": self.hlayer.get_weights()
        }
        with open(fn, "wb") as f:
            pickle.dump(weights, f)

    def load_weights(self, fn):
        with open(fn, "rb") as f:
            weights = pickle.load(f)
            self.olayer.set_weights(weights["olayer"])
            self.hlayer.set_weights(weights["hlayer"])


def demo():
    # 异或
    pat = [
        [[0, 0], [0]],
        [[0, 1], [1]],
        [[1, 0], [1]],
        [[1, 1], [0]]
    ]

    # 输入层两个节点 隐层两个节点 输出层1个节点
    n = BPNNet(2, 2, 1)
    # 训练并保存
    n.train(pat)
    # n.save_weights("demo.weights")
    # 测试
    n.test(pat)


if __name__ == '__main__':
    demo()
