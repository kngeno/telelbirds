# -*- coding: utf-8 -*-
#########################################################################
#
# Copyright (C) 2020:  TelelBirds
#
#
#########################################################################
from __future__ import unicode_literals
import os
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator

from django.db import models
from django.db.models import ImageField
from django.utils.safestring import mark_safe
from django.template.defaultfilters import truncatechars, slugify  # or truncatewords
from django.contrib.gis.db import models as gismodels

from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit

from telelbirds import settings
from apps.breeders.models import Breeders, Breed
from apps.hatchery.models import Hatchery
from apps.customer.models import Customer, Eggs


class Chicks(models.Model):
    """
    Chicks Model
    """
    id = models.AutoField(primary_key=True)
    batchnumber=models.CharField(null=True,blank=True,max_length=50)
    source=models.CharField(null=True,blank=True,max_length=50)
    breed=models.ForeignKey(Breed,
        related_name="breed_chicks", blank=True, null=True,
        on_delete=models.SET_NULL)
    age=models.DateField(null=True,blank=True,max_length=50)
    number=models.IntegerField(null=True,blank=True,max_length=50)
    description=models.TextField(null=True,blank=True) 
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']
        db_table = "chicks"
        verbose_name = 'Chick'
        verbose_name_plural = "Chicks"
        managed = True
    
    def get_absolute_url(self):
        return '/chicks/{}'.format(self.batchnumber)


class Mortality(models.Model):
    """
    Mortality Model
    """
    id = models.AutoField(primary_key=True)
    batchnumber=models.CharField(null=True,blank=True,max_length=50)
    mortalitynumber=models.CharField(null=True,blank=True,max_length=50)
    chicks=models.ForeignKey(Chicks,
        related_name="chicks_mortality", blank=True, null=True,
        on_delete=models.SET_NULL)
    age=models.DateField(null=True,blank=True,max_length=50)
    number=models.IntegerField(null=True,blank=True,max_length=50)
    mortality=models.IntegerField(null=True,blank=True,max_length=50)
    reason=models.TextField(null=True,blank=True)
    notify_vet=models.BooleanField(null=True,blank=True,max_length=50) 
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']
        db_table = "mortality"
        verbose_name = 'Mortality'
        verbose_name_plural = "Mortality"
        managed = True
    
    def get_absolute_url(self):
        return '/mortality/{}'.format(self.mortalitynumber)


class ChicksSold(models.Model):
    """
    ChicksSold Model
    """
    id = models.AutoField(primary_key=True)
    batchnumber=models.CharField(null=True,blank=True,max_length=50)
    salesnumber=models.CharField(null=True,blank=True,max_length=50)
    customer_type=models.CharField(null=True,blank=True,max_length=50)
    chicks=models.ForeignKey(Chicks,
        related_name="chicks_chickssold", blank=True, null=True,
        on_delete=models.SET_NULL)
    age=models.DateField(null=True,blank=True,max_length=50)
    number=models.IntegerField(null=True,blank=True,max_length=50)
    price=models.FloatField(null=True,blank=True)
    sales=models.FloatField(null=True,blank=True)  
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']
        db_table = "chickssold"
        verbose_name = 'ChicksSold'
        verbose_name_plural = "ChicksSold"
        managed = True
    
    def save(self, *args, **kwargs):
        self.sales = self.price - self.number
        super(ChicksSold, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return '/chicks_sold/{}'.format(self.salesnumber)


class ChicksAvailable(models.Model):
    """
    ChicksAvailable Model
    """
    id = models.AutoField(primary_key=True)
    batchnumber=models.CharField(null=True,blank=True,max_length=50)
    breed=models.ForeignKey(Breed,
        related_name="breed_chicksavailable", blank=True, null=True,
        on_delete=models.SET_NULL)
    age=models.DateField(null=True,blank=True,max_length=50)
    number=models.IntegerField(null=True,blank=True,max_length=50)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']
        db_table = "chicksavailable"
        verbose_name = 'ChicksAvailable'
        verbose_name_plural = "ChicksAvailable"
        managed = True
    
    def get_absolute_url(self):
        return '/chicks_available/{}'.format(self.batchnumber)