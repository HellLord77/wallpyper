import libs.debug


def func(self):
    return self


def func2():
    pass


class B(object):
    pass


class A(B):
    def __init__(self):
        self.var = 69

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)


def main():
    libs.debug.init('libs', 'modules', 'platforms')
    a = A()
    func(a.var)
    func2()


if __name__ == '__main__':
    main()
