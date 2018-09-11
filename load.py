import os
import argparse
import parse

EXT = ".TEP"


def find_all_files(directory):
    for root, dirs, files in os.walk(directory):
        yield root
        for file in files:
            yield os.path.join(root, file)


def get_args():
    # 準備
    parser = argparse.ArgumentParser()

    # 標準入力以外の場合
    parser.add_argument("i", help="input directory path", type=str)
    parser.add_argument("o", help="output directory path", type=str)

    # 結果を受ける
    args = parser.parse_args()

    return args


def main():
    args = get_args()
    print("input dir: %s" % args.i)
    print("output dir: %s" % args.o)

    for file in find_all_files(args.i):
        root, ext = os.path.splitext(file)
        if ext == EXT:
            print("processing: %s" % file)
            parse.parse(file, args.o)


if __name__ == '__main__':
    main()





