# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *
# Register your models here.
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id','header',)
    list_per_page = 25
    
admin.site.register(News, NewsAdmin)