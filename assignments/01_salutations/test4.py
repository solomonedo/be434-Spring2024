""" Tests for howdy.py """

import os
from subprocess import getstatusoutput

PRG = './salutations.py'

# --------------------------------------------------
def test_excited():
    """ Prints bang """

    for flag in ['-e', '--excited']:
        rv, out = getstatusoutput(f'{PRG} {flag}')
        assert rv == 0
        assert out.strip() == 'Howdy, Stranger!'

