from algo_greedy import algo_greedy
from algo_random import algo_random
from algo_bruteforce import algo_brute_force
from utils import item_list
from argparse_setup import args


def main():
    """
    Run an algorithm based on the arguments
    passed in the command line
    """
    items = item_list(f"{args['file']}.csv")
    if args['algo'] == 'random':
        algo_random(items, args['loop'], args['budget'])
    elif args['algo'] == 'brute':
        algo_brute_force(items, args['budget'])
    elif args['algo'] == 'greedy':
        algo_greedy(items, args['budget'])
main()
