#Intermediate python stuff 2

import argparse as ap
import sys 

def calc(args):
    if args.operation == 'add':
        return args.x + args.y
    elif args.operation == 'sub':
        return args.x - args.y
    elif args.operation == 'mul':
        return args.x * args.y
    elif args.operation == 'div':
        return args.x / args.y


def main():
    parser = ap.ArgumentParser()
    parser.add_argument('--x', type=float, default=1.0, help="change the x argument in the program, default 1.0")
    parser.add_argument('--y', type=float, default=1.0, help="change the y argument in the program, default 1.0") 
    parser.add_argument('--operation', type=str, default="add", help="change the operation options: add, sub, mul, div")
    
    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))
    
if __name__ == "__main__":
    main()