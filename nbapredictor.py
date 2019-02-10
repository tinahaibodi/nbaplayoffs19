import csv
import sys
import pandas as pd
import numpy as np

# The magic number is calculated as G + 1 − WA − LB, where
# G is the total number of games in the season
# WA is the number of wins that Team A has in the season
# LB is the number of losses that Team B has in the season
# From Wikipedia and Gitlab

MagicNumberDictionary = {
    'Atlanta Hawks': 83,
    'Boston Celtics': 83,
    'Brooklyn Nets': 83,
    'Charlotte Hornets': 83,
    'Chicago Bulls': 83,
    'Cleveland Cavaliers': 83,
    'Dallas Mavericks': 83,
    'Denver Nuggets': 83,
    'Detroit Pistons': 83,
    'Golden State Warriors': 83,
    'Houston Rockets': 83,
    'Indiana Pacers': 83,
    'LA Clippers': 83,
    'Los Angeles Lakers': 83,
    'Memphis Grizzlies': 83,
    'Miami Heat': 83,
    'Milwaukee Bucks': 83,
    'Minnesota Timberwolves': 83,
    'New Orleans Pelicans': 83,
    'New York Knicks': 83,
    'Oklahoma City Thunder': 83,
    'Orlando Magic': 83,
    'Philadelphia 76ers': 83,
    'Phoenix Suns': 83,
    'Portland Trail Blazers': 83,
    'Sacramento Kings': 83,
    'San Antonio Spurs': 83,
    'Toronto Raptors': 83,
    'Utah Jazz': 83
}

def predictScores(filename):


    seasonScoresFile = open(filename, 'r')
    scores = csv.reader(seasonScoresFile)
    data = list(scores)
    for row in data:
        print(row)

    initialize()


def initialize():

    df = pd.read_csv('playoffs19.py')
    df['Wins'] = pd.Series(0, index=list(range(30)))
    df['Losses'] = pd.Series(0, index=list(range(30)))
    df['Magic Number'] = pd.Series(83, index=list(range(30)))
    #df['Seed'] = pd.Series(0)

    df.loc[df.Conference_id=='East', 'Seed'] = range(1,16)
    df.loc[df.Conference_id=='West', 'Seed'] = range(1,16)
    df['Seed'] = df['Seed'].astype(int)

    #print(df)





if __name__ == '__main__':
predictScores(*sys.argv[1:])
