import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--algo', type=str, required=True)
parser.add_argument('--loop', type=int, required=False)
parser.add_argument('--file', type=str, required=False)
parser.add_argument('--budget', type=float, required=False, default=500)

args = vars(parser.parse_args())