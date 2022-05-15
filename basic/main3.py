class Myclass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def pri(self):
        print(self.name + str(self.age))


p1 = Myclass('John', 36)
p1.pri()


