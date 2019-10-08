class Vector:
    def __init__(self, lst):
        self._values = list(lst)

    def __add__(self, another):
        """向量加法，返回结果向量"""
        assert len(self) == len(another), \
            "Error in adding. length of vectors must be same"
        return Vector([a + b for a, b in zip(self,another)])

    def __sub__(self, another):
        """向量减法，返回结果向量"""
        assert len(self) == len(another), \
            "Error in substracting. length of vectors must be same"
        return Vector([a - b for a, b in zip(self, another)])

    def __iter__(self):
        """返回向量的迭代器"""
        return self._values.__iter__()

    def __getitem__(self, index):
        """取向量的第index个元素"""
        return self._values[index]

    def __repr__(self):
        return "Vector({})".format(self._values)

    def __len__(self):
        """返回向量长度（有多少个元素）"""
        return len(self._values)

    def __str__(self):
        return "({})".format(",".join(str(e) for e in self._values))