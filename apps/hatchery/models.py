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
from apps.breeders.models import Breeders
from apps.customer.models import Customer

class Hatchery(models.Model):
    """
    Hatchery Model
    """
    id = models.AutoField(primary_key=True)
    name=models.CharField(null=True,blank=True,max_length=50)
    photo = ProcessedImageField(upload_to='hatchery_photos',null=True,blank=True, processors=[ResizeToFit(1280)], format='JPEG', options={'quality': 70})
    email=models.EmailField(null=True,blank=True,max_length=50)
    phone=models.CharField(null=True,blank=True,max_length=15)
    address=models.CharField(null=True,blank=True,max_length=50)
    location=gismodels.PointField(
        srid=4326, 
        null=True, 
        spatial_index=True, 
        geography=True, 
        blank=True)  # Point
    latitude = models.FloatField(null=True,blank=True)
    longitude = models.FloatField(null=True,blank=True)
    totalcapacity=models.IntegerField(null=True,blank=True,max_length=50)    
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']
        db_table = "hatchery"
        verbose_name = 'Hatchery'
        verbose_name_plural = "Hatcheries"
        managed = True


    def __str__(self):
        return self.name

    def __int__(self):
        return self.id
    
    def get_absolute_url(self):
        return '/hatchery/{}'.format(self.name)


class Incubators(models.Model):
    """
    Incubators Model
    """
    id = models.AutoField(primary_key=True)
    hatchery=models.ForeignKey(Hatchery,
        related_name="incubators_hatchery", blank=True, null=True,
        on_delete=models.SET_NULL)
    incubatortype=models.CharField(null=True,blank=True,max_length=50)
    manufacturer=models.CharField(null=True,blank=True,max_length=50)
    model=models.CharField(null=True,blank=True,max_length=15)
    year=models.CharField(null=True,blank=True,max_length=50)
    code=models.CharField(null=True,blank=True,max_length=50)    
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']
        db_table = "incubators"
        verbose_name = 'Incubator'
        verbose_name_plural = "Incubators"
        managed = True

    def get_absolute_url(self):
        return '/incubator/{}'.format(self.code)

class IncubatorCapacity(models.Model):
    """
    IncubatorCapacity Model
    """
    id = models.AutoField(primary_key=True)
    incubator=models.ForeignKey(Incubators,
        related_name="ncubatorcapacity_incubator", blank=True, null=True,
        on_delete=models.SET_NULL)
    breed=models.CharField(null=True,blank=True,max_length=50)
    capacity=models.IntegerField(null=True,blank=True,max_length=50)
    occupied=models.IntegerField(null=True,blank=True,max_length=15)
    available=models.IntegerField(null=True,blank=True,max_length=50)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']
        db_table = "incubator_capacity"
        verbose_name = 'IncubatorCapacity'
        verbose_name_plural = "IncubatorCapacity"
        managed = True  

    def save(self, *args, **kwargs):
        self.available = self.capacity - self.occupied
        super(IncubatorCapacity, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return '/incubator_capacity/{}'.format(self.id)


class EggSetting(models.Model):
    """
    EggSetting Model
    """
    id = models.AutoField(primary_key=True)
    settingcode=models.CharField(null=True,blank=True,max_length=50)
    incubator=models.ForeignKey(Incubators,
        related_name="eggsetting_incubator", blank=True, null=True,
        on_delete=models.SET_NULL)
    customer=models.ForeignKey(Customer,
        related_name="eggsetting_customer", blank=True, null=True,
        on_delete=models.SET_NULL)
    breeders=models.ForeignKey(Breeders,
        related_name="eggsetting_breeders", blank=True, null=True,
        on_delete=models.SET_NULL)
    eggs=models.IntegerField(null=True,blank=True,max_length=50)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']
        db_table = "eggsetting"
        verbose_name = 'EggSetting'
        verbose_name_plural = "EggSettings"
        managed = True

    def get_absolute_url(self):
        return '/egg_setting/{}'.format(self.settingcode)


class Incubation(models.Model):
    """
    Incubation Model
    """
    id = models.AutoField(primary_key=True)
    incubationcode=models.CharField(null=True,blank=True,max_length=50)
    eggsetting=models.ForeignKey(EggSetting,
        related_name="incubation_eggsetting", blank=True, null=True,
        on_delete=models.SET_NULL)
    customer=models.ForeignKey(Customer,
        related_name="incubation_customer", blank=True, null=True,
        on_delete=models.SET_NULL)
    breeders=models.ForeignKey(Breeders,
        related_name="incubation_breeders", blank=True, null=True,
        on_delete=models.SET_NULL)
    eggs=models.IntegerField(null=True,blank=True,max_length=50)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']
        db_table = "incubation"
        verbose_name = 'Incubation'
        verbose_name_plural = "Incubations"
        managed = True

    def get_absolute_url(self):
        return '/incubation/{}'.format(self.incubationcode)


class Candling(models.Model):
    """
    Candling Model
    """
    id = models.AutoField(primary_key=True)
    candlingcode=models.CharField(null=True,blank=True,max_length=50)
    incubation=models.ForeignKey(Incubation,
        related_name="candling_incubation", blank=True, null=True,
        on_delete=models.SET_NULL)
    customer=models.ForeignKey(Customer,
        related_name="candling_customer", blank=True, null=True,
        on_delete=models.SET_NULL)
    breeders=models.ForeignKey(Breeders,
        related_name="candling_breeders", blank=True, null=True,
        on_delete=models.SET_NULL)
    eggs=models.IntegerField(null=True,blank=True,max_length=50)
    candled=models.BooleanField(null=True,blank=True,max_length=50)
    candled_date=models.DateTimeField(null=True,blank=True)
    spoilt_eggs=models.IntegerField(null=True,blank=True,max_length=50)
    fertile_eggs=models.IntegerField(null=True,blank=True,max_length=50)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']
        db_table = "Candling"
        verbose_name = 'Candling'
        verbose_name_plural = "Candling"
        managed = True

    def save(self, *args, **kwargs):
        self.fertile_eggs = self.eggs - self.spoilt_eggs
        super(Candling, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return '/candling/{}'.format(self.candlingcode)


class Hatching(models.Model):
    """
    Hatching Model
    """
    id = models.AutoField(primary_key=True)
    hatchingcode=models.CharField(null=True,blank=True,max_length=50)
    candling=models.ForeignKey(Candling,
        related_name="hatching_candling", blank=True, null=True,
        on_delete=models.SET_NULL)
    customer=models.ForeignKey(Customer,
        related_name="hatching_customer", blank=True, null=True,
        on_delete=models.SET_NULL)
    breeders=models.ForeignKey(Breeders,
        related_name="hatching_breeders", blank=True, null=True,
        on_delete=models.SET_NULL)
    hatched=models.IntegerField(null=True,blank=True,max_length=50)
    deformed=models.IntegerField(null=True,blank=True,max_length=50)
    spoilt=models.IntegerField(null=True,blank=True,max_length=50)
    chicks_hatched=models.IntegerField(null=True,blank=True,max_length=50)
    notify_customer=models.BooleanField(null=True,blank=True,max_length=50)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']
        db_table = "Hatching"
        verbose_name = 'Hatching'
        verbose_name_plural = "Hatching"
        managed = True

    def save(self, *args, **kwargs):
        self.chicks_hatched = self.hatched - self.deformed
        super(Hatching, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return '/Hatching/{}'.format(self.hatchingcode)


class Holding(models.Model):
    """
    Holding Model
    """
    id = models.AutoField(primary_key=True)
    holdingcode=models.CharField(null=True,blank=True,max_length=50)
    hatching=models.ForeignKey(Hatching,
        related_name="holding_hatching", blank=True, null=True,
        on_delete=models.SET_NULL)
    customer=models.ForeignKey(Customer,
        related_name="holding_customer", blank=True, null=True,
        on_delete=models.SET_NULL)
    breeders=models.ForeignKey(Breeders,
        related_name="holding_breeders", blank=True, null=True,
        on_delete=models.SET_NULL)
    customer_delivery=models.BooleanField(null=True,blank=True,max_length=50)
    mode_delivery=models.CharField(null=True,blank=True,max_length=50)
    location=gismodels.PointField(
        srid=4326, 
        null=True, 
        spatial_index=True, 
        geography=True, 
        blank=True)  # Point
    distance=models.FloatField(null=True,blank=True,max_length=50)
    cost=models.FloatField(null=True,blank=True,max_length=50)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']
        db_table = "Holding"
        verbose_name = 'Holding'
        verbose_name_plural = "Holding"
        managed = True

    def save(self, *args, **kwargs):
        self.cost = self.distance #* self.location
        super(Holding, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return '/holding/{}'.format(self.holdingcode)