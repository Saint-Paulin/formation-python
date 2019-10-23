

import sys, getopt
import requests
from math import sqrt
from argparse import ArgumentParser
from datetime import datetime

def check_rest_method(method):
    return method.upper() in ["GET", "POST", "PUT", "DELETE"]

def check_if_file_exists(output):
    return os.path.isfile(fname)

def send_request(args):
    method = args.method[0]
    url = args.url[0]
    port = args.port[0]
    try:
        output = args.output[0]
    except IndexError:
        if method.uppper == "GET":
            pass
        else:
            raise FileNotFoundError("Please provide a file")

def determine_method(method):
    if method == "POST":
        return requests.post
    elif method == "GET":
        return requests.get
    elif method == "PUT":
        return requests.put
    elif method == "DELETE":
        return requests.delete
    else:
        raise NotImplementedError("Metho not found")

def output_to(path, content):
    if path:
        with open(path, "w+") as f:
            f.write(content)
    else:
        print(content)

parser = ArgumentParser(description='API HTTP')
parser.add_argument('-u', '--url', required=True, type=str, nargs=1, help='url')
parser.add_argument('-p', '--port', help='port', default=80, type=int, nargs=1)
parser.add_argument('-o', '--output', help='output', type=str, nargs=1)
parser.add_argument('-m', '--method', help='method', type=str, nargs=1)
parser.add_argument('-f', '--file', help='file', type=str, nargs=1, required=True)

args = parser.parse_args()
send_request(args)

print(args)

if args.method[0] == "GET":
    r = requests.get(args.url[0])
    s = r.text
    output_to(args.output[0], str(s))
elif args.method[0] == "POST":
    r = requests.post(args.url[0])
    s = r.text
    output_to(args.output[0], str(s))
elif args.method[0] == "PUT":
    r = requests.put(args.url[0])
    s = r.text
    output_to(args.output[0], str(s))
elif args.method[0] == "DELETE":
    r = requests.delete(args.url[0])
    s = r.text
    output_to(args.output[0], str(s))

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