This project was inspired by my friend Big Nick, who is a Duke fan because he sucks (and maybe partly because he went there.)  

Big Nick loves to show me the website diddukewin.com, everytime duke basketball wins. I went to Virginia, so this is absurdly irritating.  I wanted to pay him back for this, but unfortunately the domain name diduvawin.com was taken, so I had to get creative.

As such, I decided to create a script that sent him an email when UVA basketball won with the score.... repeatedly.  I took live site scores from MSNBC sports, which houses them in JSON format.  Thanks Chris Riccomoni (@criccomini)!

I then took the SendGrid Messenger API (V3) which is a RESTful API used for sending emails.  With this, I was able to customize and automate the sending of the scores to a set list of recipients, whether that be to torment my friend Big Nick, or more usefully a preset list of users that wanted a reminder everytime their team was playing.
