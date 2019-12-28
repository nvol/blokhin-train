class Arr:
    def __init__(self, length=None, default_value=None, lst=None):
        self.arr = list()
        if lst is not None:
            self.arr = lst
        else:
            if default_value is None:
                default_value = 0.0
            if length is not None:
                self.arr = [default_value for _ in range(length)]
    
    def set_elem(self, ix, val):
        if type(ix) is tuple and len(ix) == 2: #TODO: n-dim
            ii, ij = ix
            try:
                while ii >= len(self.arr):
                    self.arr.append(Arr())
                self.arr[ii].set_elem(ij, val)
            except:
                self.arr[ii] = Arr()
                self.arr[ii].set_elem(ij, val)
            return self.arr[ii](ij)
        ix -= 1
        while ix >= len(self.arr):
            self.arr.append(0.0)
        self.arr[ix] = val
        return self.arr[ix]
    
    def get_elem(self, ix):
        ix -= 1
        while ix >= len(self.arr):
            self.arr.append(0.0)
        return self.arr[ix]

    def __call__(self, ix):
        if type(ix) is tuple and len(ix) == 2:
            ii, ij = ix
            assert((ii >= 1) and (ij >= 1))
            ret = None
            try:
                ret = self.get_elem(ii).get_elem(ij)
            except: # Exception as e1:
                # print('exception-1:', str(e1))
                try:
                    ret = self.get_elem(ii)[ij-1]
                except: # Exception as e2:
                    pass # print('exception-2:', str(e2))
            return ret
        assert(ix >= 1)
        return self.get_elem(ix)

    def show(self):
        print([val for val in self.arr])

    def __repr__(self):
        return str([val for val in self.arr])

    def __iter__(self):
        for val in self.arr:
            yield val

    def enumerate(self):
        ix = 1
        for val in self.arr:
            yield ix, val
            ix += 1
    
    def __len__(self):
        return len(self.arr)

'''
a1 = Arr()
a2 = Arr()
a3 = Arr()
a4 = Arr()
a5 = Arr()
a6 = Arr()
a7 = Arr()
h = 0.1
h1 = h/2
nu = 10

a1.set_elem(1, 1)
a3.set_elem(1, 2)
a2.set_elem(1, 3)
a4.set_elem(1, 4)

for j in range(10):

    for i in range(1, nu+1):
        a6.set_elem(i, a3(i))
        a3.set_elem(i, a1(i))
        a1.set_elem(i, a3(i) + (3 * a2(i) - a4(i)) * h1)
        a5.set_elem(i, a1(i))
        a7.set_elem(i, a4(i))
        a4.set_elem(i, a2(i))

    print(a1(1), a2(1), a3(1), a4(1), a5(1), a6(1), a7(1))

    # sprav()

    for i in range(1, nu+1):
        a1.set_elem(i, a3(i) + (a4(i) + a2(i)) * h1)

    # sprav()
'''