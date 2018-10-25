import os
import argparse
import parse
import json

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
    parser.add_argument("s", help="summary file path", type=str)

    # 結果を受ける
    args = parser.parse_args()

    return args


def main():
    args = get_args()
    print("input dir: %s" % args.i)
    print("output dir: %s" % args.o)

    # create summary file
    with open(args.s, 'w') as f:
        summary = []
        for file in find_all_files(args.i):
            root, ext = os.path.splitext(file)
            if ext == EXT:
                tep_dict = {}
                print("processing: %s" % file)
                image_file_name, txt_files_name = parse.parse(file, args.o)

                # tep dict
                tep_dict["image_file"] = image_file_name
                tep_dict["txt_files"] = txt_files_name
                tep_dict["original_file"] = file
                summary.append(tep_dict)
        summary_dict = {"summary": summary}
        json.dump(summary_dict, f)


if __name__ == '__main__':
    main()




