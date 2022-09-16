import rpy2
from rpy2.robjects.packages import importr
import rpy2.robjects.packages as rpackages
from rpy2.robjects.vectors import StrVector

from rmdawn import rmdtor

from assets import FFRPACKAGES

import prompt_toolkit
import tqdm

import sys, os

def install_r_deps():
    print("Installing packages...")
    base = importr('base')
    utils = importr('utils')
    utils.chooseCRANmirror(ind=1)

    packages_to_install = [x for x in FFRPACKAGES if not rpackages.isinstalled(x)]
    if len(packages_to_install) > 0:
        utils.install_packages(StrVector(packages_to_install))
    print("...done!")

def convert_markdown_to_r():
    print("Converting RMD (R-Markdown, an R Studio file format) to a regular R file...")
    rmdtor('../lib/Fantasy-Football-Models/Fantasy Football Analysis v2.Rmd')

def main():
    install_r_deps()
    convert_markdown_to_r()


if __name__ == '__main__':
    main()
