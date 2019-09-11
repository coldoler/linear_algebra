class Vector:
    def __init__(self, lst):
        # Make a copy of lst, when lst change, the copy won't
        self._values = list(lst)

    def __add__(self, other):
        assert len(self) == len(other), \
            "Error in adding. Length of vectors must be same."
        # Return a new Vector, the Vector class is immutable
        return Vector([a + b for a, b in zip(self, other)])

    def __sub__(self, other):
        assert len(self) == len(other), \
            "Error in subtracting. Length of vectors must be same."
        return Vector([a - b for a, b in zip(self, other)])

    # 数量乘法，返回 Vector * k 注意顺序重要
    def __mul__(self, k):
        return Vector([k * e for e in self])

    # 数量乘法，右乘，即从右乘，返回 k * Vector, 和__mul__顺序相反
    def __rmul__(self, k):
        return self * k  # 里面调用的还是 __mul__

    def __iter__(self):
        # Return iterator of self, i.e. vector's iterator
        return self._values.__iter__()

    # 向量取正
    def __pos__(self):
        return 1 * self

    # 向量取负
    def __neg__(self):
        return -1 * self

    def __getitem__(self, index):
        return self._values[index]

    # Method to get dimension of vector
    def __len__(self):
        return len(self._values)

    # Method used by system ->>> u
    def __repr__(self):
        return "Vector({})".format(self._values)

    # Method used by client ->>> print(v)
    def __str__(self):
        return "({})".format(", ".join(str(e) for e in self._values))
