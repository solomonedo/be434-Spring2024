""" Tests for howdy.py """

import os
from subprocess import getstatusoutput

PRG = './salutations.py'

# --------------------------------------------------
def test_all_options():
    """ Handles all options """

    rv, out = getstatusoutput(f'{PRG} -e -g Greetings -n Sarah')
    assert rv == 0
    assert out.strip() == 'Greetings, Sarah!'
