# -*- coding: utf-8 -*-
# from django.shortcuts import render
# from django.http import HttpResponseRedirect
# from django.views.generic.base import TemplateView
# from django.core.urlresolvers import reverse

# from ..models import AboutUs


from django.shortcuts import render_to_response
from django.template import RequestContext
from django.db import connection

from .models import *


def home_page(request):
    '''View for home page'''
    template = 'home.html'
    cursor = connection.cursor()
    tikets = Tickets.objects.all().order_by('id')

    q_20 = '''
        SELECT marker_id, COUNT(object_id) sum_model
        FROM computer_firm_product WHERE type_product = 'PC'
        GROUP BY marker_id HAVING COUNT(object_id) >= 3
    '''
    cursor.execute(q_20)
    q = cursor.fetchall()
    t_20 = []

    for n in q:
        tmp = list(n)
        tmp[0] = Marker.objects.get(id=tmp[0]).name
        t_20.append(tuple(tmp))

    q_24 = '''
        SELECT model, price
        FROM (SELECT model, price
            FROM computer_firm_pc
            UNION
            SELECT model, price
            FROM computer_firm_laptop
            UNION
            SELECT model, price
            FROM computer_firm_printer) AS m,
            (SELECT MAX(n.price) AS new_price
            FROM (SELECT price
                FROM computer_firm_pc
                UNION
                SELECT price
                FROM computer_firm_laptop
                UNION
                SELECT price
                FROM computer_firm_printer) AS n) AS xz
        WHERE m.price IN (xz.new_price)
    '''

    cursor.execute(q_24)
    q = cursor.fetchall()
    t_24 = []

    for n in q:
        type_product = Product.objects.get(model=n[0])
        n += (type_product.type_product,)
        t_24.append(n)

    q_58 = '''
        SELECT m, t, CAST(100.0*cc/cc1 AS NUMERIC(5,2))
        FROM (SELECT m, t, sum(c) cc
            FROM (SELECT distinct marker_id m, 'PC' t, 0 c
                FROM computer_firm_product
                UNION ALL
                SELECT distinct marker_id, 'Laptop', 0
                FROM computer_firm_product
                UNION ALL
                SELECT distinct marker_id, 'Printer', 0
                FROM computer_firm_product
                UNION ALL
                SELECT marker_id, type_product, count(*)
                FROM computer_firm_product
                GROUP BY marker_id, type_product
            ) AS qq
            GROUP BY m, t
        ) q1
        JOIN (SELECT marker_id, count(*) cc1
            FROM computer_firm_product
            GROUP BY marker_id
        ) q2
        ON m = marker_id
    '''
    cursor.execute(q_58)
    q = cursor.fetchall()
    t_58 = []

    for n in q:
        tp = list(n)
        tp[0] = Marker.objects.get(id=n[0]).name
        n += (tp,)
        t_58.append(tp)

    return render_to_response(
        template,
        {
            'tikets': tikets,
            'ticket_20': t_20,
            'ticket_24': t_24,
            'ticket_58': t_58,
        },
        context_instance=RequestContext(request))
