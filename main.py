from parsing.parser import Parser


def main():
    page = 1
    while True:
        print(f'Parsing page {page} ...')
        url = f'https://www.kijiji.ca/b-apartments-condos/city-of-toronto/page-{page}/c37l1700273'
        parser = Parser(url)
        parser.get_data()
        print(f'{page} page spars ...')
        if not parser.find_button_next():
            break
        page += 1


if __name__ == '__main__':
    main()