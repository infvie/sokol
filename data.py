import requests
import pandas as pd
import xml.etree.ElementTree as ET
import sqlite3 as sql

def main():
    # navigate to all pages in the season
    f = open('inning_all.xml')

    # parse the xml files
    tree = ET.parse(f)

    # create collector object 
    atbat = pd.DataFrame
    play = pd.DataFrame

    # go through atbat and create a unique key  
    # for atbat_obj in tree.

    # pd.DataFrame.from_dict(t,orient='columns')
    # pd.DataFrame.from_dict(t,orient='columns')

if __name__ == '__main__':
    main()
