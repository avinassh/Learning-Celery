import time
from celery import shared_task


def start_game():
    print('I am in start_game and scheduling the task now')
    print('It will run after 10 secs %s' % time.ctime())
    # stop_game.delay(kwargs={'param': 'delay avi'})
    stop_game.apply_async(kwargs={'param': 'avi'}, countdown=10)


@shared_task
def stop_game(param):
    print('Received task at: %s' % time.ctime())
    print('param: %s' % param)
