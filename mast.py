__version__ = "1.1.1"
__author__ = "jjy.ly"
class Mast:
    def __init__(self,*x):
        if len(x) == 1 and isinstance(x[0], (list, tuple)):
            self.x1 = list(x[0])
        elif len(x) == 1 and isinstance(x[0], dict):
            self.x1 = list(x[0].items())
        else:
            self.x1 = list(x)
    def __add__(self, other):
        return Mast(*self.x1, *other.x1)
    def __iter__(self):
        def flatten(items):
            for item in items:
                if isinstance(item, Mast):
                    yield from flatten(item.x1)
                elif isinstance(item, (list, tuple)):
                    yield from flatten(item)
                else:
                    yield item
        return flatten(self.x1)
    def __len__(self):
        return len(self.x1)
    def __setitem__(self, a, b):
            self.x1[a] = b 
    def __str__(self):
        return str(self.x1)
    def __getitem__(self, a):
        return self.x1[a]
    def __delitem__(self, a):
        del self.x1[a]
    def __eq__(self, value):
        return self.x1 == value.x1
    def __ne__(self, value):
        return self.x1 != value.x1
    def __gt__(self, value):
        return self.x1 > value.x1
    def __ge__(self, value):
        return self.x1 >= value.x1
    def __lt__(self, value):
        return self.x1 < value.x1
    def __le__(self, value):
        return self.x1 <= value.x1
    def __contains__(self, item):
        return item in self.x1
    def __reversed__(self):
        return Mast(*reversed(self.x1))
    def __call__(self, *args, **kwargs):
        return Mast(*args)
    def __bool__(self):
        return bool(self.x1)
    def __hash__(self):
        return hash(tuple(self.x1))
    def __copy__(self):
        return Mast(*self.x1)
    def __deepcopy__(self, memo):
        from copy import deepcopy
        return Mast(*[deepcopy(x, memo) for x in self.x1])
    def __mul__(self, other):
        if isinstance(other, int):
            return Mast(*self.x1 * other)
        elif isinstance(other, Mast):
            return Mast(*[a * b for a, b in zip(self.x1, other.x1)])
        else:
            raise TypeError("Unsupported operand type(s) for *: 'Mast' and '{}'".format(type(other).__name__))
    def __rmul__(self, other):
        return self.__mul__(other)
    def __truediv__(self, other):
        if isinstance(other, int):
            return Mast(*[x / other for x in self.x1])
        elif isinstance(other, Mast):
            return Mast(*[a / b for a, b in zip(self.x1, other.x1)])
        else:
            raise TypeError("Unsupported operand type(s) for /: 'Mast' and '{}'".format(type(other).__name__))
    def __rtruediv__(self, other):
        if isinstance(other, int):
            return Mast(*[other / x for x in self.x1])
        elif isinstance(other, Mast):
            return Mast(*[a / b for a, b in zip(other.x1, self.x1)])
        else:
            raise TypeError("Unsupported operand type(s) for /: '{}' and 'Mast'".format(type(other).__name__))
    def __mod__(self, other):
        if isinstance(other, int):
            return Mast(*[x % other for x in self.x1])
        elif isinstance(other, Mast):
            return Mast(*[a % b for a, b in zip(self.x1, other.x1)])
        else:
            raise TypeError("Unsupported operand type(s) for %: 'Mast' and '{}'".format(type(other).__name__))
    def __rmod__(self, other):
        if isinstance(other, int):
            return Mast(*[other % x for x in self.x1])
        elif isinstance(other, Mast):
            return Mast(*[a % b for a, b in zip(other.x1, self.x1)])
        else:
            raise TypeError("Unsupported operand type(s) for %: '{}' and 'Mast'".format(type(other).__name__))
    def __pow__(self, other):
        if isinstance(other, int):
            return Mast(*[x ** other for x in self.x1])
        elif isinstance(other, Mast):
            return Mast(*[a ** b for a, b in zip(self.x1, other.x1)])
        else:
            raise TypeError("Unsupported operand type(s) for **: 'Mast' and '{}'".format(type(other).__name__))
    def __rpow__(self, other):
        if isinstance(other, int):
            return Mast(*[other ** x for x in self.x1])
        elif isinstance(other, Mast):
            return Mast(*[a ** b for a, b in zip(other.x1, self.x1)])
        else:
            raise TypeError("Unsupported operand type(s) for **: '{}' and 'Mast'".format(type(other).__name__))
    def __floordiv__(self, other):
        if isinstance(other, int):
            return Mast(*[x // other for x in self.x1])
        elif isinstance(other, Mast):
            return Mast(*[a // b for a, b in zip(self.x1, other.x1)])
        else:
            raise TypeError("Unsupported operand type(s) for //: 'Mast' and '{}'".format(type(other).__name__))
    def __rfloordiv__(self, other):
        if isinstance(other, int):
            return Mast(*[other // x for x in self.x1])
        elif isinstance(other, Mast):
            return Mast(*[a // b for a, b in zip(other.x1, self.x1)])
        else:
            raise TypeError("Unsupported operand type(s) for //: '{}' and 'Mast'".format(type(other).__name__))
    def __neg__(self):
        return Mast(*[-x for x in self.x1])
    def __pos__(self):
        return Mast(*[+x for x in self.x1])
    def __abs__(self):
        return Mast(*[abs(x) for x in self.x1])
    def __round__(self, n=None):
        return Mast(*[round(x, n) for x in self.x1])
    def __floor__(self):
        import math
        return Mast(*[math.floor(x) for x in self.x1])
    def __ceil__(self):
        import math
        return Mast(*[math.ceil(x) for x in self.x1])
    def __trunc__(self):
        import math
        return Mast(*[math.trunc(x) for x in self.x1])
    def __index__(self):
        if len(self.x1) == 1:
            return int(self.x1[0])
        else:
            raise TypeError("Mast object cannot be interpreted as an integer")
    def __bytes__(self):
        return bytes(str(self.x1), 'utf-8')
    def __format__(self, format_spec):
        return format(str(self.x1), format_spec)
    def __sizeof__(self):
        return super().__sizeof__() + sum(x.__sizeof__() for x in self.x1)
    def __or__(self, value):
        if isinstance(value, Mast):
            return Mast(*[a | b for a, b in zip(self.x1, value.x1)])
        else:
            raise TypeError("Unsupported operand type(s) for |: 'Mast' and '{}'".format(type(value).__name__))
    def __and__(self, value):
        if isinstance(value, Mast):
            return Mast(*[a & b for a, b in zip(self.x1, value.x1)])
        else:
            raise TypeError("Unsupported operand type(s) for &: 'Mast' and '{}'".format(type(value).__name__))
    def __xor__(self, value):
        if isinstance(value, Mast):
            return Mast(*[a ^ b for a, b in zip(self.x1, value.x1)])
        else:
            raise TypeError("Unsupported operand type(s) for ^: 'Mast' and '{}'".format(type(value).__name__))
    def __lshift__(self, value):
        if isinstance(value, Mast):
            return Mast(*[a << b for a, b in zip(self.x1, value.x1)])
        else:
            raise TypeError("Unsupported operand type(s) for <<: 'Mast' and '{}'".format(type(value).__name__))
    def __rshift__(self, value):
        if isinstance(value, Mast):
            return Mast(*[a >> b for a, b in zip(self.x1, value.x1)])
        else:
            raise TypeError("Unsupported operand type(s) for >>: 'Mast' and '{}'".format(type(value).__name__))
    def __invert__(self):
        return Mast(*[~x for x in self.x1])
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
    def __await__(self):
        import asyncio
        return (yield from asyncio.sleep(0).__await__())
    def __aiter__(self):
        return iter(self.x1)
    def __anext__(self):
        if self.x1:
            return self.x1.pop(0)
        else:
            raise StopAsyncIteration
    def __aenter__(self):
        return self
    def __aexit__(self, exc_type, exc_val, exc_tb):
        pass
    def __set__(self, instance, value):
        self.x1 = value
    def __get__(self, instance, owner):
        return self.x1
    def __delete__(self, instance):
        del self.x1
    def __class__(self):
        return Mast
    def append(self, value):
        self.x1.append(value)
    def extend(self, iterable):
        self.x1.extend(iterable)
    def insert(self, index, value):
        self.x1.insert(index, value)
    def remove(self, value):
        self.x1.remove(value)
    def pop(self, index=-1):
        return self.x1.pop(index)
    def clear(self):
        self.x1.clear()
    def index(self, value, start=0, end=None):
        return self.x1.index(value, start, end)
    def count(self, value):
        return self.x1.count(value)
    def sort(self, *, key=None, reverse=False):
        self.x1.sort(key=key, reverse=reverse)
    def reverse(self):
        self.x1.reverse()
    def add(self,other):
        if isinstance(other, Mast):
            return Mast(*[a + b for a, b in zip(self.x1, other.x1)])
        else:
            raise TypeError("Unsupported operand type(s) for +: 'Mast' and '{}'".format(type(other).__name__))
    def bust(self):
        if len(self.x1) == 0:
            return Mast()
        for i in range(len(self.x1)):
            for j in range(i+1, len(self.x1)):
                if self.x1[i] > self.x1[j]:
                    self.x1[i], self.x1[j] = self.x1[j], self.x1[i]
        return self
    def __mast__(self, values):
        if isinstance(values, (list, tuple)):
            self.x1 = list(values)
        elif isinstance(values, dict):
            self.x1 = list(values.items())
        else:
            raise TypeError("Unsupported type for mast: '{}'".format(type(values).__name__))
        return self
    def __sub__(self, other):
        if isinstance(other, Mast):
            return Mast(*[a - b for a, b in zip(self.x1, other.x1)])
        else:
            raise TypeError("Unsupported operand type(s) for -: 'Mast' and '{}'".format(type(other).__name__))
    def __rsub__(self, other):
        if isinstance(other, int):
            return Mast(*[other - x for x in self.x1])
        elif isinstance(other, Mast):
            return Mast(*[a - b for a, b in zip(other.x1, self.x1)])
        else:
            raise TypeError("Unsupported operand type(s) for -: '{}' and 'Mast'".format(type(other).__name__))
    
    def __repr__(self):
        return str(self.x1)
    def __iadd__(self, other):
        if isinstance(other, Mast):
            self.x1 = [a + b for a, b in zip(self.x1, other.x1)]
            return self
        else:
            raise TypeError("Unsupported operand type(s) for +=: 'Mast' and '{}'".format(type(other).__name__))
    def __isub__(self, other):
        if isinstance(other, Mast):
            self.x1 = [a - b for a, b in zip(self.x1, other.x1)]
            return self
        else:
            raise TypeError("Unsupported operand type(s) for -=: 'Mast' and '{}'".format(type(other).__name__))
    def __imul__(self, other):
        if isinstance(other, int):
            self.x1 = [x * other for x in self.x1]
            return self
        elif isinstance(other, Mast):
            self.x1 = [a * b for a, b in zip(self.x1, other.x1)]
            return self
        else:
            raise TypeError("Unsupported operand type(s) for *=: 'Mast' and '{}'".format(type(other).__name__))
    def __itruediv__(self, other):
        if isinstance(other, int):
            self.x1 = [x / other for x in self.x1]
            return self
        elif isinstance(other, Mast):
            self.x1 = [a / b for a, b in zip(self.x1, other.x1)]
            return self
        else:
            raise TypeError("Unsupported operand type(s) for /=: 'Mast' and '{}'".format(type(other).__name__))
    def __imod__(self, other):
        if isinstance(other, int):
            self.x1 = [x % other for x in self.x1]
            return self
        elif isinstance(other, Mast):
            self.x1 = [a % b for a, b in zip(self.x1, other.x1)]
            return self
        else:
            raise TypeError("Unsupported operand type(s) for %=: 'Mast' and '{}'".format(type(other).__name__))
    def __ipow__(self, other):
        if isinstance(other, int):
            self.x1 = [x ** other for x in self.x1]
            return self
        elif isinstance(other, Mast):
            self.x1 = [a ** b for a, b in zip(self.x1, other.x1)]
            return self
        else:
            raise TypeError("Unsupported operand type(s) for **=: 'Mast' and '{}'".format(type(other).__name__))
    def __ifloordiv__(self, other):
        if isinstance(other, int):
            self.x1 = [x // other for x in self.x1]
            return self
        elif isinstance(other, Mast):
            self.x1 = [a // b for a, b in zip(self.x1, other.x1)]
            return self
        else:
            raise TypeError("Unsupported operand type(s) for //=: 'Mast' and '{}'".format(type(other).__name__))
    def __ior__(self, other):
        if isinstance(other, Mast):
            self.x1 = [a | b for a, b in zip(self.x1, other.x1)]
            return self
        else:
            raise TypeError("Unsupported operand type(s) for |=: 'Mast' and '{}'".format(type(other).__name__))
    def __iand__(self, other):
        if isinstance(other, Mast):
            self.x1 = [a & b for a, b in zip(self.x1, other.x1)]
            return self
        else:
            raise TypeError("Unsupported operand type(s) for &=: 'Mast' and '{}'".format(type(other).__name__))
    def __ixor__(self, other):
        if isinstance(other, Mast):
            self.x1 = [a ^ b for a, b in zip(self.x1, other.x1)]
            return self
        else:
            raise TypeError("Unsupported operand type(s) for ^=: 'Mast' and '{}'".format(type(other).__name__))
    def __ilshift__(self, other):
        if isinstance(other, Mast):
            self.x1 = [a << b for a, b in zip(self.x1, other.x1)]
            return self
        else:
            raise TypeError("Unsupported operand type(s) for <<=: 'Mast' and '{}'".format(type(other).__name__))
    def __irshift__(self, other):
        if isinstance(other, Mast):
            self.x1 = [a >> b for a, b in zip(self.x1, other.x1)]
            return self
        else:
            raise TypeError("Unsupported operand type(s) for >>=: 'Mast' and '{}'".format(type(other).__name__))
    def mast(self, values):
        return self.__mast__(values)
    def _flatten(self, item):
        result = []
        if isinstance(item, (list, tuple)):
            for sub in item:
                result.extend(self._flatten(sub))
        elif isinstance(item, Mast):
            result.extend(self._flatten(item.x1))
        elif isinstance(item, (int, float)):
            result.append(item)
        return result

    def max(self):
        if not self.x1:
            raise ValueError("max() arg is an empty sequence")
        all_numbers = self._flatten(self.x1)
        if not all_numbers:
            raise ValueError("no numeric values found")
        max_value = all_numbers[0]
        for x in all_numbers[1:]:
            if x > max_value:
                max_value = x
        return max_value

    def min(self):
        if not self.x1:
            raise ValueError("min() arg is an empty sequence")
        all_numbers = self._flatten(self.x1)
        if not all_numbers:
            raise ValueError("no numeric values found")
        min_value = all_numbers[0]
        for x in all_numbers[1:]:
            if x < min_value:
                min_value = x
        return min_value
def nest(*values):  
    result = []
    for x in values:  
        if isinstance(x, (list, tuple)):
            result.append(Mast(*x))  
        elif isinstance(x, dict):
            for k, v in x.items():
                result.append(Mast(k, v))
        else:
            result.append(x)
    return Mast(*result)  

def mast(values):
    return Mast().mast(values)