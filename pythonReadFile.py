import argparse
import sys
parser = argparse.ArgumentParser(description='Read a file in reverse')
parser.add_argument('filename', help='the file to read')
parser.add_argument('--limit', '-l', type=int, help='the number of lines to read')
parser.add_argument('--version', '-v', action='version', version='%(prog)s 1.0')

args = parser.parse_args()

try:
    f = open(args.filename)
    limit = args.limit
except FileNotFoundError as err:
    print(f"Error: {err}")
    sys.exit(1)
else:

    with f:
        #read the lines in the text
        lines = f.readlines()
        #will reverse the words in the sentence 
        lines.reverse()

        #check to see if there is a limit argument
        if args.limit:
            lines = lines[:limit]

        #reverse the word strings itself 
        #removes in white spaces
        for line in lines:
            print(line.strip()[::-1])
