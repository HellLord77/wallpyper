import utils


@utils.cache
def example_func(dct):
    print(56)
    return len(dct)


def main():
    print(example_func({}))
    print(example_func({}))
    print(example_func({'a': '3'}))
    print(example_func({'a': '3'}))


if __name__ == "__main__":
    main()
