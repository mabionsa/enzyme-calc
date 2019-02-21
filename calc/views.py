# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


def home(request):
    data = {}
    data['home_active'] = True
    data['bialko'] = 35
    # data['enzym'] = 1
    data['procent'] = 100
    data['czas'] = 6
    data['temp'] = 37
    data['trawienie'] = 3
    data['ph'] = 7.4
    data['nacl'] = '200'
    data['kcl'] = '25'
    data['line_n'] = None 
    if request.method == 'POST':
        post = request.POST
        data['bialko'] = post['bialko']
        data['procent'] = post['procent']
        data['czas'] = post['czas']
        data['trawienie'] = post['trawienie']
        data['ph'] = post['ph']
        data['nacl'] = post['nacl']
        data['kcl'] = post['kcl']
        if 'line' in post:
            data['line'] = post['line'].upper()
            data['line_n'] = data['line']
            """
            #line = post['line']
            #n = 2
            #table = [line[i:i+n] for i in range(0, len(line), n)]
            for t in table:
                if 'KK' in t or 'KR' in t or 'RR' in t or 'RK' in t:
                    data['line_n'] += '<span style="color: red;"><strong>%s</strong></span>' % t
                else:
                    data['line_n'] += '%s' % t
            """
            #replacements = {"KK": "<span style='color:red'><strong>KK</strong></span>", "KR": "<span style='color:red'><strong>KR</strong></span>", "RR": "<span style='color:red'><strong>RR</strong></span>", "RK": "<span style='color:red'><strong>RK</strong></span>"}
            #data['line_n'] = "".join([replacements.get(c, c) for c in data['line_n']])
            data['line_n'] = data['line'].replace('KK', '<span style="color: red"><strong>KK</strong></span>').replace('KR', '<span style="color: red"><strong>KR</strong></span>').replace('RR', '<span style="color: red"><strong>RR</strong></span>').replace('RK', '<span style="color: red"><strong>RK</strong></span>')

    data['enzym'] = (int(data['bialko'])/35.0)*(int(data['trawienie'])/3.0)*(6.0/int(data['czas']))*(100.0/int(data['procent']))
    # dla 7.7pH - 68% aktywnosci
    if data['ph'] == '7.7':
        data['enzym'] = data['enzym']*(100.0/68.0)
    if not data['nacl'] == '200':
        data['enzym'] = data['enzym']*(100.0/97.0)
    if data['kcl'] == '50':
        data['enzym'] = data['enzym']*(100.0/86.0)
    if data['kcl'] == '100':
        data['enzym'] = data['enzym']*(100.0/96.0)
    if data['kcl'] == '200':
        data['enzym'] = data['enzym']*(100.0/83.0)
    return render(
        request,
        'index.html',
        data
    )


def about(request):
    data = {}
    data['about_active'] = True
    return render(
        request,
        'about.html',
        data
    )