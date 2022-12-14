#  write your code here
import argparse

def decode_Caesar_cipher(s, n):
    alpha = " ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',.?!"
    s = s.strip()
    text = ''
    for c in s:
        text += alpha[(alpha.index(c) - n) % len(alpha)]
    print(text)

parser = argparse.ArgumentParser()
parser.add_argument("--file")
parser.add_argument("--number")

args = parser.parse_args()
filename = args.file
opened_file = open(filename)
encoded_text = opened_file.read()  # read the file into a string
opened_file.close()  # always close the files you've opened
n = int(args.number)

decode_Caesar_cipher(encoded_text, n)
