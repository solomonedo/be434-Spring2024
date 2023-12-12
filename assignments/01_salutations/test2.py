""" Tests for howdy.py """

import os
from subprocess import getstatusoutput

PRG = './salutations.py'

# --------------------------------------------------
def test_greeting():
    """ Accepts greeting """

    for opt in ['-g', '--greeting']:
        rv, out = getstatusoutput(f'{PRG} {opt} Hola')
        assert rv == 0
        assert out.strip() == 'Hola, Stranger.'


