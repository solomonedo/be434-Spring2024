#!/usr/bin/env python3
"""
Author : Your name
Date   : 2023-02-17 (today's date)
Purpose: Say Hello
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Say Hello',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    # Add greeting, name, and excited options

    parser.add_argument('-a',
                        '--arg',
                        help='A named string argument',
                        metavar='str',
                        type=str,
                        default='')

    parser.add_argument('-a',
                        '--arg',
                        help='A named string argument',
                        metavar='str',
                        type=str,
                        default='')

    parser.add_argument('-o',
                        '--on',
                        help='A boolean flag',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Start here"""

    args = get_args()

    # create variables for inputs (I am showing the greeting argument below only)
    excited = args.excited

    # use an if/else statement to see if the user included the --excited flag
    # if so, print the greeting with an ending !
    # if not, print the greeting with an ending .


# --------------------------------------------------
if __name__ == '__main__':
    main()


