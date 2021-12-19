#https://stackabuse.com/scheduling-jobs-with-python-crontab/
from crontab import CronTab

cron = CronTab()
job = cron.new(command='/media/miro/Acer/Users/Miro/My Drive/Python_projects/Stock_Reporter')
job.minute.every(3)

