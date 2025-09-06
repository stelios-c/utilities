#!/usr/bin/python3

import argparse

parser = argparse.ArgumentParser(
        prog ='ProgramName',
        description='A script that reads a dataset from a file and outputs a stem and leaf display',
        epilog='submission to "For the Love of Code 2025"')

parser.add_argument('filename')
