#!/usr/bin/python

from crontab import CronTab

empty_cron = CronTab()
my_user_cron = CronTab(user=True)
users_cron = CronTab(user='harounahmed')

#file_cron = CronTab(tabfile='UVAwin.py')
#mem_cron = CronTab(tab="""
#  * * * * * /Library/Frameworks/Python.framework/Versions/2.7/bin ~/Desktop/PersonalProjects/ScorePal/UVAwin.py
#""")

job = empty_cron.new(command='python ~/Desktop/PersonalProjects/ScorePal/UVAwin.py')

job.minute.every(1)

for job in empty_cron:
    print job

#job_standard_output = job.run()

#cron.write_to_user( user=True )
