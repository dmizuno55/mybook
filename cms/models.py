# coding: utf-8

from django.db import models

class Book(models.Model):
    """$B=q@R(B"""
    name = models.CharField(u'$B=q@RL>(B', max_length=255)
    publisher = models.CharField(u'$B=PHG<R(B', max_length=255, blank=True)
    page = models.IntegerField(u'$B%Z!<%8?t(B', blank=True, default=0)

    def __str__(self):
        return self.name


class Impression(models.Model):
    """$B46A[(B"""
    book = models.ForeignKey(Book, verbose_name=u'$B=q@R(B', related_name='impressions')
    comment = models.TextField(u'$B%3%a%s%H(B', blank=True)

    def __str__(self):
        return self.comment

