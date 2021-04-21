import os

import request


def cb(*args):
    print(*args)


def main():
    url = 'https://w.wallhaven.cc/full/y8/wallhaven-y8xeg7.jpg'
    request.urlretrieve(url, 'E:\\Projects\\wxWallhaven\\img.jpg', 1024, callback=cb)
    return

    url = os.path.join('https://wallhaven.cc/api/v1/', 'settings')
    params = {'apikey': '38QakOzgfHqIohe1JO0f3aoQIbm1pKYx'}  # [-1] = K
    response = request.urlopen(url, params, True)
    print(response.status, response.response.getheader('Content-Length'))
    for i in response:
        print(i)
    exit()
    url = 'http://ipv4.download.thinkbroadband.com/1GB.zip'
    # response = requests.urlopen(url, stream=True)
    response = request.urlopen(url, stream=True)
    print(response.status)
    exit()
    while True:
        print(69)


if __name__ == '__main__':
    main()
