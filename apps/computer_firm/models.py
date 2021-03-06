# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic


class Maker(models.Model):
    ''' Model Marker '''
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return u"%s" % (self.name)


class Laptop(models.Model):
    ''' Model Laptop '''

    class Meta(object):
        verbose_name = u"Laptop"
        verbose_name_plural = u"Laptop"

    model = models.CharField(max_length=50)
    speed = models.IntegerField()
    ram = models.IntegerField()
    hd = models.FloatField()
    price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        null=True,
        default=0
    )
    screen = models.IntegerField()

    def __unicode__(self):
        return u"%s" % (self.model)


class Pc(models.Model):
    model = models.CharField(max_length=10)
    speed = models.IntegerField()
    ram = models.IntegerField()
    hd = models.FloatField()
    cd = models.CharField(max_length=10)
    price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        null=True,
        default=0
    )

    def __unicode__(self):
        return u"%s" % (self.model)


class Printer(models.Model):
    model = models.CharField(max_length=50)
    color = models.CharField(max_length=1)
    type_printer = models.CharField(max_length=50)
    price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        null=True,
        default=0
    )

    def __unicode__(self):
        return u"%s" % (self.model)


class Product(models.Model):
    maker = models.ForeignKey(Maker)
    model = models.CharField(max_length=50)
    type_product = models.CharField(max_length=50)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    def __unicode__(self):
        return u"%s %s %s" % (self.maker, self.content_object.model, self.type_product)


class Tickets(models.Model):
    name = models.CharField(max_length=20)
    context = models.TextField()

    def __unicode__(self):
        return u"%s" % (self.name)
