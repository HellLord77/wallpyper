import libs.debug
import libs.gui


def func(*arg):
    print(arg)


def main():
    libs.debug.init('libs', 'modules', 'platforms')
    libs.gui.add_item('test item', func)
    libs.gui.main_loop()


if __name__ == '__main__':
    main()
