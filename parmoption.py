#!/usr/bin/python3.6

import sys, getopt
from math import sqrt
from argparse import ArgumentParser
from datetime import datetime

def output_to(path, content):
    if path:
        with open(path, "a+") as f:
            f.write(content)
    else:
        print(content)

parser = ArgumentParser(description='Racine Carré.')
parser.add_argument('-i', '--myint', required=True, type=int, nargs=1, help='integer')
parser.add_argument('-o', '--output', help='output')
parser.add_argument('-d', '--date', help='date')

args = parser.parse_args()

try:
    racine = sqrt(args.myint[0])
    now_date = str(datetime.now())
    result_str = "{date} ! {result}".format(date=now_date, result=racine)
    output_to(args.output, result_str)
except ValueError:
    print("Integer must be positive")
    sys.exit(-1)

# def madate():
#     today = date.today()
#     print(today)


print(args)

''' Exemple
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

args = parser.parse_args()
print(args.accumulate(args.integers))
'''

# def main(argv):
#     input = ""
#     output = ""
#     for opt, arg in opts:
#         if opt == '-h':
#             print('paramoption.py -i <inputfile> -o <outputfile>')
#             sys.exit()
#         elif opt in ("-i", "--integer"):
#             input = arg
#         elif opt in ("-o", "--output"):
#             output = arg
# print('Input file is "', input)
# print('Output file is "', output)