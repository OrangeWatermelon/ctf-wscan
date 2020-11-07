import argparse
from lib.init import Init


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('url', help="Target utl", type=str)
    args = parser.parse_args()
    scan = Init(args.url)
    scan.start()


if __name__ == '__main__':
    main()