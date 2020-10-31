""" Tests for cgc.py """

import os
import random
import string
import re
from subprocess import getstatusoutput

PRG = './cgc.py'
SAMPLE1 = './tests/inputs/1.fa'
SAMPLE2 = './tests/inputs/2.fa'


# --------------------------------------------------
def test_exists() -> None:
    """ Program exists """

    assert os.path.isfile(PRG)


# --------------------------------------------------
def test_usage() -> None:
    """ Usage """

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput('{} {}'.format(PRG, flag))
        assert rv == 0
        assert out.lower().startswith('usage:')


# --------------------------------------------------
def test_bad_input() -> None:
    """ Fails on bad input """

    bad = random_string()
    rv, out = getstatusoutput(f'{PRG} {bad}')
    assert rv != 0
    assert out.lower().startswith('usage:')
    assert re.search(f"No such file or directory: '{bad}'", out)


# --------------------------------------------------
def test_good_input1() -> None:
    """ Works on good input """

    rv, out = getstatusoutput(f'{PRG} {SAMPLE1}')
    assert rv == 0
    assert out == 'Rosalind_0808 60.919540'


# --------------------------------------------------
def test_good_input2() -> None:
    """ Works on good input """

    rv, out = getstatusoutput(f'{PRG} {SAMPLE2}')
    assert rv == 0
    assert out == 'Rosalind_5723 52.806415'


# --------------------------------------------------
def random_string() -> str:
    """ Generate a random string """

    k = random.randint(5, 10)
    return ''.join(random.choices(string.ascii_letters + string.digits, k=k))
