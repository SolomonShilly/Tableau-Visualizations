import shutil
import pandas as pd
import gzip

# rb = read binary and wb = wrtie binary
with gzip.open('usa_00007.dta.gz', "rb") as inputFile:
    with open('usa_00007.dta', "wb") as outputFile:
        shutil.copyfileobj(inputFile, outputFile)

file = pd.read_stata('usa_00007.dta')
file.to_csv('StateData.csv')