from argparse import ArgumentParser


def read_file(filename):
    with open(filename, "r+") as f:
        print(f.readlines())


parser = ArgumentParser(prog="Pancakes!", description="A simple tool for stacking PR's")

parser.add_argument("file")

args = parser.parse_args()

if args.file:
    read_file(args.file)
else:
    raise Exception("No file provided")
