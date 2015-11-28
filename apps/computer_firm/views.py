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
        SELECT maker_id, COUNT(object_id) sum_model
        FROM computer_firm_product WHERE type_product = 'PC'
        GROUP BY maker_id HAVING COUNT(object_id) >= 3
    '''
    cursor.execute(q_20)
    q = cursor.fetchall()
    t_20 = []

    for n in q:
        tmp = list(n)
        tmp[0] = Maker.objects.get(id=tmp[0]).name
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
            FROM (SELECT distinct maker_id m, 'PC' t, 0 c
                FROM computer_firm_product
                UNION ALL
                SELECT distinct maker_id, 'Laptop', 0
                FROM computer_firm_product
                UNION ALL
                SELECT distinct maker_id, 'Printer', 0
                FROM computer_firm_product
                UNION ALL
                SELECT maker_id, type_product, count(*)
                FROM computer_firm_product
                GROUP BY maker_id, type_product
            ) AS qq
            GROUP BY m, t
        ) q1
        JOIN (SELECT maker_id, count(*) cc1
            FROM computer_firm_product
            GROUP BY maker_id
        ) q2
        ON m = maker_id
    '''
    cursor.execute(q_58)
    q = cursor.fetchall()
    t_58 = []

    for n in q:
        tp = list(n)
        tp[0] = Maker.objects.get(id=n[0]).name
        n += (tp,)
        t_58.append(tp)

    q_85 = '''
        SELECT maker_id
        FROM computer_firm_product
        GROUP BY maker_id
        HAVING (SUM(CASE type_product WHEN 'PC' THEN 1 ELSE 0 END) >= 3 AND
            SUM(CASE type_product WHEN 'Printer' THEN 1 ELSE 0 END) = 0 AND
            SUM(CASE WHEN type_product != 'Printer' AND type_product != 'PC'
                THEN 1 ELSE 0 END) = 0
        )
        OR (SUM(CASE type_product WHEN 'PC' THEN 1 ELSE 0 END) = 0 AND
            SUM(CASE type_product WHEN 'Printer' THEN 1 ELSE 0 END) > 0 AND
            SUM(CASE WHEN type_product != 'Printer' AND type_product != 'PC'
                THEN 1 ELSE 0 END) = 0
        )
    '''
    cursor.execute(q_85)
    q = cursor.fetchall()
    t_85 = []

    for n in q:
        tp = list(n)
        tp[0] = Maker.objects.get(id=n[0]).name
        n += (tp,)
        t_85.append(tp)

    return render_to_response(
        template,
        {
            'tikets': tikets,
            'ticket_20': t_20,
            'ticket_24': t_24,
            'ticket_58': t_58,
            'ticket_85': t_85,
        },
        context_instance=RequestContext(request))







# select maker
#   from product 
# group by maker
# having 
# (sum(case type when 'PC' then 1 else 0 end) >=  3 and 
#   sum(case type when 'Printer' then 1 else 0 end)= 0
#  and sum(case when type != 'Printer' and type != 'PC'then 1 else 0 end) = 0)


# or 
# (sum(case type when 'PC' then 1 else 0 end) =0 and 
#   sum(case type when 'Printer' then 1 else 0 end) >  0
#  and sum(case when type != 'Printer' and type != 'PC'then 1 else 0 end) = 0)
