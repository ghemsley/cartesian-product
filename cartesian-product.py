#!/usr/bin/python3

from argparse import ArgumentParser
from itertools import product

def createArgumentParser():

    parser = ArgumentParser()
    parser.add_argument("list", type=list, nargs="+", help="List(s) to compute the cartesian product of")
    parser.add_argument("-u", "--unique", action="store_true", help="Deduplicate lists so that they become sets of unique elements")
    return parser.parse_args()


def cartesianProduct(unique, arglist):

    cartesianProduct = product([])

    if unique:
        for i in range(len(arglist)):
            arglist[i] = sorted(set(arglist[i]))
        cartesianProduct = product(*arglist)
    else:
        cartesianProduct = product(*arglist)
    return cartesianProduct


def main():

    args = createArgumentParser()
    for element in cartesianProduct(args.unique, args.list):
        print(element)


main()
