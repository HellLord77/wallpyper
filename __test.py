import time

import libs.thread


def func():
    time.sleep(1)
    print(69)


def main():
    timer = libs.thread.Timer(2, func)
    timer.start()
    for i in range(20):
        print(timer.__dict__)
        time.sleep(1)
    timer.stop()
    # timer.set_interval(5)
    for i in range(25):
        print(timer.__dict__)
        time.sleep(1)
    timer.stop()


if __name__ == '__main__':
    s = 'd'
    main()
