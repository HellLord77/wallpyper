import libraries.color as color
import utils


def main():
    color.cprint(f'{color.BackColor.WHITE}Hello{color.FontStyle.RESET}{color.ForeColor.GREEN}69')
    return

    url_ = "https://www.cloudflare.com/rate-limit-test/"
    url = "https://wallhaven.cc/api/v1/search"
    for _ in range(50):
        response = utils.open_url(url, {'q': 'sexy'})
        print(response.status, response.reason)
        if response.status == 429:
            print(response.response.headers['Retry-After'])


if __name__ == "__main__":
    main()
