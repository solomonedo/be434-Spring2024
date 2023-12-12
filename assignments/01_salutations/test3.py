""" Tests for howdy.py """

import os
from subprocess import getstatusoutput

PRG = './salutations.py'

# --------------------------------------------------
def test_name():
    """ Accepts name """

    for opt in ['-n', '--name']:
        rv, out = getstatusoutput(f'{PRG} {opt} Jorge')
        assert rv == 0
        assert out.strip() == 'Howdy, Jorge.'

