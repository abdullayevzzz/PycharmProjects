# write your code here
import math
import argparse
import sys
error_msg = "Incorrect parameters"

parser = argparse.ArgumentParser()
parser.add_argument("--type")
parser.add_argument("--principal")
parser.add_argument("--payment")
parser.add_argument("--periods")
parser.add_argument("--interest")

args = parser.parse_args()

if len(vars(args)) < 5:
    print(error_msg)
    quit()

if args.principal:
    P = int(args.principal)
    if P < 0:
        print(error_msg)
        quit()
if args.payment:
    A = int(args.payment)
    if A < 0:
        print(error_msg)
        quit()
if args.periods:
    n = int(args.periods)
    if n < 0:
        print(error_msg)
        quit()
if args.interest:
    i = float(args.interest) / 1200
    if i < 0:
        print(error_msg)
        quit()
else:
    print(error_msg)
    quit()

if not args.type:
    print(error_msg)
    quit()

if args.type == "annuity":
    if not args.principal:
        P = A / (i * math.pow(1 + i, n) / (math.pow(1 + i, n) - 1))
        print(f"Your loan principal = {P}!")
        print(f"Overpayment = {A * n - P}")

    elif not args.payment:
        A = P * (i * math.pow(1 + i, n) / (math.pow(1 + i, n) - 1))
        A = math.ceil(A)
        print(f"Your monthly payment = {A}!")
        print(f"Overpayment = {A * n - P}")

    elif not args.periods:
        n = math.ceil(math.log(A / (A - i * P), 1 + i))
        years = n // 12
        months = n % 12
        str = "It will take"
        if years:
            str = str + f" {years}" + " years" if years > 1 else " year"
            if months:
                str = str + " and"
        if months:
            str = str + f" {months}" + " months" if months > 1 else " month"
        print(str + " to repay this loan!")
        print(f"Overpayment = {A * n - P}")

elif args.type == "diff":
    if args.payment:
        print(error_msg)
        quit()

    sum = 0
    for m in range(1, n+1):
        D = P / n + i * (P - P * (m - 1) / n)
        D = math.ceil(D)
        print(f"Month {m}: payment is {D}")
        sum += D
    print(f"\nOverpayment = {sum - P}")

else:
    print(error_msg)
    quit()
