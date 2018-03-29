# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.

class News(models.Model):
    header = models.CharField(_('header'),max_length=100, null=True, blank=True)
    description = models.TextField(_('description'))

    def __unicode__(self):
        return self.header