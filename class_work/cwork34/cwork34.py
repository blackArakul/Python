from parsers import Parser


def main():
    pars = Parser("https://www.ixbt.com/live/index/news/", "news.txt")
    pars.run()


if __name__ == '__main__':
    main()