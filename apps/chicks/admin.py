# -*- coding: utf-8 -*-
#########################################################################
#
# Copyright (C) 2020:  TelelBirds
#
#
#########################################################################
from django.contrib import admin
from apps.chicks.models import Chicks,Mortality,ChicksSold,ChicksAvailable

admin.site.register(Chicks)
admin.site.register(Mortality)
admin.site.register(ChicksSold)
admin.site.register(ChicksAvailable)