def main():
    d1 = {'k1': 'v1', 'k2': 'v2'}
    d2 = {'k2': 'v3', 'k3': 'v4'}
    d1.update(d2)
    print(d1)

    import main
    from modules import wallhaven
    main.load_config()
    print(wallhaven.CONFIG)
    main.save_config()

    main.load_config()
    print(wallhaven.CONFIG)


if __name__ == '__main__':
    main()
