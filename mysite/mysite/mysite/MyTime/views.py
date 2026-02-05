from datetime import datetime
from zoneinfo import ZoneInfo

from django.shortcuts import render


def index(request):
    malaysia_time = datetime.now(ZoneInfo('Asia/Kuala_Lumpur'))
    context = {'malaysia_time': malaysia_time}
    return render(request, 'MyTime/index.html', context)
