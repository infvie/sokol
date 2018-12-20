import requests
import pandas as pd

def main():
    text = requests.get('http://gd2.mlb.com/components/game/mlb/year_2018/month_06/day_08/gid_2018_06_08_anamlb_minmlb_1/inning/inning_2.xml')
    print(text)

if __name__ == '__main__':
    main()
