# -*- coding: utf-8 -*-
#########################################################################
#
# Copyright (C) 2020:  TelelBirds
#
#
#########################################################################
from django.contrib import admin
from apps.breeders.models import Breed, Breeders

admin.site.register(Breed)
admin.site.register(Breeders)