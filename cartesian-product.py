#!/usr/bin/python3

from argparse import ArgumentParser
from itertools import product

def createArgumentParser():

    parser = ArgumentParser()
    parser.add_argument("list",
                        type=list,
                        nargs="+",
                        help="List(s) to compute the cartesian product of")
    parser.add_argument("-u",
                        "--unique",
                        action="store_true",
                        help="Deduplicate lists so that they become sets of unique elements")
    parser.add_argument("-U",
                        "--Universally_unique",
                        action="store_true",
                        help="Deduplicate the resulting cartesian product so it becomes a set of unique elements that have no repeated values")
    return parser.parse_args()


def cartesianProduct(unique, Universally_unique, arglist):
    "Returns the cartesian product of provided lists"
    
    cartesianProduct = product([])

    if unique:
        for i in range(len(arglist)):
            arglist[i] = sorted(set(arglist[i]))
        cartesianProduct = product(*arglist)
    else:
        cartesianProduct = product(*arglist)
    if Universally_unique:
        cartesianProduct = sorted(set(cartesianProduct))
        for element in cartesianProduct:
            for i in element:
                if element.count(i) > 1:
                    try:
                        cartesianProduct.remove(element)
                    except ValueError:
                        pass
    return cartesianProduct


def main():

    args = createArgumentParser()
    for element in cartesianProduct(args.unique,
                                    args.Universally_unique,
                                    args.list):
        print(element)


main()
