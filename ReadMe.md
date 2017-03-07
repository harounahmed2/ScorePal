This project was inspired by my friend Big Nick, who is a Duke fan because he sucks (and maybe partly because he went there.)  

Big Nick loves to show me the website diddukewin.com, everytime duke basketball wins. I went to Virginia, so this is absurdly irritating.  I wanted to pay him back for this, but unfortunately the domain name diduvawin.com was taken, so I had to get creative.

As such, I decided to create a script that sent him an email when UVA basketball won with the score.... repeatedly.  I took live site scores from MSNBC sports, which houses them in JSON format.  Thanks Chris Riccomoni (@criccomini)!

I then took the SendGrid Messenger API (V3) which is a RESTful API used for sending emails.  With this, I was able to customize and automate the sending of the scores to a set list of recipients, whether that be to torment my friend Big Nick, or more usefully a preset list of users that wanted a reminder everytime their team was playing.

To begin with, I decided that I wanted to send Big Nick an email on behalf of every point that UVA scores (luckily for him we are a defensive minded team.)  When this happens, most email clients save the large batch of emails under one line item from the same sender, which doesn't really get the torment across as much as I would like.  As such I iterated the code so that he would get a separate email from every single point as a sender, so his email would get absolutely flooded.  Once I was sure this was working, I came up with a similar email template to send everytime that Duke lost, on behalf of every point that their opponent scored.

Feel free to contact me with any questions or comments!  Once I grow up, further applications of this code can be explored- particularly to live out the ScorePal project name.
