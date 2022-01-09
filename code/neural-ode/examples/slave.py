import argparse
import time

parser = argparse.ArgumentParser()
parser.add_argument('--a', type=eval, default=False)
parser.add_argument('--n', type=int, default=2)
parser.add_argument('--s', type=str, default='hi')
args = parser.parse_args()

if __name__ == '__main__':
    t1 = time.time()
    if args.a:
        for i in range(args.n):
            print(args.s)
    else:
        print('=)')
    t2 = time.time()

    