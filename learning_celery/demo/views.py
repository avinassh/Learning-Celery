from django.http import HttpResponse

from .tasks import start_game


def index(request):
    start_game()
    return HttpResponse('Task Scheduled')
