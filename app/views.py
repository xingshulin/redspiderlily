from django.http import HttpResponse, HttpResponseServerError

from module.dateutil import convert_str2date
from module.report import generate


def generate_report(request):
    params = request.GET
    _from = params.get('_from', '2016-5-9')
    _to = params.get('_to', '2016-5-16')
    mail_group = params.get('mail_group', ['wangzhe@xingshulin.com'])
    time_from = convert_str2date(_from)
    time_to = convert_str2date(_to)
    result = generate(time_from, time_to, mail_group)

    return result


def index(request):
    result = True
    if request.method == 'GET':
        result = generate_report(request)

    if result:
        return HttpResponse("")
    else:
        return HttpResponseServerError("")
