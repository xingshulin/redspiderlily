from datetime import date
from django.http import HttpResponse, HttpResponseServerError

from module.report import generate


def index(request):
    _from = date(2016, 5, 9)
    _to = date(2016, 5, 16)
    result = generate(_from, _to)
    if result:
        return HttpResponse("")
    else:
        return HttpResponseServerError("")
