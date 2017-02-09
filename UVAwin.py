import datetime
import pytz #standardize timezone calculation across dates
import time
import json #MSNBC hosts data in json form
import os
import urllib2 #python library for opening URLs
import xml.etree.ElementTree as ET #python container object for dealing data structures such as XML in this case


url = 'http://scores.nbcsports.msnbc.com/ticker/data/gamesMSNBC.js.asp?jsonp=true&sport=CBK&period=%d' #always using college basketball scores so sport = CBK, date is what varies

def getScore():
    #formatteddate = 20170206 #confirmed date UVA plays- test to find UVA's nickname, confirmed that it is the Cavaliers in MSNBC Json
    formatteddate = int(datetime.datetime.now(pytz.timezone('US/Eastern')).strftime("%Y%m%d")) #get current date
    allgames= [] #load in all data to parse which ones are UVA scores, not necessary for conditional
    UVAhomescore = [] #array for UVA specific data conditional at home
    UVAawayscore = [] #array for UVA specific data conditional away


    try:
        alldatafile = urllib2.urlopen(url % formatteddate) #open MSNBC scoreboard for specific date
        jsonall = alldatafile.read() #read data from site and save it to variable
        alldatafile.close
        read_string = jsonall.replace('shsMSNBCTicker.loadGamesData(', '').replace(');', '')
        json_parsed = json.loads(read_string)

        for game in json_parsed.get('games', []): #for loop to create Gametrees using ElementTree
            bigtree = ET.XML(game)

            #save home information
            home_tree = bigtree.find('home-team')
            home_team = home_tree.get('nickname')
            home_score = home_tree.get('score')
            #print 'home team is: ' + home_team + ' with a score of: ' + home_score

            #save away information
            away_tree = bigtree.find('visiting-team') #for some reason MSNBC uses visiting-team instead of home in their data...
            away_team = away_tree.get('nickname')
            away_score = away_tree.get('score')

            #Save UVA Home Scores
            if home_team == 'Cavaliers':
                UVAhomescore.append({
                'Home': home_team,
                'UVA Score': home_score,
                'Away': away_team,
                'Away Score': away_score,
                })

            #Save UVA Away Scores
            if away_team == 'Cavaliers':
                UVAawayscore.append({
                'Home': home_team,
                'Home Score': home_score,
                'Away': away_team,
                'UVA Score': away_score,
                })
            print UVAhomescore

    except Exception as e:
        print e


getScore()
