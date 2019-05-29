class wenfa:
    def __init__(self, _vn, _vt, _p, _s = 'S'):
        self.vn = _vn
        self.vt = _vt
        self.p = _p
        self.s = _s


class Machine:
    def __init__(self,_sigma, _Q,_delta,_q0= 'S',_F= 'F' ):
        self.sigma = _sigma
        self.Q = _Q
        self.delta = _delta
        self.q0 = _q0
        self.F = _F

    def show(self):
        print("sigma:" + str(self.sigma))
        print("Q:" + str(self.Q))
        print("delta:" + str(self.delta))
        print("q0:" + str(self.q0))
        print("F:" + str(self.F))


def trans(wf):
    _sigma = wf.vt
    _Q = wf.vn
    _Q.append('F')
    _delta = []
    for p in wf.p:
        if len(p[1]) == 1:
            p[1] += 'F'
        a = 'delta({},{})={}'.format(p[0],p[1][0],p[1][1])
        _delta.append(a)

    return _sigma, _Q, _delta


_vn = ['S','B']
_vt = ['a','b']
_p = [
    ['S','aB'],
    ['B','aB'],
    ['B','bS'],
    ['B','a']
]
G = wenfa(_vn, _vt, _p)
_sigma, _Q, _delta = trans(G)
machine = Machine(_sigma, _Q, _delta)
machine.show()