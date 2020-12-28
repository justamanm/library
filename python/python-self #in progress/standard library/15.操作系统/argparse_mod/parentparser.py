import argparse
from argparse import _SubParsersAction
from typing import List


def run():
    print(123)


def add_subparser(
    subparsers: _SubParsersAction, parents: List[argparse.ArgumentParser]
) :
    sub_par = subparsers.add_parser("sub", parents=parents)
    sub_par.add_argument("--prompt")
    # sub_par.set_defaults(func=run)
