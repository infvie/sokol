import requests
import pandas as pd
import xml.etree.ElementTree as ET
import sqlite3 as sql
from bs4 import BeautifulSoup  
import re

def games(year,month,day):
    '''This is a function that will return the all the pitches for all the games played on a single day.'''
    
    url = f'http://gd2.mlb.com/components/game/mlb/year_{year}/month_{month}/day_{day}'
    html = requests.get(url)
    soup = BeautifulSoup(html.text,'lxml-xml')
    games = re.findall('(gid\S*)/ ',soup.text)
    
    if games == []:
        return 'There were no games on this day.'
    
    for game in games:
        
        # build containers for holding data
        atbat_df = pd.DataFrame()
        pitches_df = pd.DataFrame()
        
        game_url = f'{url}/{game}/inning/inning_all.xml'
        xml = requests.get(game_url)
        root = ET.fromstring(xml.text)
        innings = root.findall('inning')
        
        # need to recurse through to keep pitches attached to players
        n = 1
        for inning in innings:
            for half in ['top','bottom']:
                try:
                    inning.find(half).findall('atbat')
                except:
                    continue
                for atbat in inning.find(half).findall('atbat'):
                    data = pd.DataFrame(atbat.attrib,index=[0])
                    data['inning'] = n
                    # we need a link between the at bat and the pitches thrown to them
                    # error handling for walks
                    try:
                        linker = data['play_guid']
                    except:
                        continue
                    atbat_df = pd.concat([atbat_df,data],ignore_index=True,sort=False)
                    pitch = [pitch.attrib for pitch in atbat.findall('pitch')]
                    pitch = pd.DataFrame(pitch)
                    pitch['play_guid'] = linker    
                    pitches_df = pd.concat([pitches_df,pitch],sort=False)
            n += 1
        atbat_df.to_csv('atbat.csv',mode='a')
        pitches_df.to_csv('pitches.csv',mode='a')

