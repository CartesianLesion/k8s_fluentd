# app.py


from flask import Flask, request
import time
import atexit
from apscheduler.schedulers.background import BackgroundScheduler
from random import randint, choice
from socket import inet_ntoa
from struct import pack
from log import logger


app = Flask(__name__)

with open('firstnames.txt', 'r') as f:
    first_names = f.read().splitlines()

with open('lastnames.txt', 'r') as f:
    last_names = f.read().splitlines()


@app.route('/')
def default():
    remote_addr = request.remote_addr
    return 'Welcome'


def log_date_time():
    user = f'{choice(first_names)}.{choice(last_names)}'
    rand_ip = inet_ntoa(pack('>I', randint(1, 0xffffffff)))
    logger.info(f'App is running, sourceip={rand_ip}, user={user}')
    print(f'App is running, sourceip={rand_ip}, user={user}')


scheduler = BackgroundScheduler()
scheduler.add_job(func=log_date_time, trigger="interval", seconds=5)
scheduler.start()

# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())


if __name__ == "__main__":
    app.run(host='0.0.0.0')

