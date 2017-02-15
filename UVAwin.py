import datetime
import pytz #standardize timezone calculation across dates
import time
import json #MSNBC hosts data in json form
import os
import urllib2 #python library for opening URLs
import xml.etree.ElementTree as ET #python container object for dealing data structures such as XML in this case
# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import sendgrid
from sendgrid.helpers.mail import *



url = 'http://scores.nbcsports.msnbc.com/ticker/data/gamesMSNBC.js.asp?jsonp=true&sport=CBK&period=%d' #always using college basketball scores so sport = CBK, date is what varies

Scores = [] #array for score data 
OtherTeam = '' #global variable for UVA opponent
OtherTeamScore = '' #global variable for UVA opponent
UVAScore = '' #global variable for UVA opponent

def getScore():
    formatteddate = 20170212 #confirmed date UVA plays- test to find UVA's nickname, confirmed that it is the Cavaliers in MSNBC Json
    #formatteddate = int(datetime.datetime.now(pytz.timezone('US/Eastern')).strftime("%Y%m%d")) #get current date
    allgames= [] #load in all data to parse which ones are UVA scores, not necessary for conditional
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

            #Save UVA Home Scores and Opponent Name
            if home_team == 'Cavaliers':
                '''UVAscore.append({
                'Home': home_team,
                'UVA Score': home_score,
                'Away': away_team,
                'Away Score': away_score,
                })'''
                UVAScore = home_score
                OtherTeam = away_team
                OtherTeamScore = away_score
            #Save UVA Away Scores and Opponent Name/Info
            if away_team == 'Cavaliers':
                '''UVAscore.append({
                'Home': home_team,
                'Home Score': home_score,
                'Away': away_team,
                'UVA Score': away_score,
                })'''
                UVAScore = away_score
                OtherTeam = home_team
                OtherTeamScore = home_score
            #print UVAhomescore
        print OtherTeam
    except Exception as e:
        print e



############################SendGrid Code for creating and sending actual content##########

    #html to generate email and include scores
    htmlForEmail = htmlForEmail = '<html><head><title></title></head><body><div><span style="font-size:72px;"><strong>GO HOOS -The HOOS have destroyed the &nbsp;'+ OtherTeam + ' by a score of ' + UVAScore + ' to ' + OtherTeamScore +  '</strong></span></div><img src = "https://usatthebiglead.files.wordpress.com/2016/03/uva-stinky-fingers-against-cuse.gif?w=1000"></body></html>'



        #old gif, seems like it was far too large to be embedded in an email
    #<div><span class="sg-image" data-imagelibrary="%7B%22width%22%3A720%2C%22height%22%3A404%2C%22alignment%22%3A%22%22%2C%22border%22%3A0%2C%22src%22%3A%22https%3A//media.giphy.com/media/yUZootkvc3Toc/giphy.gif%22%2C%22classes%22%3A%7B%22sg-image%22%3A1%7D%7D"><img height="404" src="https://media.giphy.com/media/yUZootkvc3Toc/giphy.gif" style="width: 720px; height: 404px;" width="720" /></span></div>
    #</body>
    #</html>'



    sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
    from_email = Email("CoachK@duke.edu")
    to_email = Email("harounahmed2@gmail.com")
    subject = "Grayson Allen Sucks- Go Hoos"
    content = Content("text/html", htmlForEmail)
    mail = Mail(from_email, subject, to_email,content) #SendGrid Mail helper class assists with sending

            ############SendGrid Template code as HTML helper, not necessary
    #mail.personalizations[0].add_substitution(Substitution("-OtherTeam-", OtherTeam)) #replace html hook with actual team name
    #mail.set_template_id("9c910dcd-6252-402c-8da8-096bb372d576")  #retrieve manufactured template ID from Sendgrid Account


    response = sg.client.mail.send.post(request_body=mail.get())

getScore()
