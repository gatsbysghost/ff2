import rpy2
from rpy2.robjects.packages import importr
import rpy2.robjects.packages as rpackages
from rpy2.robjects.vectors import StrVector

import prompt_toolkit
import tqdm

import sys, os

def install_r_deps():
    base = importr('base')
    utils = importr('utils')
    utils.chooseCRANmirror(ind=1)

    packages_to_install = [x for x in FFRPACKAGES if not rpackages.isinstalled(x)]
    if len(names_to_install) > 0:
        utils.install_packages(StrVector(packages_to_install))

def main():
    pass

if '__name__' == 'main':
    main()
