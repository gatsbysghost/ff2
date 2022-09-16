import re

FFRPACKAGES = []

with open('../lib/Fantasy-Football-Models/Fantasy Football Analysis v2.Rmd') as f:
    text = f.read()
    packages = re.findall(r'library\((\w+)\)', text)
    for pkg in packages:
        FFRPACKAGES.append(pkg)

