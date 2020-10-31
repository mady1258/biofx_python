#!/usr/bin/env python3
""" Tests for subs.py """

from subprocess import getstatusoutput
import os

PRG = './subs.py'
TEST1 = ('./tests/inputs/input1.txt', './tests/inputs/input1.txt.out')


# --------------------------------------------------
def test_exists() -> None:
    """ Program exists """

    assert os.path.isfile(PRG)


# --------------------------------------------------
def test_usage() -> None:
    """ Usage """

    for arg in ['-h', '--help']:
        rv, out = getstatusoutput(f'{PRG} {arg}')
        assert rv == 0
        assert out.lower().startswith('usage:')


# --------------------------------------------------
def run(inputs: str, expected: str) -> None:
    """ Runs on command-line input """

    rv, out = getstatusoutput(f'{PRG} {inputs}')
    assert rv == 0
    assert out == expected


# --------------------------------------------------
def cat(file: str) -> str:
    """ Return contents of file """

    return open(file).read().rstrip()


# --------------------------------------------------
def test_input1() -> None:
    """ Runs on command-line input """

    run('GATATATGCATATACTT ATAT', '2 4 10')


# --------------------------------------------------
def test_input2() -> None:
    """ Runs on file input """

    file, expected = TEST1
    run(cat(file), cat(expected))
