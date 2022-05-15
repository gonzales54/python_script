# iterator
"""mytuple = ('apple', 'orange')
myit = iter(mytuple)

print(next(myit))
print(next(myit))"""


class Mynum:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


mynum = Mynum()
myiter = iter(mynum)

for i in myiter:
    print(i)
