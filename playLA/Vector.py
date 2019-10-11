from ._global import EPSILON
import math

class Vector:
    def __init__(self, lst):
        self._values = list(lst)

    @classmethod
    def zero(cls, dim):
        """返回一个dim维的零向量"""
        return cls([0] * dim)

    def norm(self):
        """返回向量的模"""
        return math.sqrt(sum(e**2 for e in self))
        """e**2表示求e的平方，sqrt是开根函数"""
    def normalize(self):
        """返回向量的单位向量"""
        # return Vector([e / self.norm() for e in self])
        # 这种写法，每次都计算了self.norm()

        # return 1 / self.norm() * Vector(self._values)

        if self.norm() < EPSILON:
            """if self.norm() < EPSILON相当于 if self.norm() == 0，因为浮点数计算有误差，直接等于零不安全"""
            raise ZeroDivisionError("Normalize error! norm is zero")
        return Vector(self._values) / self.norm()

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

    def __mul__(self, k):
        """返回数量乘法的结果向量"""
        return Vector([k * e for e in self])

    def __rmul__(self, k):
        """返回数量乘法的结果向量"""
        return self * k

    def __truediv__(self, k):
        """返回数量除法的结果向量 self / k"""
        return (1 / k) * self

    def __pos__(self):
        """返回向量取正的结果"""
        return 1 * self

    def __neg__(self):
        """返回向量取负的结果"""
        return -1 * self

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