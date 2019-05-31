import os
import argparse
import parse
import json
import glob

# 3rd party
from logzero import logger

EXT = ".TEP"


def find_all_files(directory):
    for root, dirs, files in os.walk(directory):
        yield root
        tep_counter = len(glob.glob1(root,"*.TEP"))
        if tep_counter > 1:
            for file in files:
                if file.endswith("2.TEP"):
                    yield os.path.join(root, file)
        else:
            for file in files:
                if file.endswith(".TEP"):
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
    logger.info("input dir: %s" % args.i)
    logger.info("output dir: %s" % args.o)

    # create summary file
    with open(args.s, 'w') as f:
        summary = []
        all_files = find_all_files(args.i)

        for i, file in enumerate(all_files):
            root, ext = os.path.splitext(file)
            if ext == EXT:
                tep_dict = {}
                logger.info("NO.%d processing: %s" % (i, file))

                try:
                    image_file_name, txt_files_name = parse.parse(file, args.o)
                except Exception as e:
                    logger.error(e)
                    continue

                # tep dict
                tep_dict["image_file"] = image_file_name
                tep_dict["txt_files"] = txt_files_name
                tep_dict["original_file"] = file
                summary.append(tep_dict)
            else:
                logger.info("no TEP file: %s" % file)
        summary_dict = {"summary": summary}
        json.dump(summary_dict, f)


if __name__ == '__main__':
    main()


